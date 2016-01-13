#answer to exercise 4.12
#by Matthew Tichenor

def main():
    print("This program illustrates the Caesar Cipher")
    phrase = input("Enter a phrase to be encoded/decoded: ")
    key = int(input("Enter a key: "))
    out = ''
    for string in phrase.split(' '):
        for ch in string:
            a = (65+(ord(ch)//97)*32)
            x = chr((ord(ch)+key-a)%26+a)
            out = out + x

        out = out + ' '

    print("Your encoded phrase is:",out[:-1])

main()
