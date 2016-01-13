# Easter.py
# answer to exercise 7.12
# by Matthew Tichenor

def calculate1(yr):
    a = yr % 19
    b = yr % 4
    c = yr % 7
    d = (19 * a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    day = 22 + d + e
    return(day)

def calculate2(yr):
    day = calculate1(yr) - 7
    return(day)

def calculate(yr):
    if yr == (1954 or 1981 or 2049 or 2076):
        day = calculate2(yr)
    else:
        day = calculate1(yr)
    return(day)

def main():
    print('This program calculates the date for Easter.')
    year = int(input('Enter any year from 1900 to 2099: '))

    day = calculate(year)
    if day > 31:
        print('Easter is on April %0d that year' % (day - 31))
    else:
        print('Easter is on March %0d that year' % (day))

main()
    
