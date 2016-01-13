# circle_graph.pyw
# answer to exercise 5.10
# by Matthew Tichenor

from graphics import *
import math

def main():
    print("This program calculates the intersection of a circle and\
 a horizontal line.")
    radius = input("Enter a radius (less than 10): ")
    y = input("Enter the y-intercept of the intersecting line: ")
    radius, y = float(radius), float(y)

    #Calculating the x values
    xl = -1 * math.sqrt(radius**2 - y**2)
    xr = math.sqrt(radius**2 - y**2)
    print("The circle intersects the line at x="+str(xl)+", "+str(xr)+".")

    #Creating the background
    win = GraphWin('',400,400)
    win.setBackground('white')
    win.setCoords(-12.0,-12.0,12.0,12.0)
    Line(Point(0.0,-12.0),Point(0.0,12.0)).draw(win)
    Line(Point(-12.0,0.0),Point(12.0,0.0)).draw(win)
    zero = Text(Point(1.25,-0.75),'(0,0)')
    zero.draw(win)

    #plotting the circle and line
    Circle(Point(0,0),radius).draw(win)
    Line(Point(-12.0,y),Point(12.0,y)).draw(win)

    #Points of intersection
    p1 = Point(xl,y)
    p2 = Point(xr,y)
    p1.setOutline('red')
    p2.setOutline('red')
    p1.draw(win)
    p2.draw(win)

main()
