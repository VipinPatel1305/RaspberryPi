#!/bin/bash
sleep 300
echo "script called during boot at hw clock time `date`" 

echo "boot complete `date`" 
function start_whitenoise(){
        amixer cset numid=1 5%

        mpg321 /home/pi/whitenoise/rain_w.mp3 &
        for v in {1..100}
        do
                amixer cset numid=1 $v%
                sleep 5
        done
	echo "====max volume===" 
}

start_whitenoise


