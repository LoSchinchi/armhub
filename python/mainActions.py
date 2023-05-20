import RPi.GPIO as GPIO
#from modules.I2C_LCD_driver import lcd as LCD
from time import *

GPIO.setmode(GPIO.BCM)
PINS = [17, 27, 22] #, 17, 13, 18]
KEY_WORD = 'motore'
BASE = 1
BRACCIO = 2
AVBRACCIO = 3
PINZA = 4

getDuty = lambda angle: angle / 20 + 4.5

def clearFile(name):
    open('dati/' + name, 'w').close()

def getDizMotore(string):
    string = string[len(KEY_WORD) + 1:]
    data = string.split(': ')
    return {KEY_WORD: data[0], 'degrees': data[1]}

def readFile(path):
    file = open('dati/' + path, 'r')
    lines = file.readlines()
    file.close()
    return [getDizMotore(l[:-1]) for l in lines]

def setTempFile(dizs):
    fw = open('dati/tempMotori.txt', 'w')
    for diz in dizs:
        fw.write(f"{KEY_WORD} {diz[KEY_WORD]}: {diz['degrees']}\n")
    fw.close()

def setMotorFromTempFile():
    data = readFile('tempMotori.txt')
    if data == []:
        return
    for servo, d, e in zip(servos, data, range(len(PINS))):
        servo.ChangeDutyCycle(getDuty(int(d['degrees'])))
        sleep(1)

#servos = [None] * 4
#lcd = None

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
servos = []
for pin in PINS:
    t = GPIO.PWM(pin, 50)
    t.start(0)
    servos.append(t)
print(servos)
servos[0].ChangeDutyCycle(0)
setMotorFromTempFile()

def shutdown():
    for s in servos:
        s.stop()
    GPIO.cleanup()

#lcd = LCD()

def resetMotors():
    data = readFile('motors.txt')
    for servo, d, e in zip(servos, data, range(4)):
        if e == 1:
            servo.start(0)
        servo.ChangeDutyCycle(getDuty(int(d['degrees'])))
        if e == 1:
            servo.stop()
        sleep(.7)
    clearFile('tempMotori.txt')

def showStringsLCD(d):
    pass
    #lcd.lcd_display_string('motore: ' + d[KEY_WORD], 1, 0)
    #lcd.lcd_display_string('gradi: ' + d['degrees'], 2, 0)

def toggleLCD(d):
    for _ in range(6):
        showStringsLCD(d)
        sleep(0.35)
        #lcd.lcd_clear()
        sleep(0.35)

def angle(nMot, degrees):
    servos[nMot - 1].ChangeDutyCycle(getDuty(degrees))
    print('dentro')
    sleep(1)

def reset():
    for i, data in enumerate(readFile('motors.txt')):
        angle(i + 1, int(data['degrees']))

def save():
    pass

def show(s1, s2=None):
    pass
    if s2 is not None:
        pass

def stop():
    for s in servos:
        s.stop()

def start():
    for s in servos:
        s.start(0)