from bme_280 import BME280
from ltr_390 import LTR390

bme280 = BME280()
ltr390 = LTR390()

print(f'BME280 data --> {bme280.read_bme_data()}')
print(f'LTR390 data --> {ltr390.read_ltr_data()}')
