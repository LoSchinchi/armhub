from gpiozero import Servo
from time import sleep

#servo = Servo(25)
val = -1

try:
    myGPIO=25

    myCorrection=0.45
    maxPW=(2.0+myCorrection)/1000
    minPW=(1.0-myCorrection)/1000

    servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

    while True:
        while val <= 1:
            servo.value=val
            print("0")
            sleep(1)
            val += 0.2
        val = -1
        """servo.value=0
        print("0")
        sleep(1)
        servo.value=0.6
        print("0")
        sleep(1)
        servo.value=1
        print("0")
        sleep(1)"""
except:
    pass

"""try:
	while True:
    	servo.min()
    	sleep(0.5)
    	servo.mid()
    	sleep(0.5)
    	servo.max()
    	sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")"""