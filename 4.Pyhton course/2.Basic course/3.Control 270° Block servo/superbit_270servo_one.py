from microbit import *
import microbit
import superbit

display.show(Image.HEART)
superbit.servo270(superbit.S1, 0)
microbit.sleep(1000)

while True:
    superbit.servo270(superbit.S1, 0)
    microbit.sleep(1000)
    superbit.servo270(superbit.S1, 90)
    microbit.sleep(1000)
    superbit.servo270(superbit.S1, 180)
    microbit.sleep(1000)
    superbit.servo270(superbit.S1, 270)
    microbit.sleep(1000)
    superbit.servo270(superbit.S1, 180)
    microbit.sleep(1000)
    superbit.servo270(superbit.S1, 90)
    microbit.sleep(1000)


