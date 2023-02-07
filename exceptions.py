try: #This code will run if the value is valid
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError: #If there is a ValueError, this code will run
    print("Invalid value")