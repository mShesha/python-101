from array import *
import numpy as np

# create an array

arr = array('i',[2,3,4,5,6])

# insert an element at the beginning of the array
# time complexity is O(n)

arr.insert(0,1)

print(arr)

# array traversal
# time complexity - O(n)
# space complexity - O(1)

def traverseArray(ary):
    for i in ary:
        print(i)

traverseArray(arr)

# accessing an array

def accessArray(ary,index):
    if index >= len(ary):
        print("Index out of range.")
    else:
        print("array at index "+ str(index)+ " = " +str(ary[index]))

accessArray(arr,3)

# search an element in the array

def searchArray(ary,value):
    for i in ary:
        if i==value:
            return ary.index(value)
    return "the element doesn't exist in this array"

print(searchArray(arr,7))

# delete an element from an array

arr.remove(3)
print(arr)

# create 2 dimensional array
# numpy is better for 2-D array

twoDAraay = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
print(twoDAraay)

# insert new row

newTwoDArray = np.insert(twoDAraay,0,[[5,6,7,8]],axis=1)
print(newTwoDArray)

newTwoDArrayAppend = np.append(twoDAraay,[[5,6,7,8]],axis=0)
print(newTwoDArrayAppend)

# accessing a 2D array

print(newTwoDArrayAppend[1][2])

# traverse a 2D array

def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse2DArray(newTwoDArrayAppend)

# searching an element in 2D array
# using linear search

def search2DArray(array,element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return("element found at " + str(i) + " " + str(j))
    return("element not found")

print(search2DArray(newTwoDArrayAppend,10))

# delete element (either a row or a column - cannot be an element) from 2D array

newDeleted2DArray = np.delete(newTwoDArrayAppend,1,axis=1)
print(newDeleted2DArray)





