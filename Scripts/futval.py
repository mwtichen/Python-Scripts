# futval.py
# A program to compute the value of an investment
# carried 10 years into the future
# by: John M. Zelle

def main():
    print("This program calculates the future value of a 10-year investment.")
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate: ")
    yr = input("Enter the number of years: ")
    inflation = input("Enter the rate of inflation: ")
    principal, apr, yr, inflation = float(principal), float(apr), int(yr), float(inflation)
    for i in range(yr):
        principal = principal * (1 + apr)
        principal = principal/(1 + inflation)

    print("The real amount in",yr,"years is:", principal)

main()
