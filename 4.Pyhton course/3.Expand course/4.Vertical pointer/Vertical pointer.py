from microbit import *
import microbit
import superbit

display.show(Image.HEART)

while True:
    x = accelerometer.get_x()
    x1 = ((x+1024)*(225-45)/2048)+45
    x1 = int(270 - x1)
    superbit.servo270(superbit.S1, x1)
    microbit.sleep(20)