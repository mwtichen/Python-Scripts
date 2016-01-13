# archery_graph.pyw
# answer to exercise 5.5

from graphics import *

def main():
    win = GraphWin()
    center = Point(100,100)
    bull = Circle(center,5)
    bull.setFill("yellow")
    bull.draw(win)
    red = Circle(center,25)
    red.setOutline("red")
    red.setWidth(5)
    red.draw(win)
    blue = Circle(center,50)
    blue.setOutline("blue")
    blue.setWidth(5)
    blue.draw(win)
    black = Circle(center,75)
    black.setWidth(5)
    black.draw(win)
    white = Circle(center,100)
    white.setOutline("white")
    white.setWidth(5)
    white.draw(win)
    Text(center,'HIT ME!').draw(win)
    win.getMouse()
    win.close()

main()
    
