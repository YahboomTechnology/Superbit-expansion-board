from microbit import *
import microbit
import superbit

display.show(Image.HEART)


while True:
    superbit.motor_control(superbit.M1, 255, 0)
    superbit.motor_control(superbit.M2, 255, 0)
    superbit.motor_control(superbit.M3, 255, 0)
    superbit.motor_control(superbit.M4, 255, 0)
    microbit.sleep(1000)

    superbit.motor_control(superbit.M1, 0, 0)
    superbit.motor_control(superbit.M2, 0, 0)
    superbit.motor_control(superbit.M3, 0, 0)
    superbit.motor_control(superbit.M4, 0, 0)
    microbit.sleep(1000)

    superbit.motor_control(superbit.M1, -255, 0)
    superbit.motor_control(superbit.M2, -255, 0)
    superbit.motor_control(superbit.M3, -255, 0)
    superbit.motor_control(superbit.M4, -255, 0)
    microbit.sleep(1000)
