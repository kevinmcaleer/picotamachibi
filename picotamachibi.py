# from icons import food_icon
from machine import I2C, Pin
from gui.ssd1306 import SSD1306_I2C
from icon import Animate, Icon, Toolbar, Button, Event
from time import sleep
import framebuf
import gc

sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)

print("creating oled")
oled = SSD1306_I2C(width=128, height=32, i2c=i2c)
print("Initialising display")
oled.init_display()

health = 1
happiness = 1
energy = 1

# load icons
food = Icon('food.pbm', width=16, height=16, name="food")
lightbulb = Icon('lightbulb.pbm', width=16, height=16, name="lightbulb")
game = Icon('game.pbm', width=16, height=16, name="game")
firstaid = Icon('firstaid.pbm', width=16, height=16, name="firstaid")
toilet = Icon('toilet.pbm', width=16, height=16, name="toilet")
heart = Icon('heart.pbm', width=16, height=16, name="heart")
call = Icon('call.pbm', width=16, height=16, name="call")

def clear():
    """ Clear the screen """
    oled.fill_rect(0,0,128,64,0)

# def animate(frames, timer):
#     for frame in frames:
#         oled.blit(frame.image, frame.x, frame.y)
#         oled.show()
#         sleep(0.1)

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
poopy = Animate(x=96,y=48, width=16, height=16, filename='poop')
baby = Animate(x=48,y=16, width=48, height=48, filename='baby_bounce', animation_type='bounce')
eat = Animate(x=48,y=16, width=48, height=48, filename='eat')
babyzzz = Animate(animation_type="loop", x=48,y=16, width=48, height=48, filename='baby_zzz')
death = Animate(animation_type='bounce', x=40,y=16, width=16, height=16, filename="skull")
go_potty = Animate(filename="potty", animation_type='bounce',x=64,y=16, width=48, height=48)
call_animate = Animate(filename='call_animate', width=16, height=16, x=108, y=0)
call_animate.speed = 'very slow'

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
heart_status = Event(name="Status", sprite=heart)
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
    if not cancel:
        tb.unselect(index, oled)
    if button_a.is_pressed:
        index += 1
        if index == 7:
            index = 0
        cancel = False
    if button_x.is_pressed:
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
            happiness += 1
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
            health += 1

            clear()
        if tb.selected_item == "heart":
            heart_status.message = "health = " + str(health)
            heart_status.popup(oled)
            heart_status.message = "happy = " + str(happiness)
            heart_status.popup(oled)
            heart_status.message = "energy = " + str(energy)
            heart_status.popup(oled)
            clear()
        if tb.selected_item == "call":
            # call_animate.animate(oled)
            call_animate.set = False
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
            energy += 1
            
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
    if (energy <= 1) and (happiness <= 1) and (health <=1):
        death.set = True
    else:
        death.set = False

    if (energy <= 1) or (happiness <= 1) or (health <= 1):
        # set the toolbar call icon to flash
        call_animate.set = True
    else:
        call_animate.set = False

    if poopy.set:
        poopy.load()
        poopy.animate(oled)
    if death.set:
        death.animate(oled)
    tb.show(oled)  
    if index == 6:
        tb.select(index, oled)
    else:
        if call_animate.set:
            call_animate.animate(oled)        
         
    oled.show()
    sleep(0.05)
    