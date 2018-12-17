pay_rate = 15

keep_going = 'Y'

while keep_going == 'Y' or keep_going == 'y':
    hours = int(input ('Enter Working Hours: '))
    gross_pay = pay_rate * hours
    print ('Gross Pay for this week:  $', gross_pay, sep='')
    keep_going = input ('Keep going? (Y/N)')

print ("That's all")
