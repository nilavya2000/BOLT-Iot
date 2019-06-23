import conf
from boltiot import Bolt
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
response = mybolt.digitalWrite('0', 'HIGH')
print(response)
