""" Create a bank pin """


print('Codedex Bank')

pin = int(input('Enter your pin: '))

while pin != 1234:
    print('Invalid pin')
    pin = int(input('Enter your pin: '))

if pin == 1234: 
    print('Pin accepted')