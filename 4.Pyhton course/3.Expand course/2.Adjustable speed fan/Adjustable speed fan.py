from microbit import *
import music
import superbit
import neopixel

zero = Image("09990:90009:90009:90009:09990")
one = Image("00900:09900:00900:00900:09990")
two = Image("99900:00090:00900:90000:99990")
tree = Image("99990:00090:00900:90090:09900")
four = Image("00990:09090:90090:99999:00090")
five = Image("09999:09000:09990:00009:09990")


flag = 0
superbit.motor_control(superbit.M1, 0, 0)
np = neopixel.NeoPixel(pin12, 4)

def limit():
    global flag
    if flag > 5:
        flag = 5
    elif flag < 0:
        flag = 0

def change():
    global flag
    if button_a.is_pressed():
        music.play(music.POWER_UP)
        flag = flag + 1
    elif button_b.is_pressed():
        music.play(music.POWER_DOWN)
        flag = flag - 1

while True:
    change()
    limit()
    if flag == 0:
        display.show(zero)
        superbit.motor_control(superbit.M1, 0, 0)
        np.clear()
        np.show()
    elif flag == 1:
        display.show(one)
        superbit.motor_control(superbit.M1, 50, 0)
        np.clear()
        np[0] = (50, 0, 0)
        np[1] = (50, 0, 0)
        np[2] = (50, 0, 0)
        np[3] = (50, 0, 0)
        np.show()
    elif flag == 2:
        display.show(two)
        superbit.motor_control(superbit.M1, 100, 0)
        np.clear()
        np[0] = (100, 0, 0)
        np[1] = (100, 0, 0)
        np[2] = (100, 0, 0)
        np[3] = (100, 0, 0)
        np.show()
    elif flag == 3:
        display.show(tree)
        superbit.motor_control(superbit.M1, 150, 0)
        np.clear()
        np[0] = (150, 0, 0)
        np[1] = (150, 0, 0)
        np[2] = (150, 0, 0)
        np[3] = (150, 0, 0)
        np.show()
    elif flag == 4:
        display.show(four)
        superbit.motor_control(superbit.M1, 200, 0)
        np.clear()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        np[3] = (200, 0, 0)
        np.show()
    elif flag == 5:
        display.show(five)
        superbit.motor_control(superbit.M1, 255, 0)
        np.clear()
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        np.show()