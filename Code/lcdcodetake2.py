##original code credits go to Graham GS
## view linked code https://github.com/VeganPorkChop/CircutPython/blob/master/LCD.py 

import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object!!
i2c = board.I2C()
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
buttonPress = 0

while True:
    if btn2 == True:
        lcd.print("BTN is down")
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(1, 0)
                lcd.print("BTN Press:")
                lcd.print(str(buttonPress))
        prev_state = cur_state
    else:
        lcd.set_cursor_pos(0, 0)
        lcd.print("BTN is up")