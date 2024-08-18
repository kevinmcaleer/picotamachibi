# from icons import food_icon
from machine import I2C, Pin
from gui.ssd1306 import *
from icon import Animate, Icon, Toolbar, Button, Event, GameState
from time import sleep
import framebuf
from random import randint

sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)

oled = SSD1306_I2C(width=128, height=64, i2c=i2c)
oled.init_display()
print(f"oled: {oled}")

# load icons
food = Icon('food.pbm', width=16, height=16, name="food")
lightbulb = Icon('lightbulb.pbm', width=16, height=16, name="lightbulb")
game = Icon('game.pbm', width=16, height=16, name="game")
firstaid = Icon('firstaid.pbm', width=16, height=16, name="firstaid")
toilet = Icon('toilet.pbm', width=16, height=16, name="toilet")
heart = Icon('heart.pbm', width=16, height=16, name="heart")
call = Icon('call.pbm', width=16, height=16, name="call")

# Set Animations
poopy =    Animate(x=96, y=48, width=16, height=16, filename='poop')
baby =     Animate(x=48, y=16, width=48, height=48, animation_type="bounce", filename='baby_bounce')
eat =      Animate(x=48, y=16, width=48, height=48, filename='eat')
babyzzz =  Animate(x=48, y=16, width=48, height=48, animation_type="loop", filename='baby_zzz')
death =    Animate(x=48, y=16, animation_type='bounce', filename="skull")
go_potty = Animate(filename="potty", animation_type='bounce',x=64,y=16, width=48, height=48)

# Set the game state
gamestate = GameState()

# Append states to the states dictionary
gamestate.states["sleeping"] = False      # Baby is not sleeping
gamestate.states["feeding_time"] = False  # Baby is not eating
gamestate.states["cancel"] = False
gamestate.states["unwell"] = False
gamestate.states["health"] = 10
gamestate.states["happiness"] = 10
gamestate.states["sleepiness"] = 10
gamestate.states["tired"] = False

# Game Variables
TIREDNESS = 5 # seconds
POOP_MIN = 5 # seconds
POOP_MAX = 100 # seconds
SLEEP_DURATION = 5 # seconds


def tired():
    gamestate.states["sleepiness"] -= 1
    if gamestate.states["sleepiness"] < 0:
        gamestate.states["sleepiness"] = 0
    tiredness.start(TIREDNESS * 1000)
    
def wakeup():
    gamestate.states["sleepiness"] = 10
    gamestate.states["sleeping"] = False
    gamestate.states["happiness"] += 1
    gamestate.states["health"] += 1
    babyzzz.set = False
    baby.set = True
    print("Waking up")
    
def poop_check():
    if not gamestate.states["sleeping"]:
        go_potty.loop(no=1)
        baby.set = False
        go_potty.set = True
        print("poop time")
    
def clear():
    """ Clear the screen """
    oled.fill_rect(0,0,128,64,0)

def build_toolbar():
    print("building toolbar")
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

def do_toolbar_stuff():
    if tb.selected_item == "food":
        gamestate.states["feeding_time"] = True
        gamestate.states["sleeping"] = False
        baby.set = False
        babyzzz.set = False
        eat.set = True
            
    if tb.selected_item == "game":
        print("game")
        playtime.message = "He Hee"
        playtime.popup(oled)
        clear()
        gamestate.states["happiness"] += 10
    if tb.selected_item == "toilet":
        toilet.message = "Cleaning..."
        toilet.popup(oled)
        poopy.set = False
        baby.set = True
        clear()
        baby.animate(oled)
        poop_event.start(randint(POOP_MIN * 1000, POOP_MAX * 1000))
    if tb.selected_item == "lightbulb":
        # Sleeping
        if not gamestate.states["sleeping"]:
            gamestate.states["sleeping"] = True
            baby.set = False
            babyzzz.set = True
#             babyzzz.load()
            sleep_time.message = "Night Night"
            sleep_time.popup(oled)
            clear()
            sleep_time.start(SLEEP_DURATION * 1000) # sleep for 1 second

            # need to add an event that increases energy level after sleeping for 1 minute
        else:
            gamestate.states["sleeping"] = False
            babyzzz.set = False
            baby.set = True
            sleep_time.message = "Morning"
            sleep_time.popup(oled)
            clear()
        print("lightbulb")
    if tb.selected_item == "firstaid":
        firstaid.message = "Vitamins"
        firstaid.popup(oled)
        gamestate.states["health"] += 1
#         health += 1
        clear()
    if tb.selected_item == "heart":
#             print("heart")
        gamestate.states["happiness"] += 10

    if tb.selected_item == "call":
#             print("call")
        pass

def unhealthy_environment():
    gamestate.states["health"] -= 1
    gamestate.states["happiness"] -= 1
    print("Unhealthy Environment")
    if gamestate.states["health"] <= 0:
        gamestate.states["health"] = 0
        death.set = True
    if gamestate.states["happiness"] < 0:
        gamestate.states["happiness"] = 0
    gamestate.states["unwell"] = False 

def update_gamestate():

    print(gamestate)
    if gamestate.states["feeding_time"]:
        babyzzz.set = False
        baby.set = False
        eat.set = True
        eat.animate(oled)
        if not eat.done:
            eat.animate(oled)
        if gamestate.states["feeding_time"] and eat.done:
            gamestate.states["feeding_time"] = False
            energy_increase.message = "ENERGY + 1"
            energy_increase.popup(oled)
            gamestate.states["health"] += 10
            gamestate.states["happiness"] += 2
            
            clear()
#             eat.unload()
            eat.set = False
            baby.set = True
        
    if gamestate.states["sleeping"]:
#             babyzzz.load()
        babyzzz.set = True
        babyzzz.animate(oled)
            
    if go_potty.set:
#         baby.set = False
        go_potty.animate(oled)

    if go_potty.done:
        go_potty.set = False
        poopy.set = True
        baby.set = True
        
    if baby.set:
        baby.animate(oled)

    if poopy.set:
        poopy.animate(oled)
        # Check for the poop and if there is poop, decrease the health every 5 seconds
        if not gamestate.states["unwell"]:
            gamestate.states["unwell"] = True    
            decrease_health.start(5000)
        
    if death.set:
        death.animate(oled)
    
    if gamestate.states["health"] >= 1:
        death.set = False
    
    if gamestate.states["health"] == 0:
        death.set = True
    
    if not gamestate.states["tired"]:
        gamestate.states["tired"] = True
        tiredness.start(5000)
    if gamestate.states["sleepiness"] == 0:
        if not go_potty.set:
            baby.set = False
            babyzzz.set = True
            babyzzz.animate(oled)
tb = build_toolbar()

# Setup buttons
button_a = Button(2)
button_b = Button(3)
button_x = Button(4)

# Set toolbar index
index = 0

# Set the toolbar
tb.select(index, oled)

# Set up Events
energy_increase = Event(name="Increase Energy", sprite=heart, value=1)
firstaid = Event(name="First Aid", sprite=firstaid, value=0)
toilet = Event(name="Toilet", sprite=toilet, value=0)
poop_event = Event(name="poop time", sprite=toilet, callback=poop_check)
poop_event.start(randint(POOP_MIN * 1000, POOP_MAX * 1000))
sleep_time = Event(name="sleep time", sprite=lightbulb, value=1, callback=wakeup)
decrease_health = Event(name="decrease health", callback=unhealthy_environment)
tiredness = Event(name="tiredness", callback=tired)
playtime = Event(name="Game", sprite=game)
# poop_event.timer = 3
# poop_event.timer_ms = 1

baby.loop(no=-1)
poopy.bounce()
death.loop(no=-1)
death.speed='very slow'
babyzzz.speed = 'very slow'
# go_potty.loop(no=1)
# go_potty.set = True
poopy.set = False
# go_potty.load() # duplicate if go_potty.set is True

# death.set = True
baby.set = True

# Main Game Loop
while True:
    key = ' '
#     baby.animate(oled)

    if not gamestate.states["cancel"]:
        tb.unselect(index, oled)
        
    if button_a.is_pressed:
        index += 1
        if index == 7:
            index = 0
        gamestate.states["cancel"] = False
        
    if button_x.is_pressed:
        gamestate.states["cancel"] = True
        index = -1
    
    if not gamestate.states["cancel"]:
        tb.select(index, oled)

    if button_b.is_pressed:
        do_toolbar_stuff()
    
    tb.show(oled) 
    update_gamestate()   
    oled.show()
    sleep(0.05)
    