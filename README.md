# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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
Pictures / Gifs of your work should go here

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://www.markdownguide.org/basic-syntax/)

### Reflection
I had issues with the new process of uploading code to the board by saving it to the Python hard drive. After getting my pc to recognize my Python drive saving the code to the folder was easy. 


## CircuitPython_Servo

### Description & Code
After getting the Servo to mov

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

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
