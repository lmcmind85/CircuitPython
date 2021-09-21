# Write your code here :-)
import time
import board
import pwmio
import servo
import hc-r04







sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1. echo_pin=board.A2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

simpleio.map_range(x, 5, 20, 0, 255)

