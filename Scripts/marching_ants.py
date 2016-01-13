# marching_ants.py
# answer to exercise 6.7
# by Matthew Tichenor

def march(num):
    print('The ants go marching '+num+' by '+num+', hurrah! hurrah!')
    print('The ants go marching '+num+' by '+num+', hurrah! hurrah!')
    print('The ants go marching '+num+' by '+num+'.')

def chorus():
    print('And they all go marching down...')
    print('In the ground...')
    print('To get out...')
    print('Of the rain.')
    print('Boom! Boom! Boom!')

def one():
    return 'The little one stops to'

def main():
    march('one')
    print(one(),'suck his thumb')
    chorus()
    march('two')
    print(one(),'tie his shoe')
    chorus()
    march('three')
    print(one(),'brew some tea')
    chorus()
    march('four')
    print(one(),'join the war')
    chorus()
    march('five')
    print(one(),'joke and jive')
    chorus()
    march('six')
    print(one(),'pick up sticks')
    chorus()
    march('seven')
    print(one(),'gather up venom')
    chorus()
    march('eight')
    print(one(),'save a mate')
    chorus()
    march('nine')
    print(one(),'drink moonshine')
    chorus()
    march('ten')
    print(one(),'shoot the men')
    chorus()
    
main()
          
