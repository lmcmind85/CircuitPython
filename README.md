# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [UltraSonic Sensor](#UltraSonic_Sensor)
---

## Hello_CircuitPython

### Description & Code

The goal is to make the LED on the board shine blue.

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it blue!")

while True:
    dot.fill((0, 0, 255))
```


### Evidence

### Wiring

### Reflection
I had issues with the new process of uploading code to the board by saving it to the Python hard drive. After getting my pc to recognize my Python drive saving the code to the folder was easy. 


## CircuitPython_Servo

### Description & Code
After getting the Servo to move, our goal is to use compacitive touch to make the servo turn to the left or the right.

```python
Code goes here
import time
import board
import pwmio
import servo
import touchio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)


while True:
    if touch_A1.value:
        print("Touch A1!")
        my_servo.angle = 90
    if touch_A2.value:
        print("Touch A2")
        my_servo.angle = 0
        time.sleep(0.05)
```

### Evidence and Wiring
<img src="https://github.com/lmcmind85/CircuitPython/blob/main/Images/IMG_2772.JPG?raw=true" width="400">

### Reflection




## CircuitPython_LCD

### Description & Code

The goal is to make a counter on the LCD sceen begin counting when a wire is touched. Touching another wire should reverse the counter.

```python
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

```

### Evidence
<img src="https://github.com/lmcmind85/CircuitPython/blob/main/Images/LCDImage.JPG?raw=true" width="400">

<img src="https://github.com/lmcmind85/CircuitPython/blob/main/Images/LCDVid.gif?raw=true" width="400">


### Reflection





## UltraSonic_Sensor

### Description & Code

The goal is to make the LCD color change in relation to the distance from the sensor.

```python
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)
blueValue = 0
redValue = 0
greenValue = 0

while True:
    try:
        cm = sonar.distance
        cm = sonar.distance
        print((cm,))
        if cm < 5:
            dot.fill((0, 0, 0))
        elif cm < 20:
            redValue = simpleio.map_range(cm, 5, 20, 255, 0)
            greenValue = 0
            blueValue = simpleio.map_range(cm, 5, 20, 0, 255)
            print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
            dot.fill((int(redValue), int(greenValue), int(blueValue)))
        elif cm < 35:
            redValue = 0
            greenValue = simpleio.map_range(cm, 20, 35, 0, 255)
            blueValue = simpleio.map_range(cm, 20, 35, 255, 0)
            print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
            dot.fill((int(redValue), int(greenValue), int(blueValue)))
        else:
            dot.fill((0, 0, 0))
        time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")
```

### Evidence

<img src="https://github.com/lmcmind85/CircuitPython/blob/main/Images/UltraSonic_IMG_2951.JPG?raw=true" width="400">

![AltText](https://github.com/lmcmind85/CircuitPython/blob/main/Images/UltraSonicVID.gif?raw=true)
### Reflection


## Photo_Interrupter 

### Description & Code

The goal is to have the serial monitor state the amount of times the sensor was interruped over a 4 second interval. 

```python
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D8)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter2 = 0
counter = 0
photo = False
state = False
speed = 4
start = time.time()

while True:
    photo = interrupter.value
    if photo and not state:
        counter += 1
        counter2 += 1
    state = photo

    remaining = speed - time.time()

    if remaining <= 0:
        print("Interrupted :", str(counter), "more times")
        print("The number of total interrupts is:", str(counter2))
        speed = time.time() + 4
        counter = 0

```

### Evidence

<img src="https://github.com/lmcmind85/CircuitPython/blob/main/Images/PhotoVid.gif?raw=true" width="400">

### Reflection

