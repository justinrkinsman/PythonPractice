# my solution
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


# Mosh's solution
mosh_numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in mosh_numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)