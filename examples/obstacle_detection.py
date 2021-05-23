#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)

#motion
from picarmini import dir_servo_angle_calibration
from picarmini import forward

from picarmini import backward
from picarmini import set_dir_servo_angle
from picarmini import stop

#ultrasonic
from ezblock import Pin
from ezblock import Ultrasonic

#programming
from ezblock import print
from ezblock import delay

dir_servo_angle_calibration(0)
distance = None
pin_D0=Pin("D0")
pin_D1=Pin("D1")

def forever():
  global distance
  distance = Ultrasonic(pin_D0, pin_D1).read()
  print("%s"%distance)
  delay(100)

  forward(50)
  delay(1000)
  backward(50)
  delay(1000)
  forward(50)
  set_dir_servo_angle((-30))
  delay(1000)
  forward(50)
  set_dir_servo_angle(30)
  delay(1000)
  set_dir_servo_angle(0)
  stop()
  delay(2000)



if __name__ == "__main__":
    while True:
        forever()  
