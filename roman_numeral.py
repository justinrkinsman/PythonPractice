class Solution:
    def romanToInt(string):
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        output = 0
        array = []

        for symbol in string:
            array.append(symbols.get(symbol))
        
        while len(array) != 0:
            if len(array) == 1:
                output += array[0]
                array.remove(array[0])
            elif array[1] > array[0]:
                next_number = array[1]
                array.remove(array[1])
                array[0] = next_number - array[0]
                output += array[0]
                array.remove(array[0])
            else:
                output += array[0]
                array.remove(array[0])
        print(output)


Solution.romanToInt("MCMXCIV")