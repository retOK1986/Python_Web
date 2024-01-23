from pathlib import Path
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
import file_parser
from normalize import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    shutil.move(str(file_name), str(target_folder / normalize(file_name.name)))

def handle_files(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    normalized_name = normalize(file_name.stem) + file_name.suffix
    file_name.replace(target_folder / normalized_name)
def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.stem)
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name), str(folder_for_file))
        file_name.unlink()
    except shutil.ReadError:
        folder_for_file.rmdir()

def main(folder: Path):
    file_parser.scan(folder)
    with ThreadPoolExecutor() as executor:
        # Збереження зображення в папку images
        for file in file_parser.JPEG_IMAGES:
            executor.submit(handle_media, file, folder / 'images' / 'JPEG')
        for file in file_parser.JPG_IMAGES:
            executor.submit(handle_media, file, folder / 'images' / 'JPG')
        for file in file_parser.PNG_IMAGES:
            executor.submit(handle_media, file, folder / 'images' / 'PNG')
        for file in file_parser.SVG_IMAGES:
            executor.submit(handle_media, file, folder / 'images' / 'SVG')
        # Збереження відео файлів в папку video
        for file in file_parser.AVI_VIDEO:
            executor.submit(handle_media, file, folder / 'video' / 'AVI')
        for file in file_parser.MP4_VIDEO:
            executor.submit(handle_media, file, folder / 'video' / 'MP4')
        for file in file_parser.MOV_VIDEO:
            executor.submit(handle_media, file, folder / 'video' / 'MOV')
        for file in file_parser.MKV_VIDEO:
            executor.submit(handle_media, file, folder / 'video' / 'MKV')
        # Збереження документів в папку documents
        for file in file_parser.DOC_DOCUMENTS:
            executor.submit(handle_media, file, folder / 'documents' / 'DOC')
        for file in file_parser.DOCX_DOCUMENTS:
            executor.submit(handle_media, file, folder / 'documents' / 'DOCX')
        for file in file_parser.TXT_DOCUMENTS:
            executor.submit(handle_media, file, folder / 'documents' / 'TXT')
        for file in file_parser.PDF_DOCUMENTS:
            executor.submit(handle_media, file, folder / 'documents' / 'PDF')
        for file in file_parser.XLSX_DOCUMENTS:
            executor.submit(handle_media, file, folder / 'documents' / 'XLSX')
        for file in file_parser.PPTX_DOCUMENTS:
            executor.submit(handle_media, file, folder / 'documents' / 'PPTX')
        # Збереження аудіо файлів в папку audio
        for file in file_parser.MP3_AUDIO:
            executor.submit(handle_media, file, folder / 'audio' / 'MP3')
        for file in file_parser.OGG_AUDIO:
            executor.submit(handle_media, file, folder / 'audio' / 'OGG')
        for file in file_parser.WAV_AUDIO:
            executor.submit(handle_media, file, folder / 'audio' / 'WAV')
        for file in file_parser.AMR_AUDIO:
            executor.submit(handle_media, file, folder / 'audio' / 'AMR')
        # Збереження  архівних файлів в папку archives
        for file in file_parser.ZIP_ARCHIVES:
            executor.submit(handle_archive, file, folder / 'archives' / 'ZIP')
        for file in file_parser.GZ_ARCHIVES:
            executor.submit(handle_archive, file, folder / 'archives' / 'GZ')
        for file in file_parser.TAR_ARCHIVES:
            executor.submit(handle_archive, file, folder / 'archives' / 'TAR')
    #    Збереження файлів які відсуині у списку в папку  MY_OTHER
        for file in file_parser.MY_OTHER:
            executor.submit(handle_files, file, folder / 'MY_OTHER')

    for folder in file_parser.FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_process = Path(sys.argv[1])
    else:
        print("You did not specify a folder path. Please specify the path as an argument")
        sys.exit(1)
    main(folder_process.resolve())
