#answer to exercise 4.8
#by Matthew Tichenor

def main():
    print('This program creates an acronym for a given phrase.')
    acr = ''
    phrase = input('Enter a phrase: ')
    for ch in phrase.split(' '):
        acr = acr + ch[0].upper()

    print('Your acronym is',acr)

main()
