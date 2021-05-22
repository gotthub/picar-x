#!/usr/bin/python3
import json
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from vilib import Vilib
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import WiFi
from ezblock import print

with open('config.json', 'r') as configuration:
  data=configuration.read()

obj = json.loads(data)

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
WiFi().write(str(obj['country']), str(obj['ssid']), str(obj['key']))

def forever():
  print("%s"%(''.join([str(x) for x in ['There are ', Vilib.human_detect_object('number'), ' people']])))

if __name__ == "__main__":
    while True:
        forever()  