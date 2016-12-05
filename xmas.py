# Import Python libraries
from gpiozero import LED, PWMLED, Button
import pygame.mixer
from pygame.mixer import Sound
import time
from signal import pause
import random
import os

pygame.mixer.init()
randomfile = ""
file = ""

# Set the GPIO pins
led = PWMLED(24)
button = Button(3)

while True:
    button.wait_for_press()
    time.sleep(0.25)
    led.pulse(n=10)
    randomfile = random.sample(os.listdir("/home/pi/fright/music/"), 1)[0]
    print randomfile
    file = '/home/pi/fright/music/'+ randomfile
    santa = Sound(file)
    print file
    pygame.mixer.music.set_volume(0.5)
    santa.play()
