
# 1. Write a Python program to sum all the items in a list.
def sum_list_items(items):
    total = sum(items)
    return total
numbers = [1, 2, 3, 4, 5]
result = sum_list_items(numbers)
print(f"The sum of all the items in the list is: {result}")

# 2. Write a Python program to multiply all the items in a list.
def multiply_list_items(items):
    result = 1
    for item in items:
        result *= item
        
    return result

numbers = [1, 2, 3, 4]
result = multiply_list_items(numbers)
print(f"The product of all the items in the list is: {result}")

#3 Write a Python program to get the largest number from a list.

def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max

print(max_num_in_list([1, 2,17,9, 0]))


# 4. Write a Python program to get the smallest number from a list.
def find_smallest_number(numbers):
    return min(numbers)

numbers = [5, 1, 8, 3, 2]
result = find_smallest_number(numbers)
print(result)


#5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

string_list = ["abc", "xyz", "aba", "1221"]
result = count_special_strings(string_list)
print(result)


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def sort_tuples_by_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_tuples_by_last(tuple_list)
print(result)


# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

original_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(original_list)
print(result)


# 8. Write a Python program to check if a list is empty or not.

def check_if_empty(lst):
    return "The list is empty." if not lst else "The list is not empty."

non_empty_list = [1, 2, 3]
result = check_if_empty(non_empty_list)
print(result)


# 9. Write a Python program to clone or copy a list.

def clone_list(lst):
    return lst[:]

original_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(original_list)
print(f"Original List: {original_list}")
print(f"Cloned List: {cloned_list}")


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def find_longer_words(words, n):
    return [word for word in words if len(word) > n]
word_list = ["apple", "banana", "fig", "kiwi", "orange"]
n = 4
result = find_longer_words(word_list, n)
print(f"Words longer than {n} characters: {result}")


#11.Write a Python function that takes two lists and returns True if they have at least one common member.

def check_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]
result = check_common_member(list_a, list_b)
print(result)


# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors = [x for (i, x) in enumerate(colors) if i not in (0, 4, 5)]
print(colors)


# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

def createArray():
    array = [[[ '*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
    return array

array3d = createArray()
for layer in array3d:
    for row in layer:
        print(row)


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def remove(nums):
    return [num for num in nums if num % 2 != 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
filtered_numbers = remove(numbers)
print(filtered_numbers)


# 15. Write a Python program to shuffle and print a specified list.
import random

def shuffleList(lst):
    random.shuffle(lst)
    return lst

list = [0,1,2,3,6,8,11,94,22]

shuffledList = shuffleList(list)
print(shuffledList)


# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

def squares():
    s = [i**2 for i in range(1, 31) if i**2 <= 30]
    elements = s[:5] + s[-5:]
    return elements

print(squares())


# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_all_prime(numbers):
    for number in numbers:
        if not is_prime(number):
            return False
    return True

list_of_numbers =[0, 3, 4, 7, 9] 
result = check_all_prime(list_of_numbers)
print(result)


# 18. Write a Python program to generate all permutations of a list in Python.

import itertools

def list_permutations(lst):
    return list(itertools.permutations(lst))

my_list = [1, 2, 3]
permutations = list_permutations(my_list)
for perm in permutations:
    print(perm)


# 19. Write a Python program to calculate the difference between the two lists.

def list_difference(list1, list2):
    return list(set(list1) - set(list2))
list_a = [0, 1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8, 9]
print(list_difference(list_a, list_b))

# 20. Write a Python program to access the index of a list.

def print_list(lst):
    for index, element in enumerate(lst):
        print(f"Index: {index}, Element: {element}")

list = ['test1', 'test2', 'test3', 'test4']
print_list(list)

