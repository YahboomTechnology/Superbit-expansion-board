from microbit import *
import superbit

display.show(Image.HEART)
superbit.servo270(superbit.S1, 0)
sleep(1000)
while True:
    if button_a.is_pressed():
        superbit.servo270(superbit.S5, 60)
    elif button_b.is_pressed():
        superbit.servo270(superbit.S5, 0)