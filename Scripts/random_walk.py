# random_walk.py
# answer to exercise 9.16
# by Matthew Tichenor

import math
from random import random
from graphics import *

def main():
    intro()
    n = getn()
    win = walk(n)
    finish(win)

def intro():
    print('intro')

def getn():
    n = int(input('Enter the number of steps for the random walk: '))
    return n

def walk(n):
    win = background()
    point0 = initial(win)
    for i in range(1,n):
        point0 = plot(win,point0)
    return win

def background():
    window = GraphWin('Random Walk',400,400)
    window.setCoords(-7,-7,7,7)
    window.setBackground('white')
    return window

def initial(win):
    point0 = Point(0,0)
    point1 = points(point0)
    Line(point0,point1).draw(win)
    return point1
    
def plot(win,point0):
    point1 = points(point0)
    Line(point0,point1).draw(win)
    return point1

def points(point0):
    x = point0.getX()
    y = point0.getY()
    angle = random() * 2 * math.pi
    x = x + math.cos(angle)
    y = y + math.sin(angle)
    return Point(x,y)

def finish(win):
    Text(Point(0,4),'Click to end').draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__': main()
    
