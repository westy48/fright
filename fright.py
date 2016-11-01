# Import Python libraries
import RPi.GPIO as GPIO
import time
import pygame

# Set the GPIO caming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO pins for button input and LED output
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.OUT)

pygame.mixer.init()
pygame.mixer.load("Laugh.wav")

while True:
    if(GPIO.input(3) ==0):
        GPIO.output(24, GPIO.HIGH)
        pygame.mixer.music.play()
        time.sleep (10)
        GPIO.output(24, GPIO.LOW)
        
GPIO.cleanup
