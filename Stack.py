# Stack - can be imagined as a data structure where pile of objects are stacked vertically
# stack is a data structure that stores items in last-in/first-out manner.
# stack operations: create stack , push, pop, peek, isEmpty, isFull, delete

# 3 ways to create a stack - list with and without size limits and using linked lists

# create stack using Python Lists without size limits

# using list - implementation is easy but might run into speed issues cos the memory is contiguous when compared to Linked list.
# With LL, implementation is not easy.

class Stack:
    def __init__(self):
        self.list = []

    # changing str method to display the stack in the LIFO order
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    # push time complexity : amortized time complexity. cos, when list is initialized, it will allocate a little more
    # than 1 memory location. when the end is reached and this is has no size limit, the memory has to be
    # re-allocated. this can be O(n) or worst case can be O(n-squared) also

    def push(self, value):
        self.list.append(value)
        return "the element has been inserted successfully"

    # pop

    def pop(self):
        if not self.list:
            return "No element in this stack"
        else:
            return self.list.pop()

    # peek

    def peek(self):
        if not self.list:
            return "No element in this stack"
        else:
            return self.list[-1]

    # delete stack

    def delete(self):
        self.list = []
        # self.list = None # from the lecture


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print("push")
# print(customStack)
print("pop")
print(customStack.pop())
print("peek")
# print(customStack)
print(customStack.peek())
print("stack")
print(customStack)
customStack.delete()
print(customStack)
