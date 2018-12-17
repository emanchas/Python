print ('This program converts fahrenheit to celsius \n')

user_temp = int(input('Please input a temperature in Fahrenheit:'))
while user_temp < 0:
    print ('Error! Temperature must be greater than 0 degrees!')
    user_temp = int(input('Please input a temperature in Fahrenheit:'))
print ('')
print ('Fahrenheit \t Celsius')
for user_temp in range (0, user_temp+1, 5):
    Cel = (5/9) * user_temp - 17.8
    print (user_temp, '\t', '\t', format (Cel, '.2f'))
print ('')
answer = input ('Input new temperature...Y/N? \n')
while answer == 'Y' or answer == 'y':
    user_temp = int(input('Please input a temperature in Fahrenheit:'))
    while user_temp < 0:
        print ('Error! Temperature must be greater than 0 degrees!')
        user_temp = int(input('Please input a temperature in Fahrenheit:'))
    print ('')
    print ('Fahrenheit \t Celsius') 
    for user_temp in range (0, user_temp+1, 5):
        Cel = (5/9) * user_temp - 17.8
        print (user_temp, '\t', '\t', format (Cel, '.2f'))
    print ('')    
    answer = input ('Input new temperature...Y/N? \n')
print ('')
print ('Thank you for using this program ^_^')
