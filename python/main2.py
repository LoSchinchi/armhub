try:
    from mainActions import *
    import traceback as TB
except:
    print('qqqqqqqqqqqqqqqqqqqqqqqqq')
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
                        #lcd.lcd_clear()
                        #showStringsLCD(dataMotors[ind])
                        #ind = (ind + 1) % len(dataMotors)
                        #nSec = time()
                else:
                    print('qui')
                    d = d[0]
                    #print('xx', d, d[0])
                    __ind = int(d[KEY_WORD]) - 1
                    dataMotors[__ind] = d
                    print('arriviato')
                    angle(__ind + 1, int(d['degrees']))
                    clearFile('datiMotori.txt')
                    #toggleLCD(d)

                fc = open('dati/isRunning.txt', 'r')
                t = fc.readline()
                fc.close()
            
        except KeyboardInterrupt:
            shutdown()
    except BaseException as e:
        print('yy', e)
        TB.print_exc()
        print('qqqqqqqqqqqqqqqqqqqqqqqqq')
        shutdown()

if __name__ == '__main__':
    main()
    shutdown()

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
