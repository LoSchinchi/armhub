import RPi.GPIO as GPIO
from time import sleep
import modules.servosModules as servo

try:
    servo.setMode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)
    s = GPIO.PWM(17, 50)
    s.start(0)
    s.ChangeDutyCycle(5)
    while True:
        pass
except KeyboardInterrupt:
    pass