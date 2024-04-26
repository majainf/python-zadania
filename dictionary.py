# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

def sortByValue(d, ascending=True):
    sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse=not ascending)
    return dict(sorted_dict)

example = {'test1': 10, 'test2': 5, 'test3': 15, 'test4': 2}

print("Ascending:", sortByValue(example, ascending=True))
print("Descending:", sortByValue(example, ascending=False))


# 2. Write a Python script to add a key to a dictionary.

def addKey(d, key, value):
    d[key] = value
    return d
    
example = {'test1': 10, 'test2': 5, 'test3': 15}

newKey = 'test4'
newValue = 20
updatedList = addKey(example, newKey, newValue)
print("Updated Dictionary:", updatedList)


# 3. Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)

print(dic4) 


# 4. Write a Python script to check whether a given key already exists in a dictionary.

def keyExists(d, key):
    return key in d

example = {'test1': 10, 'test2': 5, 'test3': 15}

checkedKey = 'test2'
print(keyExists(example, checkedKey))

checkedKey = 'test4'
print(keyExists(example, checkedKey))


# 5. Write a Python program to iterate over dictionaries using for loops.

def iterate(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

example = {'test1': 10, 'test2': 5, 'test3': 15, 'test4': 20}

iterate(example)


# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Input a number "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x

print(d) 


#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

def createDict():
    dict = {i: i ** 2 for i in range(1, 16)}
    return dict

print(createDict())


# 8. Write a Python script to merge two Python dictionaries.

def mergeDict(dict1, dict2):
    mergedDict = dict1.copy()
    mergedDict.update(dict2)
    return mergedDict

dict1 = {'test1': 10, 'test2': 5}
dict2 = {'test3': 15, 'test4': 20}

print(mergeDict(dict1, dict2))


# 9. Write a Python program to iterate over dictionaries using for loops.

def iterateDict(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

example = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 20}

iterateDict(example)


# 10. Write a Python program to sum all the items in a dictionary.

def sumValues(d):
    total_sum = sum(d.values())
    return total_sum

example = {'test1': 10, 'test2': 5, 'test3': 15}

print(sumValues(example))


# 11. Write a Python program to multiply all the items in a dictionary.

def multiplyValues(d):
    result = 1
    for value in d.values():
        result *= value
        
    return result

example = {'test1': 5, 'test2': 15, 'test3': 3, 'test4': 4}

print(multiplyValues(example))


# 12. Write a Python program to remove a key from a dictionary.

def removeKey(d, key):
    if key in d:
        del d[key]
    return d

example = {'test1': 3, 'test2': 5, 'test3': 15, 'test4': 4}

print(removeKey(example.copy(), 'test3'))


# 13. Write a Python program to map two lists into a dictionary.

def map(k, v):
    return dict(zip(k, v))

keys = ['test1', 'test2', 'test3', 'test4']
values = [14, 5, 3, 20]

print(map(keys, values))


# 14. Write a Python program to sort a given dictionary by key.

def sort(d):
    return {key: d[key] for key in sorted(d)}

example = {'a_test1': 4, 'd_test2': 11, 'b_test3': 2, 'c_test4': 7}

print(sort(example))


# 15. Write a Python program to get the maximum and minimum values of a dictionary.

def findMaxMin(d):
    maxv = max(d.values())
    minv = min(d.values())
    return maxv, minv

example = {'test1': 10, 'test2': 43, 'test3': 5, 'test4': 21}

print(findMaxMin(example))


# 16. Write a Python program to get a dictionary from an object's fields.

class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'
    
    def do_nothing(self):
        pass

test = dictObj()

print(test.__dict__) 


# 17. Write a Python program to remove duplicates from the dictionary.

def removeDuplicates(d):
    uniqueValues = set()
    newDict = {}
    for key, value in d.items():
        if value not in uniqueValues:
            uniqueValues.add(value)
            newDict[key] = value
    return newDict

example = {'test1': 10, 'test2': 10, 'test3': 2, 'test3': 21, 'test4': 2}

print(removeDuplicates(example))


# 18. Write a Python program to check if a dictionary is empty or not.
def isEmpty(d):
    return not bool(d)

# Example dictionaries
empty = {}
notEmpty = {'apple': 10, 'banana': 5}

# Checking if dictionaries are empty
print("First dictionary: ",isEmpty(empty))
print("Second dictionary:",isEmpty(notEmpty))


# 19. Write a Python program to combine two dictionary by adding values for common keys.

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print(Counter(d1) + Counter(d2))


#20.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

def find_top_three_values(d):
    highest_three = sorted(d.items(), key=lambda item: item[1], reverse=True)[:3]
    return highest_three

example_dict = {'test1': 50, 'test2': 85, 'test3': 30, 'test4':65, 'test5': 80}

top_three_values = find_top_three_values(example_dict)

for key, value in top_three_values:
    print(f"{key}: {value}")

