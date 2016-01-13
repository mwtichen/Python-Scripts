# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Suzie Programmer

def main():
    print("This program has been modified for exercise 2.8")
    fahrenheit = input("What is the Fahrenheit temperature? ")
    fahrenheit = float(fahrenheit)
    celsius = 5/9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius.")

main()
