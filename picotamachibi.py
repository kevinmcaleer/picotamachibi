# from icons import food_icon
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from icon import Icon, Toolbar
from time import sleep

sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)

# food = food_icon
# print(food)
oled = SSD1306_I2C(width=128, height=64, i2c=i2c)
oled.init_display()
# oled.text("test", 1, 1)
# oled.show()
# sleep(1)

def build_toolbar():

    toolbar = Toolbar()
    toolbar.spacer = 1
    
    food = Icon('food.pbm', width=16, height=16, name="food")
    toolbar.additem(food)

    lightbulb = Icon('lightbulb.pbm', width=16, height=16, name="lightbulb")
    toolbar.additem(lightbulb)

    game = Icon('game.pbm', width=16, height=16, name="game")
    toolbar.additem(game)

    oled.blit(toolbar.data, 0,0)
    
    # game = Icon('game.pbm', width=16, height=16)
    # game.x = spacer + (16 * 2) + spacer
    # firstaid = Icon('firstaid.pbm', width=16, height=16)
    # firstaid.x = spacer + (16 * 3) + spacer
    # toilet = Icon('toilet.pbm', width=16, height=16)
    # toilet.x = (16 * 4) + spacer
    # heart = Icon('heart.pbm', width=16, height=16)
    # heart.x = (16 * 5) + spacer
    # book = Icon('book.pbm', width=16, height=16)
    # book.x = (16 * 6) + spacer
    # call = Icon('call.pbm', width=16, height=16)
    # call.x = (16 * 7) + spacer

    # oled.blit(food.image, food.x, food.y) # 48 is the lower row
    # oled.blit(lightbulb.image, lightbulb.x, lightbulb.y)
    # oled.blit(toilet.image, toilet.x, toilet.y)
    # oled.blit(heart.image, heart.x, heart.y)
    # oled.blit(book.image, book.x, book.y)
    # oled.blit(call.image, call.x, call.y)
    # oled.blit(firstaid.image, firstaid.x, firstaid.y)
    # oled.blit(game.image, game.x, game.y)

build_toolbar()
oled.show()