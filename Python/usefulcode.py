Adding two numbers:

num1 = int(input(''))
num2 = int(input(''))
sum = num1 + num2
print (sum)

#########################################

Monthly cost calculator:

print ('Enter food cost:')
food_cost = int(input(''))
print ('Enter treats cost:')
treats_cost = int(input(''))
print ('Enter toys cost:')
toys_cost = int(input(''))
print ('Enter number of cats:')
numCats = int(input(''))
total_cost = (food_cost + treats_cost + toys_cost) * numCats
print ('Total cost equals: $', total_cost)

#########################################

Formatting:

userNum = int(input('Enter integer: \n'))
print ('You entered:', userNum)
userNumsquared = (userNum * userNum)
print (userNum, 'squared is', userNumsquared)
userNumcubed = (userNum * userNum * userNum)
print ('And', userNum, 'cubed is', userNumcubed,'!!')
userNum2 = int(input('Enter another integer: \n'))
sum = (userNum + userNum2)
print (userNum, '+', userNum2, 'is', sum)
print (userNum, '*', userNum2, 'is', userNum * userNum2)


#########################################

Test grade calculator/relations/indenting example:

test_score = int(input ('Enter your test score: '))

if test_score>=90 :
    print ('Your score is high.')
    print ('You will get grade A.')
    print ('Congratulations!')
    if test_score == 100 :
        print ('You got a perfect score!')
        print ('WOW!')
else:
    if test_score>=80 :
        print ('Your score is good.')
        print ('You will get a B.')
        print ('Good work.')
    else:        
        if test_score>=70 :
            print ('Your score is average.')
            print ('You will get a C.')
            print ('Try harder next time.')
        else:
            if test_score>=60 :
                print ('Your score is below average.')
                print ('You will get a D.')
                print ('Study harder please.')
    
#########################################

Combining else/if

if score <=0:
    print ('Invalid input!')
elif score >=90:
    print ('Grade is A')
elif score >=80:
    print ('Grade is B')
elif score >=70:
    print ('Grade is C')
elif score >=60:
    print ('Grade is D')
else:
    print ('Grade is F')


#########################################
Defining a _range_

user_grade = 10
if user_grade >=9 and user_grade <=12:
    print ('In High School')
else:
    print ('Not In High School')

#########################################

Checking odd/even numbers

user_num = 13
if user_num % 2 == 0:
    print ('Even')
else:
    print ('Odd')
    
                  
#########################################

Checking a _range_

num_cents = 109
if num_cents >=100:
    print ('Dollar or more')
else:
    print ('Not a dollar')

#########################################

Loopback conditions

pay_rate = 15

keep_going ='Y'

while keep_going == 'Y':
    hours = int(input('Enter working hours:  '))
    gross_pay = pay_rate * hours
    print ('Gross pay for this week:  $', gross_pay, sep='')
    keep_going = input ('Keep going? (Y/N)')

print ("That's all."

#########################################

special_list = [-99, 0, 44]
special_num = 17

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')

#########################################

Conditional Expressions

user_val = -9

cond_str = "negative" if (user_val < 0) else "non-negative"

print(user_val, 'is', cond_str)

#########################################


req_serv = input('Enter desired auto service: \n')
oc_cost = '$35'
tr_cost = '$19'
cw_cost = '$7'
print ('You entered:', req_serv)
print ('')
if req_serv == 'Oil change':
    print ('Cost of oil change:', oc_cost)
elif req_serv == 'Tire rotation':
    print ('Cost of tire rotation:', tr_cost)
elif req_serv == 'Car wash':
    print ('Cost of car wash:', cw_cost)
else:
    print ('Error: Requested service is not recognized.')

#########################################

num_insects = 8

while num_insects <= 100:
    print (num_insects, end=' ')
    num_insects = num_insects * 2

#########################################

Using a loop with a counter:

num_stars = 3
num_printed = 0

while num_printed != num_stars
       print ('*')
       num_printed = num_printed + 1

       
#########################################

How to print from a list:

stock_prices - [34.62, 76.30, 85.05]
for price in stock_prices:
       print ('$', price)

#########################################

Ranges:

Every integer from 0 to 500
range (501)
Every integer from 10 to 20
range (10, 21)
Every 2nd integer from 10 to 20
range (10, 21, 2)
Every integer from 5 down to -5
range (5, -6, -1)


#########################################

Printing from a list:

stock_prices = [34.62, 76.30, 85.05]
for price in stock_prices:
       print ('$', price)

#########################################

Printing from a dictionary:

contact_emails = {
    'Sue Ryan' : 's.reyn@email.com'
    'Mike Filt' : 'mike.filt@bmail.com'
    'Nate Arty' : 'narty042@nmail.com'
}

for (key, value) in contact_emails.items():
       print (value, 'is', key)

#########################################

import edit_distance

#A few legal, acceptable Danish names
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn', 
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne', 
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia', 
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne', 
    'Dorte'
]

user_name = input('Enter desired name:\n')

if user_name in legal_names:
    print('%s is an acceptable Danish name. Congratulations.' % user_name)
else:
    print('%s is not acceptable.' % user_name)
    for name in legal_names:
        if edit_distance.distance(name, user_name)  < 2:
            print('You might consider: %s,' % name, end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')

#########################################

import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')

#########################################


def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print ('Too small')
    elif bag_ounces > 10:
        print ('Too large')
    else: 
        print (6 * bag_ounces, 'seconds')

print_popcorn_time(7)


#########################################

def pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    pyramid_volume = (base_area * pyramid_height) * .33333
    return pyramid_volume

print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))

#########################################

def output_without_whitespace():
    string = input("Enter a sentence or phrase: ")
    string = string.replace(' ', '')
    print ('String with no whitespace:', string)

def get_num_chars():
    string = input("Enter a sentence or phrase: ")
    print ('You entered:', string)
    print('Number of characters:', len(string) - string.count(" "))
    print ()
    output_without_whitespace()


get_num_chars()

#########################################




