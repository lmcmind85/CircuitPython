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


