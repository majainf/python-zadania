
# 1. Write a Python program to calculate the length of a string.
string = input("Enter a string: ")
length = len(string)
print("The length of the entered string is: ",length)

# 2.Write a Python program to count the number of characters (character frequency) in a string.
def character_frequency():
    string = input("Enter a string: ")
    
    freq = {}
    
    for char in user_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    for char, count in freq.items():
        print(f"Character: {char} -> Frequency: {count}")

character_frequency()

#3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

print(change_char('restart'))  

# 4.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b

print(chars_mix_up('abc', 'xyz')) 

# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def add_string(str1):
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    return str1

print(add_string('ab'))      
print(add_string('abc'))  
print(add_string('string')) 

# 6. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1

print(not_poor('The lyrics is not that poor!')) 
print(not_poor('The lyrics is poor!'))    

# 7. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()

    return word_len[-1][0], word_len[-1][1]

result = find_longest_word(["PHP", "Exercises", "Backend"])

print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])

# 8 Write a Python program to remove the nth index character from a nonempty string.
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n+1:]

    return first_part + last_part

print(remove_char('Python', 0))  
print(remove_char('Python', 3)) 
print(remove_char('Python', 5))  

# 9 Write a Python program to remove the nth index character from a nonempty string.
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n+1:]

    return first_part + last_part

print(remove_char('test12345', 0))  
print(remove_char('test12345', 3)) 
print(remove_char('test12345', 5))  

# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]

print(change_string('abcde'))  
print(change_string('12345'))  

# 11. Write a Python program to remove characters that have odd index values in a given string.
def odd_values_string(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    
    return result

print(odd_values_string('abcdef'))  
print(odd_values_string('python'))  

#12. Write a Python program to count the occurrences of each word in a given sentence.

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

user_input = input("What's your favorite language? ")
print("My favorite language is ", user_input.upper())
print("My favorite language is ", user_input.lower()) 

#14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
items = input("Input comma-separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#15. Write a Python function to create an HTML string with tags around the word(s).
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

#16. Write a Python function to insert a string in the middle of a string.
def insert_string_middle(str, word):
    return str[:2] + word + str[2:]

print(insert_string_middle('[[]]', 'Python')) 
print(insert_string_middle('{{}}', 'PHP'))    
print(insert_string_middle('<<>>', 'HTML')) 

#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

def make_new_string(s):
    if len(s) < 2:
        return "Error: The string must be at least 2 characters long."
    last_two = s[-2:]
    return last_two * 4

result = make_new_string("Python")
print(result) 

#18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.

def first_three_chars(s):
    if len(s) >= 3:
        return s[:3]
    else:
        return s

result = first_three_chars("Python")
print(result) 

# 20. Write a Python function to reverse a string if its length is a multiple of 4.

def reverse_string(str1):
    if len(str1) % 4 == 0:
        return ''.join(reversed(str1))
    
    return str1
print(reverse_string('abcd')) 
print(reverse_string('python')) 

