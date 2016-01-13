#answer to exercise 4.18
#File wordcount.py
#by Matthew Tichenor
#need to fix number of words

import math

def main():
    print("This program calculates the number of words, characters \
and lines in a file")
    fileName = input("Enter a file (full file extension): ")
    infile = open(fileName, 'r')
    c1 = 0
    c2 = 0
    c3 = 0
    for line in infile.readlines():
        c1 = c1 + 1
        sentence = line[:-1]
        for string in sentence.split(' '):
            a = math.ceil(len(string)/(len(string)+1))
            c2 = c2 + 1 * a
            for ch in string:
                c3 = c3 + 1


    print('There are',c1,'lines,',c2,'words and',c3,'characters.')

main()
            
    
    
          
