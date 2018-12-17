max_kmph = int(input('Please enter a speed in kmph:'))
while max_kmph < 10 or max_kmph >= 500:
    print ('Error, please choose a reasonable speed! (10-500kmph)')
    max_kmph = int(input('Please enter a speed in kmph:'))
print ('')
print ('KMPH \t MPH')
for kmph in range (10, max_kmph+1, 10):
    mph = kmph * 0.6214
    print (kmph, '\t', format (mph, '.2f'))
print ('')
answer = input ('Input new value...Y/N?')
while answer == 'Y' or answer == 'y':
    max_kmph = int(input('Please enter a speed in kmph:'))
    while max_kmph < 10 or max_kmph >= 500:
        print ('Error, please choose a reasonable speed! (10-500kmph)')
        max_kmph = int(input('Please enter a speed in kmph:'))
    print ('')
    print ('KMPH \t MPH')
    for kmph in range (10, max_kmph+1, 10):
        mph = kmph * 0.6214
        print (kmph, '\t', format (mph, '.2f'))
    print ('')
    answer = input ('Input new value...Y/N?')
print ('')
print ('Thank you for using this program...BYE')
