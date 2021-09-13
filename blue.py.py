# Write your code here :-)
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.3

print("Make it blue!")

while True:
    dot.fill((0, 0, 255))

