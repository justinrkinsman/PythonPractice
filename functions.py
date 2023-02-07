def greet_user(name, last_name):
    print(f"Hi {name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", last_name="Smith") #keyword arguments should be used after positional arguments
print("Finish")

def square(number):
    return number * number #All functions return the value "None by default"

print(square(4))