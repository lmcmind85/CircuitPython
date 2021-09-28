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
