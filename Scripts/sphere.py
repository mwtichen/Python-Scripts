#Calculates the surface area and volume for a sphere
#Matthew Tichenor

import math

def main():
    print("This program calculates the surface area and volume of a sphere")
    radius = input("Enter a radius: ")
    radius = float(radius)
    volume = 4 / 3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2
    print("The volume is",volume)
    print("The surface are is",area)

main()
