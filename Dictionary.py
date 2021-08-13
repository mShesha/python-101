# Dictionary is a collection of unordered, mutable and indexed elements.
# It is defined using key and value pairs

# Create a dictionary

firstDict = dict()
secondDict = {}

print(firstDict)
print(secondDict)

engToSp = {"one": "uno", "two": "dos", "three": "tres"}
print(engToSp)

# Accessing elements of dictionary. By using keys

print(engToSp['one'])

# accessing is O(1)

# how are dictionaries stored in Python
# Dictionaries are indexed by keys and can be seen as associative arrays.
# Python dictionaries are implemented using hash tables. It is an array whose index is obtained by hash functions over the keys

# update/add new key value pairs to the dictionary
# time complexity - O(1) space complexity - O(1) -- for updating

myDict = {'name': 'Megha', 'age': 30, 'education': 'masters'}
print(myDict)
myDict['age'] = 31
print(myDict)

# add new element to the existing dictionary
# time complexity - O(1) space complexity - amortized O(1) -- for adding

myDict['address'] = 'Bangalore'
print(myDict)


# traverse over a dictionary - O(n)

def traverseDict(dictionary):
    for key in dictionary:
        print(str(key) + " : " + str(dictionary[key]))


traverseDict(myDict)


# search values in a dictionary using linear search

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "value doesn't exist"


print(searchDict(myDict, 31))

# delete an element from dictionary
# pop method

print(myDict.pop('age'))
print(myDict)

print(myDict.popitem())
print(myDict)

print("here")
del myDict['name']
print(myDict)

del myDict  # deletes the entire dictionary

myDict = {'name': 'Megha', 'age': 30}

# myDict.clear() # clears all key value pairs in the dictionary. doesn't delete the dictionary itself
# a print statement after clear doesn't throw an error
# print(myDict)

# time complexity - to delete - O(1)/ amortized O(n)
# space complexty - O(1)

# Dictionary methods

# shallow copy of original dictionary

anotherDict = myDict.copy()
print(anotherDict)
print(myDict)

# fromkeys - creates a new dictionary from given keys
# keys - mandatory field. Needs an iterable
# Values - optional. it will return None if not specified

newDict = {}.fromkeys([1, 2, 3], 1)
print(newDict)

# get method. takes 'key' and 'value' (optional - value to be returned if key is not found)
# searches for the key

print(myDict.get('age', 31))
print(myDict.get('city', 31))

# items. returns list of given dictionaries - tuple pair

print(myDict.items())

# keys. returns a list of keys

print(myDict.keys())

# myDict.clear()
# print(myDict)

# popitems. randomly removes a key value pair from the dictionary.

print(myDict.popitem())
print(myDict)

# set default. search for a given key and return the same if present.
# Else add the key with the default value mentioned.

print(myDict.setdefault('name', 'shesha'))
print(myDict.setdefault('lastname', 'shesha'))
print(myDict)

# pop. removes the given key from dictionary
# if key doesn't exist, it returns the default value mentioned

print(myDict.pop('middlename', 'R'))
print(myDict.pop('name', 'R'))
print(myDict)

# values. returns a list of values.

print(myDict.values())

# update. updates from another dictionary or an iterable key value pair

updateDict = {'a': 1, 'b': 2, 'c': 3}
myDict.update(updateDict)
print(myDict)

# build in python dictionary functions
# in operator - only checks for keys

print(engToSp)

print('one' in engToSp)
# or
print('uno' in engToSp.values())

# time complexity for in operator on a dictionary is O(1), coz it uses hash tables to search the element
# time complexity for in operator on a list in O(n), coz it uses linear search

# for operator - traverses all keys

for key in engToSp:
    print(key)

for key in engToSp:
    print(engToSp[key])

# take O(n) time complexity - for operator

# all() method
# returns true if all values are true
# works like logical AND operator
# if dictionary is empty, it returns True

#myDict1 = {1: True, 2: True}
#print(all(myDict1))

#myDict2 = {2: False, 0: False}
#print(all(myDict2))
myDict3 = {0: False, 2: False, 3: True}
print(all(myDict3))
#myDict4 = {1: False, 2: True, 3: True}
#print(all(myDict4))
#myDict5 = {}
#print(all(myDict5))
