import json
import logging
from threading import Thread
import socket
import urllib.parse
from pathlib import Path
import mimetypes
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler


BASE_DIR = Path(__file__).parent
BUFFER_SIZE = 1024
HTTP_PORT = 3000
HTTP_HOST = '0.0.0.0'
SOCKET_HOST = '127.0.0.1'
SOCKET_PORT = 5000

storage_path = BASE_DIR / 'storage'
data_file = storage_path / 'data.json'
storage_path.mkdir(parents=True, exist_ok=True)
if not data_file.exists():
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump({}, file, ensure_ascii=False, indent=4)

class GoitFramework(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        match pr_url.path:
            case '/':
                self.send_html_file("index.html")
            case '/message':
                self.send_html_file("message.html")
            case _:
                file_path = BASE_DIR / 'public' / pr_url.path.strip("/")
                if file_path.exists():
                    self.send_static(file_path)
                else:
                    self.send_html_file('error.html', 404)

    def do_POST(self):
        size = self.headers.get('Content-Length')
        data = self.rfile.read(int(size))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(data, (SOCKET_HOST, SOCKET_PORT))
        client_socket.close()
        self.send_response(302)
        self.send_header('Location', '/message')
        self.end_headers()

    def send_html_file(self, filename, status_code=200):
        file_path = BASE_DIR / 'templates' / filename
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(file_path, 'rb') as file:
            self.wfile.write(file.read())

    def send_static(self, file_path, status_code=200):
        self.send_response(status_code)
        mime_type, _ = mimetypes.guess_type(file_path)
        self.send_header("Content-type", mime_type or 'application/octet-stream')
        self.end_headers()
        with open(file_path, 'rb') as file:
            self.wfile.write(file.read())

def save_data_from_form(data):
    parse_data = urllib.parse.parse_qs(data.decode())
    parsed_dict = {key: value[0] for key, value in parse_data.items()}
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    with open(data_file, 'r+', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}
        data[current_time] = parsed_dict
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.truncate()

def run_socket_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    logging.info("Starting socket server")
    try:
        while True:
            msg, address = server_socket.recvfrom(BUFFER_SIZE)
            logging.info(f"Socket received from {address}: {msg}")
            save_data_from_form(msg)
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()

def run_http_server(host, port):
    address = (host, port)
    http_server = HTTPServer(address, GoitFramework)
    logging.info('Starting HTTP server')
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        http_server.server_close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    http_server_thread = Thread(target=run_http_server, args=(HTTP_HOST, HTTP_PORT))
    socket_server_thread = Thread(target=run_socket_server, args=(SOCKET_HOST, SOCKET_PORT))

    http_server_thread.start()
    socket_server_thread.start()
