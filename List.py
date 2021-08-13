# collection of ordered elements
# built-in data type (primitive) - no need to import any library
# can be created using []

integerList = [1, 2, 3, 4]
stringList = ['Edy', 'John', 'Jane']
mixedList = [1, 2, 3.4, 'hello']
nestedList = [1, 3.4, ['Edy', 'John', 'Jane'], [9.0]]

# Accessing/traversing a list

shoppingList = ['Milk', 'Butter', 'Cheese']

print(shoppingList[1])

# in operator -- it is case sensitive

print('milk' in shoppingList)

# access elements backwards

print(shoppingList[-1])

# traverse a list

for i in shoppingList:
    print(i)

# insert/update elements of a list
# mutable data structures

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] = 33
print(myList)

# insert elements at the beginning, random index, at the end and merge 2 lists

# beginning
myList.insert(0, 0)  # ----------------------------------------------------------------> TC : O(n) SC: O(1)
print(myList)

# random index
myList.insert(4, 0)  # ----------------------------------------------------------------> TC : O(n) SC: O(1)
print(myList)

# append to the end
myList.append(99)  # ------------------------------------------------------------------> TC : O(1) SC: O(1)
print(myList)

newList = [11, 22, 33, 44, 55]
myList.extend(newList)  # -------------------------------------------------------------> TC : O(n) SC: O(n)
print(myList)

# delete and element from a List

myStringList = ['a', 'b', 'c', 'd', 'e', 'f']

print(myStringList[0:2])  # excluding the to index

# update multiple elements in one shot

myStringList[0:2] = ['x', 'y']
print(myStringList)

# delete elements - deletes using the index

myStringList.pop()  # removes the last element and returns that value. Works like a stack
print(myStringList)
myStringList.pop(2)  # removed element in index 2 and returns that value.
print(myStringList)

del myStringList[3]

print(myStringList)

# use remove to delete the element using its value rather than it's index

myStringList.remove('y')
print(myStringList)

# searching a value in the list

if 100 in myList:
    print(myList.index(100))
else:
    print("value doesn't exist in the List")

# List operations/functions
# concatenation/+

a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
print(c)

# repetitive/*

a = [0, 1]
a = a * 2
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

# string to list

str = 'stringToList'
lst = list(str)
print(lst)

# string to list using split method

strSplitOnHyphen = 'Notre-Dame-de-la-Garde'
listFromString = strSplitOnHyphen.split('-')
print(listFromString)

# List to string
# join function

stringFromList = '-'.join(listFromString)
print(stringFromList)

# pitfalls while using List

# 1) many operations on List are in-place and if we try to assign it to the same variable, it returns None
# example:

test = [1,4,2,3,6,5]
test = test.sort() # returns None here. Instead, see below.
print(test)

test1 = [1,4,2,3,6,5]
test1.sort() # sorts teh list in-place
print(test1)

# 2) there are many ways to insert/delete elements in a List. Be careful while using them.
# append/concatenate
# delete/remove/pop

# 3) Since, many operations are in-place, take a copy of the variables where possible.

##########################################################################################################
###                                      ARRAYS V/S LISTS                                              ###
##########################################################################################################

# Similarities

# 1) both are mutable. Both can be updated using their indices
# 2) both can be sliced and diced
# 3) both can be indexed and iterated through

# Differences - operations we can perform on them
# if we need to perform arithmetic operations on them, Array's are optimized for the same
# you can add different data types to List, also to Array. But it will convert everything to the more larger data-type (int v/s string - everything will be converted to string)
# example

import numpy as np

# 1

myArray = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5,6]

print(myArray/2)
# print(myList/2)
# errors out with - TypeError: unsupported operand type(s) for /: 'list' and 'int'

# 2

newArray = np.append(myArray,['a']) # all converted to string - ['1' '2' '3' '4' '5' '6' 'a']
myList.append('a') # all remains same - [1, 2, 3, 4, 5, 6, 'a']

print(newArray)
print(myList)





