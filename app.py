#first_number = input('Enter your first number: ')
#second_number = input('Enter your second number: ')
#print('Sum: ' + str(float(first_number) + float(second_number)))

weight = input("Weight: ")
units = input("(K)g or (L)bs: ")

if units.upper() == "L":
    print("Weight in Kg: " + str(int(weight) / 2.205))
elif units.upper() == "K":
    print("Weight in Lbs: " + str(int(weight) * 2.205))