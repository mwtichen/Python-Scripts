# lettergrade
# answer to exercise 7.5
# by Matthew Tichenor

def lettergrade(score):
    if 90 <= score <= 100:
        letter = 'A'
    elif 80 <= score < 90:
        letter = 'B'
    elif 70 <= score < 80:
        letter = 'C'
    elif 60 <= score < 70:
        letter = 'D'
    elif 0 <= score < 60:
        letter = 'F'
    else:
        letter = ''
    return(letter)

def out(score,letter):
    if 0 <= score <= 100:
        print('You got an',letter+'!')
    else:
        print('An exam score must be between 0 and 100.')
        print('Try again.')

def main():
    print('This program calculates the letter grade for your exam.')
    score = input('Enter your exam score: ')
    score = float(score)

    letter = lettergrade(score)
    out(score,letter)
    
main()
    
    
