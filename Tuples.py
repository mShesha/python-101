# Tuples
# Tuples are immutable sequence of python objects
# Tuples are iterable, comparable and hashable (hashable: whose values do not change over their lifetime)

# create a tuple:

newTuple1 = 'a', 'b', 'c', 'd', 'e'
newTuple2 = ('a', 'b', 'c', 'd', 'e')
newTuple3 = tuple('abcde')
newTuple4 = ('a',)  # single element tuple needs to be followed by a , else it will treat it as a string. Example below
newTuple5 = ('a')
newTuple6 = tuple('a')  # this works
# newTuple7 = tuple('a','b','c') # doesn't work. needs 1 argument

print(newTuple1)
print(newTuple2)
print(newTuple3)
print(newTuple4)
print(newTuple5)
print(newTuple6)
# print(newTuple7)

# tuples in memory and how to access them

# access - bracket [] operator / slice ( excludes the left index)

print(newTuple1[3])
print(newTuple1[-1])
print(newTuple1[-2])
print(newTuple1[1:3])

# traverse a tuple

for i in newTuple1:
    print(i)

for i in range(len(newTuple1)):
    print(newTuple1[i])

# search in tuple

print('b' in newTuple1)


# or linear search

def searchTuple(ptuple, element):
    for j in ptuple:
        if j == element:
            return ptuple.index(j)
    return 'element doesnt exist in the tuple'


print(searchTuple(newTuple1, 'c'))

# tuple operations

print(newTuple1 + newTuple2)

print(newTuple2 * 4)  # * for repetition

print('c' in newTuple2)

# no add/delete method cos they are immutable
# count and index are available

print(newTuple1.count('a'))
print(newTuple1.index('a'))
print(len(newTuple1))
print(max(newTuple1))
print(min(newTuple1))
print(tuple([1, 2, 3, 4, 5]))  # convert list to tuple

# Tuple v/s List
# List can be modified, reassigned, delete an element or the entire List

list1 = [0, 1, 2, 3, 4, 5, 6, 7]
list1[1] = 3
print(list1)

list1 = [7, 6, 5, 4, 3, 2, 1, 0]
print(list1)

tuple1 = (0, 1, 2, 3, 4, 5, 6, 7)
# tuple1[1] = 3 # typeError. Immutable tuples
print(tuple1)
# can reassign the entire tuple. cannot change single element
# same for delete
tuple1 = (7, 6, 5, 4, 3, 2, 1, 0)
print(tuple1)

# can create tuples inside List and vice versa

myList = [(1,2),(3,4),(5,6)]
myTuple = ([1,2],[3,4],[5,6])

print(myList)
print(myTuple)
