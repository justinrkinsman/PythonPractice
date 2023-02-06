output = 0
total = []
index = 0
previous_number = 9999
suffix = 0

for symbol in string:
    total.append(symbols.get(symbol))
for digit in total:
    if digit > previous_number:
        suffix += (digit - previous_number)
    else:
        print(output)
        output += digit
        previous_number = digit
        print(output)
#total = 

#take string