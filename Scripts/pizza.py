#Calculates the price per square inch of a pizza
#by Matthew Tichenor

import math

def main():
    print("This program calculates the price per square inch of a pizza")
    diameter = input("Enter the diameter of the pizza: ")
    price = input("Enter the price of the pizza: ")
    diameter, price = float(diameter), float(price)
    radius = diameter / 2.
    area = 4 * math.pi * radius ** 2
    ppsq = price / area
    print("The price per square inch is",ppsq,"dollars per square inches")

main()
