# timeandahalf.py
# answer to exercise 7.3

def pay(hr,rt):
    sal = hr * rt
    return sal

def half(hr,rt):
    ex = (hr - 40) * rt
    return ex

def main():
    print('This program calculates your weekly salary.')
    hours = input('Enter the number of hours worked: ')
    rate = input('Enter the hourly rate: ')
    hours, rate = float(hours), float(rate)

    salary = pay(hours,rate)
    if hours > 40:
        salary = salary + half(hours,rate)

    print('Your salary is $%0.2f.' % (salary))

main()
        
