#answer to exercise 4.7
#by Matthew Tichenor

def main():
    print("This program will calculate the letter grade for your exam.")
    grade = float(input("Please Enter your exam grade: "))
    index = int(grade // 10)
    scale = 'FFFFFFDCBAA'
    print(scale[index],'is your letter grade.')

main()
    
