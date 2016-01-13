#Answers 3.9
#by Matthew Tichenor

def main():
    print("Welcome to the Konditorei coffee shop.")
    lb = input("How many pounds of coffee would you like? ")
    lb = float(lb)
    price = lb * 10.50
    shipping = lb * 0.86 + 1.50
    total = price + shipping
    print("Your order will cost $",total)

main()
