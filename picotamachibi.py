# from icons import food_icon
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from icon import Animate, Icon, Toolbar, Button
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

def load_baby():
    baby = Icon('baby.pbm', width=48, height=48, name="Baby")
    return baby

def load_baby_bounce():
    bounce_animation = []
    x = 48
    y = 16
    bounce_animation.append(Icon('baby_bounce01.pbm', width=48, height=48, x=x, y=y, name='frame01'))
    bounce_animation.append(Icon('baby_bounce02.pbm', width=48, height=48, x=x, y=y, name='frame02'))
    bounce_animation.append(Icon('baby_bounce03.pbm', width=48, height=48, x=x, y=y, name='frame03'))
    bounce_animation.append(Icon('baby_bounce02.pbm', width=48, height=48, x=x, y=y, name='frame04'))
    bounce_animation.append(Icon('baby_bounce01.pbm', width=48, height=48, x=x, y=y, name='frame05'))
    bounce_animation.append(Icon('baby_bounce04.pbm', width=48, height=48, x=x, y=y, name='frame06'))
    # bounce_animation.append(Icon('baby_bounce01.pbm', width=48, height=48, name='frame07'))
    return bounce_animation

def load_poop():
    poop_animation = []
    x = 96
    y = 48
    poop_animation.append(Icon('poop01.pbm', width=16, height=16, x=x, y=y, name="poop01"))
    poop_animation.append(Icon('poop02.pbm', width=16, height=16, x=x, y=y, name="poop02"))
    poop_animation.append(Icon('poop03.pbm', width=16, height=16, x=x, y=y, name="poop03"))
    poop_animation.append(Icon('poop04.pbm', width=16, height=16, x=x, y=y, name="poop04"))
    poop_animation.append(Icon('poop03.pbm', width=16, height=16, x=x, y=y, name="poop05"))
    poop_animation.append(Icon('poop02.pbm', width=16, height=16, x=x, y=y, name="poop06"))
    return poop_animation

def load_eat():
    eat_animation = []
    x = 48
    y = 16
    eat_animation.append(Icon('eat01.pbm', width=48, height=48, x=x, y=y, name="eat01"))
    eat_animation.append(Icon('eat02.pbm', width=48, height=48, x=x, y=y, name="eat02"))
    eat_animation.append(Icon('eat03.pbm', width=48, height=48, x=x, y=y, name="eat03"))
    eat_animation.append(Icon('eat04.pbm', width=48, height=48, x=x, y=y, name="eat04"))
    eat_animation.append(Icon('eat05.pbm', width=48, height=48, x=x, y=y, name="eat05"))
    eat_animation.append(Icon('eat06.pbm', width=48, height=48, x=x, y=y, name="eat06"))
    eat_animation.append(Icon('eat07.pbm', width=48, height=48, x=x, y=y, name="eat07"))

    return eat_animation

def animate(frames, timer):
    for frame in frames:
        oled.blit(frame.image, frame.x, frame.y)
        oled.show()
        sleep(0.1)

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
# baby = load_baby()
bounce = load_baby_bounce()
poop = load_poop()
eat_food = load_eat()
poopy = Animate(frames=poop)
baby = Animate(frames=bounce)
eat = Animate(frames=eat_food)

button_a = Button(4)
button_b = Button(3)
button_x = Button(2)

index = 0
tb.select(index, oled)
cancel = False
feeding_time = False
while True:
    # key = input("v & b to move selection")
    key = ' '
    if not cancel:
        tb.unselect(index, oled)
    # if key == "v":
    #     index -= 1
    #     if index <0:
    #         index = 6
        
        # cancel = False
    if button_a.is_pressed:
        index += 1
        if index == 7:
            index = 0
        cancel = False
    if button_x.is_pressed:
        # tb.unselect(index, oled)
        cancel = True
        index = -1
    
    if not cancel:
        tb.select(index, oled)

    if button_b.is_pressed:
        if tb.selected_item == "food":
            print("food")
            feeding_time = True
        if tb.selected_item == "game":
            print("game")
        if tb.selected_item == "toilet":
            print("toilet")
        if tb.selected_item == "lightbulb":
            print("lightbulb")
        if tb.selected_item == "firstaid":
            print("firstaid")
        if tb.selected_item == "heart":
            print("heart")
        if tb.selected_item == "call":
            print("call")

    if feeding_time and (not eat.done):
        eat.animate(oled)
        # sleep(1)
    elif feeding_time and eat.done:
        feeding_time = False
    else:
        baby.animate(oled)
    tb.show(oled)    
    poopy.animate(oled)
    # oled.blit(baby.image, 0, 16)
    oled.show()
    sleep(0.05)
    

