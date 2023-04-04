import time

options = ('Mon' , 'Tue' , 'Wed' , 'Thur' , 'Fri')

while True
print()
print('*OPTIONS*')
print('Mon = Monday')
print('Tue = Tuesday')
print('Wed = Wednesday')
print('Thur = Thursday')
print ('Fri = Friday')

print()
user_input = input('Enter an option:')

if user_input in options:
    break
    
    else:
        print()
        print('OPTION NOT AVAILABLE')
        