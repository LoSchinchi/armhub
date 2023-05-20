import os
from modules.I2C_LCD_driver import lcd as LCD

PORT = 3000

lcd = LCD()

def main():
    os.system('hostname -I | cat > dati/ip.txt')
    f = open('dati/ip.txt')
    ip = f.readline()[:-1]
    f.close()
    lcd.lcd_display_string(ip, 1, 0)
    lcd.lcd_display_string(':' + str(PORT), 2, 0)


if __name__ == '__main__':
    main()