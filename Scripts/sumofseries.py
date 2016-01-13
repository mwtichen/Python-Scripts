#for exercise 3.18
#by Matthew Tichenor

def main():
    print("This programs computes the average of a series of numbers.")
    n = input("How many numbers do you want to average? ")
    x = input("Enter the numbers separated by a comma: ").split(",")
    n = int(n)
    count = 0
    for i in range(n):
        x[i] = float(x[i])
        count = count + x[i]

    avg = count/n
    print("The average is",count)

main()
