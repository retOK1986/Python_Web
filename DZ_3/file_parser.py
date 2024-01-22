import sys
from pathlib import Path
# Зображення
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
# Відео файли
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
# Документич
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
# Музика
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
# Архіви
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
# Інші файли
MY_OTHER = []

REGISTER_EXTENSION = {
    # Зображення
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    # Відео файли
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    # Документи
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    # Музика
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    # Архіви
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # .mp4, .mov, .avi
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    # Зображення
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    # Відео файли
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
    # Документи
    print(f'Documents doc: {DOC_DOCUMENTS}')
    print(f'Documents docx: {DOCX_DOCUMENTS}')
    print(f'Documents txt: {TXT_DOCUMENTS}')
    print(f'Documents pdf: {PDF_DOCUMENTS}')
    print(f'Documents xlsx: {XLSX_DOCUMENTS}')
    print(f'Documents pptx: {PPTX_DOCUMENTS}')
    # Музика
    print(f'audio mp3: {MP3_AUDIO}')
    print(f'audio ogg: {OGG_AUDIO}')
    print(f'audio wav: {WAV_AUDIO}')
    print(f'audio amr: {AMR_AUDIO}')
    # Архіви
    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f'Archives gz: {GZ_ARCHIVES}')
    print(f'Archives tar: {TAR_ARCHIVES}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
    print(f'FOLDERS: {FOLDERS}')









