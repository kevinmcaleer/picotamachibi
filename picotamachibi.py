# from icons import food_icon
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from icon import Animate, Icon, Toolbar, Button, Event
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

# load icons
food = Icon('food.pbm', width=16, height=16, name="food")
lightbulb = Icon('lightbulb.pbm', width=16, height=16, name="lightbulb")
game = Icon('game.pbm', width=16, height=16, name="game")
firstaid = Icon('firstaid.pbm', width=16, height=16, name="firstaid")
toilet = Icon('toilet.pbm', width=16, height=16, name="toilet")
heart = Icon('heart.pbm', width=16, height=16, name="heart")
call = Icon('call.pbm', width=16, height=16, name="call")

def load_baby_bounce():
    bounce_animation = []
    x = 48
    y = 16
    bounce_animation.append(Icon('baby_bounce04.pbm', width=48, height=48, x=x, y=y, name='frame01'))
    bounce_animation.append(Icon('baby_bounce01.pbm', width=48, height=48, x=x, y=y, name='frame01'))
    bounce_animation.append(Icon('baby_bounce02.pbm', width=48, height=48, x=x, y=y, name='frame02'))
    bounce_animation.append(Icon('baby_bounce03.pbm', width=48, height=48, x=x, y=y, name='frame03'))
    return bounce_animation

def load_poop():
    poop_animation = []
    x = 96
    y = 48
    poop_animation.append(Icon('poop01.pbm', width=16, height=16, x=x, y=y, name="poop01"))
    poop_animation.append(Icon('poop02.pbm', width=16, height=16, x=x, y=y, name="poop02"))
    poop_animation.append(Icon('poop03.pbm', width=16, height=16, x=x, y=y, name="poop03"))
    poop_animation.append(Icon('poop04.pbm', width=16, height=16, x=x, y=y, name="poop04"))
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

def load_sleep():
    sleep_animation = []
    x = 48
    y = 16
    w = 48
    h = 48
    sleep_animation.append(Icon('baby_zzz01.pbm', width=w, height=h, x=x, y=y, name="baby_zzz01"))
    sleep_animation.append(Icon('baby_zzz02.pbm', width=w, height=h, x=x, y=y, name="baby_zzz02"))
    sleep_animation.append(Icon('baby_zzz03.pbm', width=w, height=h, x=x, y=y, name="baby_zzz03"))
    sleep_animation.append(Icon('baby_zzz04.pbm', width=w, height=h, x=x, y=y, name="baby_zzz04"))
    # sleep_animation.append(Icon('baby_zzz05.pbm', width=w, height=h, x=x, y=y, name="baby_zzz05"))
    return sleep_animation

def load_skull():
    skull_animation = []
    x = 40
    y = 16
    w = 16
    h = 16
    # skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull01"))
    # skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull02"))
    # skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull03"))
    # skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull04"))
    skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull05"))
    skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull06"))
    skull_animation.append(Icon('skull02.pbm', width=w, height=h, x=x, y=y, name="skull01"))
    skull_animation.append(Icon('skull01.pbm', width=w, height=h, x=x, y=y, name="skull01"))
    return skull_animation

def load_go_potty():
    potty_animation = []
    x = 64
    y = 16
    potty_animation.append(Icon('potty01.pbm', width=48, height=48, x=x, y=y, name="potty01"))
    potty_animation.append(Icon('potty02.pbm', width=48, height=48, x=x, y=y, name="potty02"))
    potty_animation.append(Icon('potty03.pbm', width=48, height=48, x=x, y=y, name="potty03"))
    potty_animation.append(Icon('potty04.pbm', width=48, height=48, x=x, y=y, name="potty04"))
    potty_animation.append(Icon('potty05.pbm', width=48, height=48, x=x, y=y, name="potty05"))
    potty_animation.append(Icon('potty06.pbm', width=48, height=48, x=x, y=y, name="potty06"))
    potty_animation.append(Icon('potty07.pbm', width=48, height=48, x=x, y=y, name="potty07"))
    potty_animation.append(Icon('potty08.pbm', width=48, height=48, x=x, y=y, name="potty08"))
    potty_animation.append(Icon('potty09.pbm', width=48, height=48, x=x, y=y, name="potty09"))
    potty_animation.append(Icon('potty10.pbm', width=48, height=48, x=x, y=y, name="potty10"))
    potty_animation.append(Icon('potty11.pbm', width=48, height=48, x=x, y=y, name="potty11"))
    potty_animation.append(Icon('potty12.pbm', width=48, height=48, x=x, y=y, name="potty12"))
    potty_animation.append(Icon('potty13.pbm', width=48, height=48, x=x, y=y, name="potty13"))
    potty_animation.append(Icon('potty14.pbm', width=48, height=48, x=x, y=y, name="potty14"))
    return potty_animation

def clear():
    """ Clear the screen """
    oled.fill_rect(0,0,128,64,0)

def animate(frames, timer):
    for frame in frames:
        oled.blit(frame.image, frame.x, frame.y)
        oled.show()
        sleep(0.1)

def build_toolbar():
    toolbar = Toolbar()
    toolbar.spacer = 2
    toolbar.additem(food)    
    toolbar.additem(lightbulb)
    toolbar.additem(game)
    toolbar.additem(firstaid)
    toolbar.additem(toilet)
    toolbar.additem(heart)
    toolbar.additem(call)
    return toolbar

tb = build_toolbar()
# bounce = load_baby_bounce()
# poop_sprite = load_poop()
# eat_food = load_eat()
# sleepy_baby = load_sleep()
# skull = load_skull()
# potty = load_go_potty()
poopy = Animate(x=96,y=48, width=16, height=16, filename='poop')
baby = Animate(x=48,y=16, width=48, height=48, filename='baby_bounce', animation_type='bounce')
eat = Animate(x=48,y=16, width=48, height=48, filename='eat')
babyzzz = Animate(animation_type="loop", x=48,y=16, width=48, height=48, filename='baby_zzz')
death = Animate(animation_type='bounce', x=40,y=16, width=16, height=16, filename="skull")
go_potty = Animate(filename="potty", animation_type='bounce',x=64,y=16, width=48, height=48)

button_a = Button(4)
button_b = Button(3)
button_x = Button(2)

index = 0
tb.select(index, oled)
cancel = False
feeding_time = False
sleeping = False
death.set = True

# Set up Events
energy_increase = Event(name="Increase Energy", sprite=heart, value=1)
firstaid = Event(name="First Aid", sprite=firstaid, value=0)
toilet = Event(name="Toilet", sprite=toilet, value=0)
# poop_event = Event(name="poop time", sprite=poop_sprite, callback=poop_check())
sleep_time = Event(name="sleep time", sprite=lightbulb, value=1)
# poop_event.timer = 3
# poop_event.timer_ms = 1

baby.bounce()
poopy.bounce()
death.loop(no=-1)
death.speed='slow'
babyzzz.speed = 'very slow'
go_potty.loop(no=1)
go_potty.set = True
poopy.set = False
go_potty.load()

while True:
    # key = input("v & b to move selection")
    key = ' '
    if not cancel:
        tb.unselect(index, oled)
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
            feeding_time = True
            sleeping = False
            baby.unload()
            
        if tb.selected_item == "game":
            print("game")
        if tb.selected_item == "toilet":
            toilet.message = "Cleaning..."
            toilet.popup(oled=oled)
            poopy.set = False
            baby.set = True
            clear()
            poopy.unload()
        if tb.selected_item == "lightbulb":
            if not sleeping:
                sleeping = True
                babyzzz.load()
                sleep_time.message = "Night Night"
                sleep_time.popup(oled)
                clear()
                # need to add an event that increases energy level after sleeping for 1 minute
            else:
                sleeping = False
                babyzzz.unload()
            print("lightbulb")
        if tb.selected_item == "firstaid":
            firstaid.message = "Vitamins"
            firstaid.popup(oled=oled)

            clear()
        if tb.selected_item == "heart":
            print("heart")
        if tb.selected_item == "call":
            print("call")

    # Time for Poop?
    # poop_check()
    # poop_event.tick()

    if feeding_time:
        eat.load()
        if not eat.done:
            eat.animate(oled)
        if feeding_time and eat.done:
            feeding_time = False
            energy_increase.message = "ENERGY + 1"
            energy_increase.popup(oled=oled)
            
            clear()
            eat.unload()
            baby.load()
    else:
        if sleeping:
            babyzzz.animate(oled)
        else:
            if baby.set:
                baby.load()
                baby.animate(oled)
            if go_potty.set:
                go_potty.animate(oled)
            if go_potty.done:
                print("potty done")
                go_potty.set = False
                poopy.set = True
                baby.load()
                baby.bounce(no=-1)
                baby.set = True

    if poopy.set:
        poopy.load()
        poopy.animate(oled)
    if death.set:
        death.animate(oled)
    tb.show(oled)    
    oled.show()
    sleep(0.05)
    