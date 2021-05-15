#!/usr/bin/python3
import json
import sys
sys.path.append(r'/opt/ezblock')
from vilib import Vilib
from ezblock import WiFi

with open('config.json', 'r') as configuration:
  data=configuration.read()

obj = json.loads(data)

Vilib.camera_start(True)
Vilib.color_detect_switch(True)
Vilib.detect_color_name('red')
WiFi().write(str(obj['country']), str(obj['ssid']), str(obj['key']))


def forever():
  pass

if __name__ == "__main__":
    while True:
        forever()
