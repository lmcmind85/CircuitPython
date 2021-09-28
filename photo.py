from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D8)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP


counter = 0
photo = False
state = False
speed = 4
start = time.time()

while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = speed - time.time()

    if remaining <= 0:
        print("The number of interrupts is:", str(counter))
        speed = time.time() + 4

