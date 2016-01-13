# graph_art.pyw
# answer to exercise 5.8
# by Matthew Tichenor

from graphics import *

def main():
    win = GraphWin('',500,500)
    win.setCoords(0.0, 0.0, 90.0, 90.0)

    # Creating the background
    win.setBackground('white')
    front = Rectangle(Point(0.0,0.0),Point(100.0,15.0))
    front.setFill('brown')
    front.draw(win)

    # Making die shapes
    for i in range(5):
        x = 5.0 + 16 * i
        Rectangle(Point(x,15.0),Point(x+15.0,30.0)).draw(win)
        
    # Making dots on dice
    # Consider making this a loop
    dot1 = Circle(Point(12.5,22.5),1)
    dot1.setFill('black')
    dot1.draw(win)
    dot21 = dot1.clone()
    dot21.move(12.5,3.5)
    dot21.draw(win)
    dot22 = dot1.clone()
    dot22.move(19.5,-3.5)
    dot22.draw(win)
    dot31 = dot1.clone()
    dot31.move(28.5,3.5)
    dot31.draw(win)
    dot32 = dot1.clone()
    dot32.move(32,0)
    dot32.draw(win)
    dot33 = dot1.clone()
    dot33.move(35.5,-3.5)
    dot33.draw(win)
    dot41 = dot1.clone()
    dot41.move(44.5,3.5)
    dot41.draw(win)
    dot42 = dot1.clone()
    dot42.move(44.5,-3.5)
    dot42.draw(win)
    dot43 = dot1.clone()
    dot43.move(51.5,3.5)
    dot43.draw(win)
    dot44 = dot1.clone()
    dot44.move(51.5,-3.5)
    dot44.draw(win)
    dot51 = dot1.clone()
    dot51.move(60.5,3.5)
    dot51.draw(win)
    dot52 = dot1.clone()
    dot52.move(60.5,-3.5)
    dot52.draw(win)
    dot53 = dot1.clone()
    dot53.move(64,0)
    dot53.draw(win)
    dot54 = dot1.clone()
    dot54.move(67.5,3.5)
    dot54.draw(win)
    dot55 = dot1.clone()
    dot55.move(67.5,-3.5)
    dot55.draw(win)
    
    
    
    Text(Point(45,70),'Roll the dice!').draw(win)
    win.getMouse()
    win.close()

main()
