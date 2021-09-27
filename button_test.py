from machine import Pin

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    if button.value() == 0:
        print("0")
    if button.value() == 1:
        print("1")