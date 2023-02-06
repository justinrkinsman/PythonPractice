numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(5)
#numbers.clear()
numbers.pop()
print(numbers.index(5))
print(50 in numbers) #Won't cause error if number is not in numbers
numbers.sort()
print(numbers)