# 遠隔で行うESP32のソフトウェアアップデート
SimpleHTTPServerを使用したESP32のソフトウェアアップデート


## OTA.py
ESP32用のコードで, ESP32をクライアントとし遠隔更新を行うためのコードです.

## SimpleHTTPServer.py
PC等のサーバー用のコードで, Pythonの標準ライブラリの1つであるSimpleHTTPServerを実験環境として扱うためのコードです.


## BMP280.py
これはBMP280気圧センサのセンサープログラムで, アップデート後の数値の確認のために使用した. BMP280_module.pyと一緒にESP32に入れてください.

## BMP280_module.py
これはBMP280気圧センサの気圧と温度を算出するためのプログラムです. BMP280.pyと一緒にESP32に入れてください.
