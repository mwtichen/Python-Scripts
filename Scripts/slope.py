#calculates the slope given two points
#by Matthew Tichenor
#for exercise 3.10

def main():
    print("This program calculates the slope given two points")
    x1, y1 = input("Enter the first pair of coordinates: ").split(",")
    x2, y2 = input("Enter the second pair of coordinates: ").split(",")
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    m = (y2 - y1)/(x2 - x1)
    print("The slope of the line is",m)

main()
    
