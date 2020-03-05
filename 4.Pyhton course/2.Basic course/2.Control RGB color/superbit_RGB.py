from microbit import *
import neopixel

Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Dark_Violet = (148, 0, 211)
White = (255, 255, 255)

color = (Red, Orange, Yellow, Green, Blue, Dark_Violet, White)

display.show(Image.HAPPY)

np = neopixel.NeoPixel(pin12, 4)
i = 0
while True:
    np.clear()
    np[0] = color[i]
    np[1] = color[i]
    np[2] = color[i]
    np[3] = color[i]
    np.show()
    sleep(1000)
    i = i+1
    if i > 6:
        i = 0

