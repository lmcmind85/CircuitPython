"""CircuitPython Essentials Servo standard servo example"""
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
