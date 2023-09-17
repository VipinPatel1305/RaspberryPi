#!/bin/bash
dir="/home/pi/webserver/dashcam"
while true
do
	touch $dir/dashcam.txt
	echo "Started at: $(date)" >> $dir/dashcam.txt
	libcamera-vid -t 30000 -n -b 900000 --width 1920 --height 1080 --codec libav --libav-format mp4  -o $dir/dashcam.mp4 &>/dev/null
	echo "completed at $(date)" >> $dir/dashcam.txt
	printf -v filename '%(%Y-%m-%d-%H:%M:%S)T' -1
	echo "filename $filename"
	mv $dir/dashcam.mp4 "$dir/$filename-dashcam.mp4"
	sleep 3
done

