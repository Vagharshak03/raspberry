import time
import smbus2
import bme280

address = 0x76

bus = smbus2.SMBus(1)

calibration_param = bme280.load_calibration_params(bus, address)

while True:
    data = bme280.sample(bus, address, calibration_param)

    temperature = data.temperature
    pressure = data.pressure
    humidity = data.humidity

    print(f'Temperature = {temperature}')

    time.sleep(2)
