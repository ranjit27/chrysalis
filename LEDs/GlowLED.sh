#!/bin/bash

GPIO18="18"
GPIO17="17"
OUT="out"
IN="in"

set_gpio_mode () {
        set="gpio -g mode $1 out"
        $set
}

pattern_1() {
	led_on1="gpio -g write $GPIO18 1"
        $led_on1
        led_on2="gpio -g write $GPIO17 0"
        $led_on2
}

pattern_2() {
	led_off1="gpio -g write $GPIO18 0"
        $led_off1
        led_off2="gpio -g write $GPIO17 1"
        $led_off2
}

set_gpio_mode $GPIO18
set_gpio_mode $GPIO17

while true;
do
	echo "Turn On"
	pattern_1
	sleep 2
	echo "Turn Off"
	pattern_2
	sleep 2
done

#EOF
