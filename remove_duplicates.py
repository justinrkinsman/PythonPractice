numbers = [6, 6, 7, 5, 2, 8, 2, 9, 9]
current_number = 0

for number in numbers:
    current_number = number
    remaining_numbers = numbers.copy()
    remaining_numbers.remove(current_number)
    for number in remaining_numbers:
        if current_number == number:
            numbers.remove(number)
print(numbers)


#numbers.remove(5)
#print(numbers.index(5))
#print(50 in numbers)
#numbers2 = numbers.copy()