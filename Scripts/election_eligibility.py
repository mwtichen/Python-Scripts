# election_eligibility.py
# answer to exercise 7.10
# by Matthew Tichenor

def eligibility(age,res):
    if age >= 30 and res >= 9:
        str1 = 'are'
    else:
        str1 = 'are NOT'
    if age >= 25 and res >= 7:
        str2 = 'are'
    else:
        str2 = 'are NOT'
    return str1, str2

def main():
    print('This program determines whether or not you can run for legislative office.')
    age = input('Enter your age: ')
    residency = input("Enter the number of years you've been a citizen: ")
    age, residency = int(age), int(residency)

    string1, string2 = eligibility(age,residency)
    print('You',string1,'eligible for the senate.')
    print('You',string2,'eligible for congress.')

main()
    
