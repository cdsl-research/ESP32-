import network
import urequests
import machine
import time
import utime
from machine import Pin


#execfile("wifi-password.py")
SSID_NAME = ""
SSID_PASS = ""

# サーバーのIPアドレスとポート番号
SERVER_IP = ''
SERVER_PORT = 8000

# 更新ファイルのリスト
update_files = ['test_1.py','test_2.py','test_3.py']
update_index = 0

# ピン設定
led_blue = machine.Pin(2, Pin.OUT)

# WiFiに接続する関数
def connect_wifi(ssid, passkey, timeout=10):
    wifi = network.WLAN(network.STA_IF)
    if wifi.isconnected():
        print('WiFiに接続済み。接続をスキップします。')
        return wifi
    else:
        wifi.active(True)
        wifi.connect(ssid, passkey)
        while not wifi.isconnected() and timeout > 0:
            print('.')
            utime.sleep(1)
            timeout -= 1

    if wifi.isconnected():
        print('WiFiに接続しました')
        led_blue.value(1)
        return wifi
    else:
        print('WiFiへの接続に失敗しました')
        return None

# サーバーに接続を通知する関数
def notify_server(path):
    url = f'http://{SERVER_IP}:{path}'
    response = urequests.get(url)
    if response.status_code == 200:
        print(f'サーバーに通知しました: {path}')
    response.close()

# 更新プログラムをダウンロードする関数
def download_update(file_index):
    time.sleep(3)
    url = f'http://{SERVER_IP}:{SERVER_PORT}/update'
    response = urequests.get(url)
    if response.status_code == 200:
        file_path = update_files[file_index]
        print(f"{file_path}のプログラムを受け取りました。更新を開始します")
        #while True:
            #if not button_pin_request.value():
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f'更新プログラムをダウンロードしました: {file_path}')
        response.close()
    else:
        print(f'更新プログラムのダウンロードに失敗しました: ステータスコード {response.status_code}')
        response.close()

# LEDを点滅させる関数
def blink_led(duration, interval=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        led_blue.value(1)
        time.sleep(interval)
        led_blue.value(0)
        time.sleep(interval)

# メインプログラムの実行部分
print('WiFiに接続します...')
connect_wifi(SSID_NAME, SSID_PASS)


while True:
    notify_server(f'{SERVER_PORT}/connect')
    print("サーバーに接続しました")
    while True:
        download_update(update_index)
        update_index += 1
        notify_server(f'{SERVER_PORT}/complete')
        print("-----------------------------")
        if update_index >= len(update_files):
            print("全ての更新終了")
            blink_led(10)
            break# 10秒間LEDを点滅させる
    break



