# Creating stack using Linked Lists

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None # not needed for stack

    # to print the elements of the LL. Make it an iterable

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    # O(1) time complexity
    # O(1) space complexity

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    # O(1) time complexity
    # O(1) space complexity
    # the GC will collect the de-linked nodes. No need to destroy them in the program

    def pop(self):
        if self.isEmpty():
            return "There is no element to return"
        else:
            popValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return popValue

    # O(1) time complexity
    # O(1) space complexity

    def peek(self):
        if self.isEmpty():
            return "There is no element to peek into"
        else:
            return self.LinkedList.head.value

    # O(1) time complexity
    # O(1) space complexity

    def delete(self):
        self.LinkedList.head = None


LLStack = Stack()
print(LLStack.isEmpty())
LLStack.push(2)
LLStack.push(1)
LLStack.push(4)
print(LLStack)
print("popped value = " + str(LLStack.pop()))
print(LLStack)
print("peek value = " + str(LLStack.peek()))
print(LLStack)
LLStack.delete()
print(LLStack)
