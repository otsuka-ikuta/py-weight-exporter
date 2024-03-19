from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import time
import urequests
import unit

weigh_0 = unit.get(unit.WEIGHT, unit.PORTA)
wd = None

def buttonA_wasPressed():
  global wd
  weigh_0.set_calibrate_scale(265000)
  pass
btnA.wasPressed(buttonA_wasPressed)

wifiCfg.doConnect('ssid', 'password')
rgb.setColorAll(0xcc0000)
while not (wifiCfg.wlan_sta.isconnected()):
  wait(1)
rgb.setColorAll(0x33cc00)
wait(5)
weigh_0.zero()
while True:
  if wifiCfg.wlan_sta.isconnected():
    rgb.setColorAll(0x000099)
    wd = str((weigh_0.weight))
    wd = (str('http://10.0.8.40:5000/set_gauge/') + str(wd))
    try:
      req = urequests.request(method='GET', url=wd, headers={})
      gc.collect()
      req.close()
    except:
      pass
  else:
    rgb.setColorAll(0xcc0000)
    wait_ms(20)
  rgb.setColorAll(0x000000)
  wait(5)
  wait_ms(2)
