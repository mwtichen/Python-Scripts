#answer to excerise 4.9
#by Matthew Tichenor

def main():
    print('This program calculates your numerology value.')
    name = input('Enter your name: ')
    name = name.lower()
    num = 0
    for string in name.split(' '):
        for ch in string:
            num = num + ord(ch) - 96

    print('Your numerology value is',str(num)+'.')

main()
