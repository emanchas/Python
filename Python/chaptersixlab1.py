#Calculate Commission

def GetData(sale_amount):
    if sale_amount <=0:
        print ('Error: Please enter a positive sale amount!')
        GetData(float(input('Please enter the sale amount: ')))
    else:
        Commission = sale_amount * 0.05
        print ('Commission is:', sale_amount, '* 0.05 =', format (Commission, '.2f'))  
    


GetData(float(input('Please enter the sale amount: ')))

answer = input ('Calculate new value...Y/N? ')

while answer == 'Y' or answer == 'y':
    sale_amount = float(input('Please enter the sale amount: '))
    if sale_amount <=0:
        print ('Error: Please enter a positive sale amount!')
        GetData(float(input('Please enter the sale amount: ')))
    else:
        Commission = sale_amount * 0.05
        print ('Commission is:', sale_amount, '* 0.05 =', format (Commission, '.2f'))
        print ('')
        answer = input ('Calculate new value...Y/N? ')

print ('')
print ('Thank you for using this program.')
