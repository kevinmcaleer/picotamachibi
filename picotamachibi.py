# from icons import food_icon
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from icon import Icon, Toolbar
from time import sleep
import framebuf

sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)

oled = SSD1306_I2C(width=128, height=64, i2c=i2c)
oled.init_display()

health = 1
happiness = 1
sleepiness = 1

def load_baby(oled):
    baby = Icon('baby.pbm', width=48, height=48, name="Baby")
    oled.blit(baby.image, 10, 16)
    oled.show()
    return oled

def build_toolbar():
    toolbar = Toolbar()
    toolbar.spacer = 2
    
    food = Icon('food.pbm', width=16, height=16, name="food")
    toolbar.additem(food)

    lightbulb = Icon('lightbulb.pbm', width=16, height=16, name="lightbulb")
    toolbar.additem(lightbulb)

    game = Icon('game.pbm', width=16, height=16, name="game")
    toolbar.additem(game)

    firstaid = Icon('firstaid.pbm', width=16, height=16, name="firstaid")
    toolbar.additem(firstaid)

    toilet = Icon('toilet.pbm', width=16, height=16, name="toilet")
    toolbar.additem(toilet)

    heart = Icon('heart.pbm', width=16, height=16, name="heart")
    toolbar.additem(heart)

    call = Icon('call.pbm', width=16, height=16, name="call")
    toolbar.additem(call)

    # book = Icon('book.pbm', width=16, height=16)
    # toolbar.additem(book)

    return toolbar

tb = build_toolbar()
tb.show(oled)
# tb.select(, oled)
# tb.show(oled)
oled = load_baby(oled)
oled.show()

index = 0
tb.select(index, oled)
cancel = False
while True:
    key = input("v & b to move selection")
    if not cancel:
        tb.unselect(index, oled)
    if key == "v":
        index -= 1
        if index <0:
            index = 6
        
        cancel = False
    if key == "b":
        index += 1
        if index == 7:
            index = 0
        cancel = False
    if key == "m":
        # tb.unselect(index, oled)
        cancel = True
        index = -1
    
    if not cancel:
        tb.select(index, oled)
    tb.show(oled)
