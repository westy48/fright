# Import Python libraries
from gpiozero import LED, PWMLED, Button
import pygame.mixer
from pygame.mixer import Sound
import time
from signal import pause

pygame.mixer.init()
santa = Sound("Laugh.wav")

# Set the GPIO pins
led = PWMLED(24)
button = Button(3)

while True:
    button.wait_for_press()
    led.pulse(n=5)
    santa.play()


