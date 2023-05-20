try:
    from mainActions import *
    import traceback as TB
except:
    shutdown()

def main():
    try:
        nSec = time()
        dataMotors = readFile('motors.txt')
        setTempFile(dataMotors)
        ind = 0

        reset()
        
        try:
            fc = open('dati/isRunning.txt')
            t = fc.readline()
            fc.close()
            while t != '':
                d = readFile('datiMotori.txt')
                if d == []:
                    if time() > nSec + 2:
                        pass
                        lcd.lcd_clear()
                        showStringsLCD(dataMotors[ind])
                        ind = (ind + 1) % len(dataMotors)
                        nSec = time()
                else:
                    d = d[0]
                    #print('xx', d, d[0])
                    __ind = int(d[KEY_WORD]) - 1
                    dataMotors[__ind] = d
                    angle(__ind + 1, int(d['degrees']))
                    clearFile('datiMotori.txt')
                    toggleLCD(d)

                fc = open('dati/isRunning.txt', 'r')
                t = fc.readline()
                fc.close()
            
        except KeyboardInterrupt:
            shutdown()
    except BaseException as e:
        TB.print_exc()
        shutdown()

if __name__ == '__main__':
    main()
    shutdown()