import conf
from boltiot import Bolt
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
response = mybolt.analogWrite('0', '155')
print(response)


