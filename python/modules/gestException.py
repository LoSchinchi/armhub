import traceback as TB

def onExcept(info: tuple, lcd):
    TB.print_exc()
    (type_, obj, tb) = info

    print(type_.__name__, obj, tb.tb_lineno - 14)

    fHimself = open('python/run.py', 'r')
    line = fHimself.readlines()[tb.tb_lineno - 1]
    line = ''.join(line.split('\t')).strip()
    fHimself.close()

    fw = open('dati/editorException.txt', 'w')
    fw.write('Traceback (most recent call last):\n')
    fw.write(f"{'  ' * 2}Editor, line {tb.tb_lineno - 14}\n")
    fw.write(f"{'  ' * 4}{line}\n")
    fw.write(f'{type_.__name__}: {obj}')
    fw.close()

    lcd.lcd_clear()
    if type_.__name__.index('Error') != -1:
        lcd.lcd_display_string('Error', 1, 0)
    elif type_.__name__.index('Exception') != -1:
        lcd.lcd_display_string('Exception', 1, 0)
    else:
        lcd.lcd_display_string('Warning', 1, 0)
    lcd.lcd_display_string(type_.__name__, 1, 0)
    l = len(f'line {tb.tb_lineno - 14}')
    lcd.lcd_display_string(f'line {tb.tb_lineno - 14}', 2, 16 - l)