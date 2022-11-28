from turtle import *
import time
import random

def star(size):
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
        forward(size)
        left(72)
    end_fill()

colormode(255)
speed(0)
for j in range(100,0,-2):
    fillcolor(int(j*2.4),int(j*1.9),0)
    star(j)
    right(36)
time.sleep(1)
