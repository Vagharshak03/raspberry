from bme_280 import BME280
from ltr_390 import LTR390
from pms_5003 import PMS5003
import json


bme280 = BME280()
ltr390 = LTR390()
pms5003 = PMS5003()
json_string = json.dumps(pms5003.read_pms_data())

print(f'BME280 data --> {bme280.read_bme_data()}')
print(f'LTR390 data --> {ltr390.read_ltr_data()}')
print(f'PMS5003 data -> {json_string}')
