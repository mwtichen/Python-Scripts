# bmi.py
# answer to exercise 7.7
# by Matthew Tichenor

def bmi(wt,ht):
    score = (720 * wt) / (ht ** 2)
    return score

def interpret(score):
    if 19 <= score <= 25:
        print('You got a BMI in the healthy range.')
    elif score < 19:
        print('Your BMI is below the healthy range.')
    else:
        print('Your BMI is above the healthy range.')

def main():
    print('This program calculates your body mass index (BMI).')
    weight = input('Enter your weight (in pounds): ')
    height = input('Enter your height (in inches): ')
    weight, height = float(weight), float(height)

    score = bmi(weight,height)
    interpret(score)
    print('Your BMI is %0.2f' % (score))

main()
    
