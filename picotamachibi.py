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
book = Icon('book.pbm', width=16, height=16)

def load_baby():
    baby = Icon('baby.pbm', width=48, height=48, name="Baby")
    return baby

def load_baby_bounce():
    bounce_animation = []
    x = 48
    y = 16
    bounce_animation.append(Icon('baby_bounce04.pbm', width=48, height=48, x=x, y=y, name='frame01'))
    bounce_animation.append(Icon('baby_bounce01.pbm', width=48, height=48, x=x, y=y, name='frame01'))
    bounce_animation.append(Icon('baby_bounce02.pbm', width=48, height=48, x=x, y=y, name='frame02'))
    bounce_animation.append(Icon('baby_bounce03.pbm', width=48, height=48, x=x, y=y, name='frame03'))
    # bounce_animation.append(Icon('baby_bounce02.pbm', width=48, height=48, x=x, y=y, name='frame04'))
    # bounce_animation.append(Icon('baby_bounce01.pbm', width=48, height=48, x=x, y=y, name='frame05'))
    # bounce_animation.append(Icon('baby_bounce04.pbm', width=48, height=48, x=x, y=y, name='frame06'))
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
    # poop_animation.append(Icon('poop03.pbm', width=16, height=16, x=x, y=y, name="poop05"))
    # poop_animation.append(Icon('poop02.pbm', width=16, height=16, x=x, y=y, name="poop06"))
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

    # 
    # toolbar.additem(book)

    return toolbar

def poop_check():
    global poop
    poop = True
    print("poop check")

tb = build_toolbar()
# baby = load_baby()
bounce = load_baby_bounce()
poop_sprite = load_poop()
eat_food = load_eat()
sleepy_baby = load_sleep()
poopy = Animate(frames=poop_sprite, animation_type="default")
baby = Animate(frames=bounce, animation_type="default")
eat = Animate(frames=eat_food, animation_type="default")
babyzzz = Animate(frames=sleepy_baby, animation_type="loop")
poop = False

button_a = Button(4)
button_b = Button(3)
button_x = Button(2)

index = 0
tb.select(index, oled)
cancel = False
feeding_time = False

# Set up Events
energy_increase = Event(name="Increase Energy", sprite=heart, value=1)
firstaid = Event(name="First Aid", sprite=firstaid, value=0)
toilet = Event(name="Toilet", sprite=toilet, value=0)
poop_event = Event(name="poop time", sprite=poop_sprite, callback=poop_check())
poop_event.timer = 3
poop_event.timer_ms = 1

baby.bounce()
poopy.bounce()
babyzzz.speed = 'very slow'

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
        if tb.selected_item == "game":
            print("game")
        if tb.selected_item == "toilet":
            toilet.message = "Cleaning..."
            toilet.popup(oled=oled)
            poop = False
            clear()
        if tb.selected_item == "lightbulb":
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
    poop_event.tick()

    if feeding_time:
        if not eat.done:
            eat.animate(oled)
        if feeding_time and eat.done:
            feeding_time = False
            energy_increase.message = "ENERGY + 1"
            energy_increase.popup(oled=oled)
            # oled.blit(energy_increase.sprite.image, energy_increase.sprite.x, energy_increase.sprite.y)
            # oled.show()
            
            clear()
    else:
        # baby.animate(oled)
        babyzzz.animate(oled)
    if poop:
        poopy.animate(oled)
    tb.show(oled)    
    # poopy.animate(oled)
    oled.show()
    sleep(0.05)
    