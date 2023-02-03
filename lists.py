# My solution
#numbers = [1, 2, 3, 6, 5, 4, 3, 7]
#previous_number = 0
#largest_number = 0
#for number in numbers:
    #if previous_number < number:
        #largest_number = number
    #previous_number = number
#print(largest_number)

# Mosh's solution
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

