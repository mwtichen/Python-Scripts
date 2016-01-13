#Calculates molecular weight of a hydrocarbon
#by Matthew Tichenor

def main():
    print("This program calculates the molecular weight of a hydrocarbon")
    H = input("Enter the number of Hydrogen atoms: ")
    C = input("Enter the number of Carbon atoms: ")
    O = input("Enter the number of Oxygen atoms: ")
    H, C, O = float(H), float(C), float(O)
    weight = 1.0079 * H + 12.011 * C + 15.9994 * O
    print("The molecular weight is",weight,"grams per mole")

main()
