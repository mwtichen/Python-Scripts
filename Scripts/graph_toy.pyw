# answer to exericse 5.3
# note that you must add main() otherwise this does nothing
# graph_toy.pyw

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(25,25), Point(75,75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        xl = p.getX() - 25
        yl = p.getY() - 25
        xu = p.getX() + 25
        yu = p.getY() + 25
        p1, p2 = Point(xl,yl), Point(xu,yu)
        square = Rectangle(p1,p2)
        square.setOutline("red")
        square.setFill("red")
        square.draw(win)
    Text(Point(100,100),'Click to exit').draw(win)
    win.getMouse()
    win.close()

main()
