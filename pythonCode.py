# import libaries
import pygame
from sys import exit
import serial  
import time

# set up serial communication
ser = serial.Serial("COM4", baudrate=9600, timeout=1)
print(ser) # my Ardunio is connected to serial port COM4, this will likely be different on your computer
time.sleep(3) # sleep to allow connection 


def getValues():  # function for getting value from serial port
    ser.write(b"g")  # sends 'g' to arduino via serial
    ardunioData = ser.readline().decode("ascii")  # reads serial port
    
    # print(ardunioData) # for debugging
    # print(type(ardunioData)) # for debugging
    return int(ardunioData)


def translate(value, leftMin, leftMax, rightMin, rightMax): # map function from 0 1023 to 0 255 
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(int(value) - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.

    return int(rightMin + (valueScaled * rightSpan))


def getColour(value): #create rgb value from force value
    redValue = translate(value, 0, 1023, 0, 255)
    greenValue = 255 - redValue
    colours = [redValue, greenValue, 0]
    return colours


pygame.init() #initialise pygame
width, height = 800, 800 # set window dimensions
screen = pygame.display.set_mode((width, height))  # create screen with dimensions
pygame.display.set_caption("Rectangle")  # set window title
clock = pygame.time.Clock()
rgb = [255, 0, 0]

test_surface = pygame.Surface((800, 800))  # create surface
test_surface.fill(rgb, rect=None, special_flags=0)

while True:
    for event in pygame.event.get(): # for quitting the programme
        if event.type == pygame.QUIT:  # exit game
            pygame.quit()
            ser.close() # close com port
            exit()  # quits all code

    rgb = getColour(getValues())  # get rgb value, using serial value
   
    test_surface.fill(rgb, rect=None, special_flags=0) # fill surface

    screen.blit(test_surface, (0, 0))  # display surface

    pygame.display.update()
    clock.tick(60)  # set max framerate
