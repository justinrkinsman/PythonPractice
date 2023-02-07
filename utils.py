def find_max(list):
    numbers = list
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)

