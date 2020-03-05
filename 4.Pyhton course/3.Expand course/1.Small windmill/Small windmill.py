from microbit import *
import superbit

a = 135

display.show(Image.HEART)
superbit.servo270(superbit.S1, 135)
superbit.motor_control(superbit.M1, 255, 0)

while True:
    if button_a.is_pressed():
        a = a - 1
        if a < 0:
            a = 0
        superbit.servo270(superbit.S1, a)
    elif button_b.is_pressed():
        a = a + 1
        if a > 270:
            a = 270
        superbit.servo270(superbit.S1, a)
