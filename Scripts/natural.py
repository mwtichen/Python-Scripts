#program for exercise 3.15
#by Matthew.Tichenor

def main():
    print("This program calculates the sum of n squared natural numbers")
    n = input("Enter a natural number: ")
    n = int(n)
    count = 0
    for i in range(n+1):
        count = count + i ** 2

    print("The sum of squares is",count)

main()
