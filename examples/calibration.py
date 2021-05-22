#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)

from picarmini import dir_servo_angle_calibration

dir_servo_angle_calibration(0)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)

print("Calibrated all servos.")

