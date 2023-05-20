import RPi.GPIO as GPIO
from time import sleep, time
import modules.servo as sv
import modules.I2C_LCD_driver as I2C_LCD_driver

KEY_WORD = 'motore'


def getDizMotore(string):
    string = string[len(KEY_WORD) + 1:]
    data = string.split(': ')
    return {KEY_WORD: data[0], 'degrees': data[1]}

def readFile(path):
    file = open('dati/' + path, 'r')
    lines = file.readlines()
    file.close()
    return [getDizMotore(l[:-1]) for l in lines]

def clearFile():
    open('dati/datiMotori.txt', 'w').close()

getDuty = lambda angle: angle / 9 - 8
    
pins = [17, 12, 19, 20, 21]
angle = 90

def main():
    nSec = time()
    servos = []
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        #GPIO.setup(pin, GPIO.OUT) 
        servos.append(sv.Init(pin)) # GPIO 17 for PWM with 50Hz
    lcd = I2C_LCD_driver.lcd()

    dataMotors = readFile('motors.txt')
    for servo, data in zip(servos, dataMotors):
        servo.run(int(data['degrees']))
    ind = 0
    #sleep(5)

    try:
        while True:
            for servo, data in zip(servos, dataMotors):
                print(data)
                servo.run(int(data['degrees']))  

            d = readFile('datiMotori.txt')
            if d == []:
                if time() > nSec + 2:
                    lcd.lcd_clear()
                    lcd.lcd_display_string('motore: ' + dataMotors[ind][KEY_WORD], 1, 0)
                    lcd.lcd_display_string('gradi: ' + dataMotors[ind]['degrees'], 2, 0)
                    ind = (ind + 1) % len(dataMotors)
                    nSec = time()
            else:
                d = d[0]
                __ind = int(d[KEY_WORD]) - 1
                dataMotors[__ind] = d
                servos[__ind].run(int(d['degrees']))
                clearFile()
                for _ in range(6):
                    lcd.lcd_display_string('motore: ' + d[KEY_WORD], 1, 0)
                    lcd.lcd_display_string('gradi: ' + d['degrees'], 2, 0)
                    sleep(0.35)
                    lcd.lcd_clear()
                    sleep(0.1)
        
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()

# d -> duty, g = grado
# 2d  = 90g
# 12d = 180g
# 7d = 135 g
#
# g = 9(d - 2) + 90
# 9(d - 2) = g - 90
# d - 2 = (g - 90) / 9
# d - 2 = g / 9 - 10
# d = g / 9 - 10 + 2
# d = g / 9 - 8