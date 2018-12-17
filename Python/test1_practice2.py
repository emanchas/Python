pay_rate = 25

keep_going = 'Y'

while keep_going == 'Y' or keep_going == 'y':
    hours = int(input('Enter working hours: '))
    while hours < 0:
        print ('Error! Hours should be a positive integer!')
        hours = int(input('Enter working hours: '))

    gross_pay = pay_rate * hours
    print ('Gross pay for this week: $', gross_pay, sep='')
    keep_going = input('Keep going? Y/N?')
print ('THATS ALL')
