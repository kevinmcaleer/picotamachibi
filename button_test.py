from machine import Pin
from time import sleep

button_a = Pin(2, Pin.IN, Pin.PULL_UP)
button_b = Pin(3, Pin.IN, Pin.PULL_UP)
button_x = Pin(4, Pin.IN, Pin.PULL_UP)

count = 0

while True:
#     print(f"Button Status, A: {button_a.value()}, B: {button_b.value()}, X: {button_x.value()}, {count}")
    if button_a.value() == 0:
        print("button A pressed")
    if button_b.value() == 0:
        print("button B pressed")
    if button_x.value() == 0:
        print("button X pressed")
    sleep(0.25)
    count += 1