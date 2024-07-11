from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import time

SERVER_IP = ''
SERVER_PORT = 8000
update_files = ['update_1.py', 'update_2.py', 'update_3.py']  # 更新ファイルのリスト
device_updates = {}
lock = threading.Lock()

class OTAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global device_updates

        if self.path == '/connect':
            client_ip = self.client_address[0]
            with lock:
                if client_ip not in device_updates:
                    device_updates[client_ip] = 0  # 新しいデバイスのために更新インデックスを初期化
            self.send_response(200)
            self.end_headers()
            print(f'デバイスが接続しました:')
            #print(f'デバイスが接続しました: {client_ip}')

        elif self.path.startswith('/update'):
            client_ip = self.client_address[0]
            with lock:
                update_index = device_updates.get(client_ip, 0)
                if update_index < len(update_files):
                    file_path = update_files[update_index]
                    self.send_response(200)
                    self.send_header('Content-type', 'application/octet-stream')
                    self.end_headers()
                    with open(file_path, 'rb') as file:
                        self.wfile.write(file.read())
                    print(f"更新ファイルを送信しました: {file_path} to {client_ip}")
                else:
                    self.send_response(404)
                    self.end_headers()

        elif self.path == '/complete':
            client_ip = self.client_address[0]
            self.send_response(200)
            self.end_headers()
            with lock:
                if client_ip in device_updates:
                    device_updates[client_ip] += 1  # 更新インデックスを増加
                    print(f'デバイスが更新を完了しました: 更新インデックス: {device_updates[client_ip]}')
                    if device_updates[client_ip] >= len(update_files):
                        print(f'{client_ip} のすべての更新が完了しました。')

def run_server():
    server_address = (SERVER_IP, SERVER_PORT)
    httpd = HTTPServer(server_address, OTAHandler)
    print('OTAサーバーを起動します...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('OTAサーバーを停止します。')

if __name__ == '__main__':
    run_server()
