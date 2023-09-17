#!/bin/bash
export DISPLAY=":0"
 nohup python3 /home/pi/python-ui/grid-clock2.py > clock.log 2>&1 &
