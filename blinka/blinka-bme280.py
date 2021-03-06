#!/usr/bin/python3

import time
import board
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
sensor.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.humidity)
    print("Pressure: %0.1f hPa" % sensor.pressure)
    print("Altitude = %0.2f meters" % sensor.altitude)
    time.sleep(2)
