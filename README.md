# 遠隔で行うESP32のソフトウェアアップデート
SimpleHTTPServerを使用したESP32のソフトウェアアップデート

## サーバー

### SimpleHTTPServer.py
サーバー用のコードで, Pythonの標準ライブラリの1つであるSimpleHTTPRequestHandlerを実験環境として扱うためのコードです.

  ・run_server()：サーバーIPとサーバーポートを参照してサーバーの開設を行い, 通信・ファイルの送受信の処理が行われる

## クライアント(ESP32)

### OTA.py
ESP32用のコードで, ESP32をクライアントとし遠隔更新を行うためのコードです.

  ・connect_wifi()：SSID_NAME(WI-Fiの名前), SSID_PASS(Wi-Fiのパスワード)を参照してWi-Fi接続を行う.

  ・notify_server()：引数にサーバーIP：サーバーポート：Pathを指定して, サーバー接続やタスク完了のリクエストを送信する.
  
  ・download_update()：更新を行うためのリクエストを行い, 返ってきたレスポンスのファイルをクライアント内に保存, または対象のファイルを更新する.
  
  ・Wi-Fi接続の状態と更新完了後の動作を可視化するためled_blueとblink_led()を使用し, 内臓LEDを点灯・点滅させる.

## 実行の仕方
サーバーでSimpleHTTPServer.pyを実行し,「OTAサーバーを起動します...」が表示されるのを確認し, クライアントでOTA.pyを実行し, ソフトウェアのアップデートを行います.

サーバーでの実行結果
```
OTAサーバーを起動します...
[SERVER_IP-ESP32] - - [11/Jul/2024 14:46:00] "GET /connect HTTP/1.0" 200 -
デバイスが接続しました:
[SERVER_IP-ESP32]  - - [11/Jul/2024 14:46:03] "GET /update HTTP/1.0" 200 -
更新ファイルを送信しました: update_1.py to [SERVER_IP-ESP32]
[SERVER_IP-ESP32]  - - [11/Jul/2024 14:46:04] "GET /complete HTTP/1.0" 200 -
デバイスが更新を完了しました: 更新インデックス: 1
[SERVER_IP-ESP32]  - - [11/Jul/2024 14:46:07] "GET /update HTTP/1.0" 200 -
更新ファイルを送信しました: update_2.py to [SERVER_IP-ESP32]
[SERVER_IP-ESP32]  - - [11/Jul/2024 14:46:07] "GET /complete HTTP/1.0" 200 -
デバイスが更新を完了しました: 更新インデックス: 2
[SERVER_IP-ESP32]  - - [11/Jul/2024 14:46:10] "GET /update HTTP/1.0" 200 -
更新ファイルを送信しました: update_3.py to [SERVER_IP-ESP32]
[SERVER_IP-ESP32]  - - [11/Jul/2024 14:46:11] "GET /complete HTTP/1.0" 200 -
デバイスが更新を完了しました: 更新インデックス: 3
[SERVER_IP-ESP32]  のすべての更新が完了しました。

```

クライアントでの実行結果
```

WiFiに接続します...
.
.
.
.
WiFiに接続しました
サーバーに通知しました: 8000/connect
サーバーに接続しました
test_1.pyのプログラムを受け取りました。更新を開始します
更新プログラムをダウンロードしました: test_1.py
サーバーに通知しました: 8000/complete
-----------------------------
test_2.pyのプログラムを受け取りました。更新を開始します
更新プログラムをダウンロードしました: test_2.py
サーバーに通知しました: 8000/complete
-----------------------------
test_3.pyのプログラムを受け取りました。更新を開始します
更新プログラムをダウンロードしました: test_3.py
サーバーに通知しました: 8000/complete
-----------------------------
全ての更新終了


```

詳しいやり方は下記のQiitaに乗っているので参考にしてください.

Qiita URL：https://qiita.com/c0a21121/items/16cf2bbd1ab025109338　
