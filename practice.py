first_name = "John"
last_name = "Smith"
message = f'{first_name} [{last_name}] is a code'
#print(message)

price = 1000000
good_credit = True

if good_credit:
    down_payment = price * 0.1
    #print(f"Down payment: ${down_payment}")
else:
    down_payment = price * 0.2
    #print(f"Down payment: ${down_payment}")

name = input('What is your name? ')
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good')