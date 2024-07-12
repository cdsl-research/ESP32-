import machine
import time
import utime
import os
#import bmp280  # 先ほどのコードをbmp280.pyとして保存しておく
execfile("BMP280_module.py")

# I2Cバスの初期化
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))

# BMP280の初期化
init_bmp280(i2c)


while True:
    temp = read_temp(i2c)
    pres = read_pressure(i2c)
    print(f"Temperature: {temp} C")
    print(f"Pressure: {pres} hPa")
    print("---------------------")
    if count >= 60:
        break
    count = count +1
    
    time.sleep(1)

