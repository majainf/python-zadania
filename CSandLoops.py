# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

def numbers():
    result = []
    for num in range(1500, 2701): 
        if num % 7 == 0 and num % 5 == 0:
            result.append(num)
    return result

print(numbers())


# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

def celsiusToFahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    f = (c * 9/5) + 32
    return f

def fahrenheitToCelsius(f):
    """Convert Fahrenheit to Celsius."""
    c = (f - 32) * 5/9
    return c

celsius = 60
fahrenheit = celsiusToFahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit} in Fahrenheit")

fahrenheit = 45
celsius = fahrenheitToCelsius(fahrenheit)
print(f"{fahrenheit}°F is {int(celsius)} in Celsius")


# 4. Write a Python program to construct the following pattern, using a nested for loop.

def print_star_pattern():
    n = 5
    
    for i in range(1, n + 1):
        print('* ' * i)
    
    for i in range(n - 1, 0, -1):
        print('* ' * i)

print_star_pattern()


# 5. Write a Python program that accepts a word from the user and reverses it.

def reverse():
    word = input("Enter a word to reverse: ")
    
    reversed = word[::-1]
    
    print("Reversed word:", reversed)

reverse()


# 6. Write a Python program to count the number of even and odd numbers in a series of numbers

def count(n):
    evenCount = 0
    oddCount = 0
    
    for num in numbers:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
            
    return evenCount, oddCount

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

evenCount, oddCount = count(numbers)
print(f"Number of even numbers: {evenCount}")
print(f"Number of odd numbers: {oddCount}")


# 7. Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for item in datalist:
    print("Type of", item, "is", type(item)) 


# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

def printNumbers():
    for num in range(7):
        if num == 3 or num == 6:
            continue
        print(num)

printNumbers()


# 9. Write a Python program to get the Fibonacci series between 0 and 50.

def fibonacci(limit):
    a, b = 0, 1
    series = []
    
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    
    return series

limit = 50

print(fibonacci(limit))


# 10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

def fizzBuzz():
    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzBuzz()


# 11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

def generateArray(m, n):
    return [[i * j for j in range(n)] for i in range(m)]

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

array = generateArray(m, n)

for row in array:
    print(row)


# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

def collect_and_print_lines():
    lines = []
    print("Enter lines (leave blank to terminate):")

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nOutput:")
    for line in lines:
        print(line.lower())

collect_and_print_lines()


# 13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.

def filter():
    binaryNumbers = input("Enter comma-separated 4-digit binary numbers: ")
    binaryList = binaryNumbers.split(',')
    
    divisibleBy5 = [binNum for binNum in binaryList if int(binNum, 2) % 5 == 0]
    
    print("Output:", ','.join(divisibleBy5))

filter()


# 14. Write a Python program that accepts a string and calculates the number of digits and letters.

def count():
    userInput = input("Enter a string: ")
    
    digit = 0
    letter = 0
    
    for char in userInput:
        if char.isdigit():
            digit += 1
        elif char.isalpha():
            letter += 1
    
    print("Number of digits:", digit)
    print("Number of letters:", letter)

count()


# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

def findEvenNumbers():
    result = []  
    for number in range(100, 401):
        s = str(number)
        if all(int(char) % 2 == 0 for char in s):
            result.append(s)
    
    print(','.join(result))

findEvenNumbers()


# 17. Write a Python program to print the alphabet pattern 'A'.

def printLetter():
    pattern = [
        '  ***  ',  
        ' *   * ',  
        ' *   * ',  
        ' ***** ',  
        ' *   * ',  
        ' *   * '  
    ]
    for line in pattern:
        print(line)

printLetter()


# 18. Write a Python program to print the alphabet pattern 'D'.

def printLetter():
    pattern = [
        '****',                                                                  
        '*   * ',                                                                  
        '*   * ',                                                                
        '*   * ',                                                                 
        '*   * ' ,                                                               
        '*   * ',                                                               
        '****' 
    ]
    for line in pattern:
        print(line)

printLetter()


# 19. Write a Python program to print the alphabet pattern 'E'.

def printLetter():
    pattern = [
        '*****  ',                                                                 
        '*      ',                                                               
        '*      ',                                                                
        '****   ',                                                                
        '*      ',                                                                
        '*      ',                                                                
        '*****  ',
    ]

    for line in pattern:
        print(line)

printLetter()


# 20. Write a Python program to print the alphabet pattern 'L'.

def printLetter():
    pattern = [
        '*      ',
        '*      ',
        '*      ',
        '*      ',
        '*      ',
        '*      ',
        '****** '
    ]

    for line in pattern:
        print(line)

printLetter()
