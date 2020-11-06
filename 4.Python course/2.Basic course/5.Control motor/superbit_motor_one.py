from microbit import *
import microbit
import superbit

display.show(Image.HEART)

while True:
    superbit.motor_control(superbit.M1, 255, 0)
    microbit.sleep(1000)

    superbit.motor_control(superbit.M1, 0, 0)
    microbit.sleep(1000)

    superbit.motor_control(superbit.M1, -255, 0)
    microbit.sleep(1000)

