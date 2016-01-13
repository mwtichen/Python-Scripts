# datechecker.py
# answer to exercise 7.14
# by Matthew Tichenor
# logical error when entering 02/29/2015

def numerize(string):
    if len(string) == 9:
        month = string[0]
        day = string[2:4]
        year = string[5:]
        month, day, year = int(month), int(day), int(year)
    elif len(string) == 10:
        month = string[0:2]
        day = string[3:5]
        year = string[6:]
        month, day, year = int(month), int(day), int(year)
    else:
        month, day, year = 0, 0, 0
    return month, day, year

def leap(year):
    if year % 4 == 0:
        if (year % 100 != 0) or (year % 400 == 0):
            x = 1
        else:
            x = 0
    else:
        x = 0
    return x

def monthcheck(month, year):
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        day = 31
    elif month == (4 or 6 or 9 or 11):
        day = 30
    else:
        num = leap(year)
        if num == 1:
            day = 29
        else:
            day = 28
    return day

def main():
    print('This program checks whether or not a date is valid.')
    string = input('Enter a date in the form mm/dd/yyyy: ')

    month, day1, year = numerize(string)
    day2 = monthcheck(month,year)
    if year == 0:
        print('You did not enter a date in the correct format.')
        print('Try again.')
    else:
        if 0 < day1 <= day2:
            print('That is a correct date.')
        else:
            print('That date is incorrect.')

main()
    
    
    
