from microbit import *
import microbit
import superbit

display.show(Image.HEART)


while True:
    superbit.stepper_control(superbit.B1, 90)
    microbit.sleep(1000)
    superbit.stepper_control(superbit.B2, 90)
    microbit.sleep(1000)
    superbit.stepper_control(superbit.B1, 360)
    superbit.stepper_control(superbit.B2, 360)
    microbit.sleep(1000)
    microbit.sleep(1000)
