import machine
import time
import utime
import os
#import bmp280  # 先ほどのコードをbmp280.pyとして保存しておく
execfile("BMP280_module.py")

file_name = "bmp280__FULL.csv"
count = 1
# I2Cバスの初期化
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))

# BMP280の初期化
init_bmp280(i2c)

start_time_ms = utime.ticks_ms()

# データの取得と表示
f = open(file_name, "w", encoding="UTF-8")
f.write(f"count,time,temp,pres,\n")
f.close()

while True:
    temp = read_temp(i2c)
    pres = read_pressure(i2c)
    print(f"Temperature: {temp} C")
    print(f"Pressure: {pres} hPa")
    current_time_ms = utime.ticks_ms()
    time_data = (current_time_ms - start_time_ms) / 1000
    print(f"time_data:{time_data}秒")
    
    with open(file_name, "a") as f:
        f.write(f"{count},{time_data},{temp},{pres}\n")

    print(f"count{count}")
    print("---------------------")
    if count >= 60:
        break
    count = count +1
    
    time.sleep(1)
