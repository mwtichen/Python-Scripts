#calculates the distance between two given points
#by Matthew Tichenor
#for exercise 3.11

import math

def main():
    print("This program calculates the distance between two points")
    x1, y1 = input("Enter the first pair of coordinates: ").split(",")
    x2, y2 = input("Enter the second pair of coordinates: ").split(",")
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("The distance between these points is",distance)

main()
    
