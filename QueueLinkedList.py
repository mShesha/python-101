# time : O(1) for all operations
#Space : O(1) for all operations

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        # converting teh linked list to an iterable
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Queue:
    # time : O(1)
    # Space : O(1)

    def __init__(self):
        self.LinkedList = QueueLinkedList()

    # making the queue printable
    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def enqueue(self, item):
        node = Node(item)
        if self.isEmpty():
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node
        return "Item added to the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            firstElement = self.LinkedList.head.value
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

customQueue = Queue()
print(customQueue.isEmpty())
print(customQueue.enqueue(11))
print(customQueue.enqueue(21))
print(customQueue.enqueue(31))
print(customQueue)
print("first element is : " + str(customQueue.dequeue()))
print(customQueue)
print("peeking : " + str(customQueue.peek()))
print(customQueue)
customQueue.delete()
print(customQueue)
