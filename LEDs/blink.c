#include <stdio.h>
#include <wiringPi.h>

int main(void)
{
	printf("Raspberry Pi Blink\n");

	if (wiringPiSetup() == -1)
		return 1;

	pinMode(0, OUTPUT); /* aka BCM_GPIO pin 17 */
	pinMode(1, OUTPUT); /* aka BCM_GPIO pin 18 */

	for (;;) {
		digitalWrite(0, 1);	//On
		digitalWrite(1, 0);
		delay(100);		// mS
		digitalWrite(0, 0);	// off
		digitalWrite(1, 1);
		delay(100);
	}

	return 0;
}

