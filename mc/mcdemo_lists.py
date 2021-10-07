'''Set up program for MC and two buttons
create a 'counter' variable that starts at 0
create a list of blockdata numbers for diffrent color wool
define a function called placeNext
    - it takes one argument called direction
    - it changes the counter by adding the direction argument
    - place a wool of the color from the list where
      the index matches the counter variable
    - if the counter is out of bounds of the index, reset it
in a forever loop:
    - if the first button was pressed, placeNext(1)
    - if the second button was pressed, placeNext(-1)'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import time

GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

counter = 0
woolColors = [6, 5, 10]

def placeNext(direction):
    global counter
    if counter >= 3:
        counter = 0
    counter += direction
    mc.setBlock(86, 13, -81, 35, woolColors[counter])
    
while True:
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
        print ("Button 6 has been pressed. ")
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)