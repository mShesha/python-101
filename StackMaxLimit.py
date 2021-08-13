class StackMaxLimit:
    def __init__(self, maxsize):
        self.maxSize = maxsize
        self.list = []

    # changing str method to display the stack in the LIFO order
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push time complexity : amortized time complexity. cos, when list is initialized, it will allocate a little more
    # than 1 memory location. when the end is reached and this is has no size limit, the memory has to be
    # re-allocated. this can be O(n) or worst case can be O(n-squared) also
    # change this

    def push(self, value):
        if self.isFull():
            return "stack is full"
        else:
            self.list.append(value)
            return "Inserted the element to the stack"

    def pop(self):
        if self.isEmpty():
            return "The stack is empty. Cannot pop an empty stack"
        else:
            return self.list.pop()

    # time and space complexity = O(1)
    def peek(self):
        if self.isEmpty():
            return "The stack is empty. Cannot peek into an empty stack"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None

customStack = StackMaxLimit(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(4)
customStack.push(7)
# print(customStack)
print(customStack.pop())
print(customStack.peek())
customStack.delete()

