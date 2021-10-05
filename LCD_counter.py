import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio

# get and i2c object
i2c = board.I2C()

lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)


touchCounter1 = 0
touchCounter2 = 0
variable = 1
while True:
    lcd.set_cursor_pos(0, 0)
    lcd.print(str(touchCounter1))
    lcd.set_cursor_pos(1, 0)
    if touch_A1.value:
        print("Touch A1!")
        touchCounter1 = touchCounter1 + variable
    time.sleep(0.05)
    if touch_A2.value:
        print("Touch A2")
        variable = variable * -1

