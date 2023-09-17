#!/bin/bash
export DISPLAY=":0"
python3 /home/pi/lift/keypad16_pcf8574.py &> a.log &
python3 /home/pi/lift/lift.py &> b.log &
