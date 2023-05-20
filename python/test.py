import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = None

getD = lambda a: a / 20 + 4.5

try:
    pwm=GPIO.PWM(17, 50)
    pwm.start(0)

    #for n in range(45, 181, 15):
    """for d in range(0, 13):
        pwm.ChangeDutyCycle(d) # left -90 deg position
        print(d)
        sleep(1)"""
    pwm.ChangeDutyCycle(6.5)
    sleep(2)
    pwm.ChangeDutyCycle(12)
    sleep(2)
    pwm.ChangeDutyCycle(4.5)
    sleep(2)
    while True: pass
    
    #pwm.stop()

    # da 4.5 a 12!!!!! va da 0  150

    while True: pass
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()


#da 7 a 12 con 50Hz