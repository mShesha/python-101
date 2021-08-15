# Queue is a DS which stores data in FIFO manner
# uses: Printer queue
# Call center
# order in restaurants etc
# operations : createQueue, enqueue, dequeue, peek, isEmpty, isFull, deleteQueue

# implementation : using lists( with and without limit (circular queue)) and linked lists

# Queues using python lists - without limit

class Queue:
    # time: O(1)
    # space: O(1)

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # time: O(1)
    # space: O(1)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    # time: amortized constant : if the list reaches its full capacity, it takes O(n2) coz, it needs to move the entire list to a different memory location. Else, O(1)
    # space: O(1)

    def enqueue(self, value):
        self.items.append(value)
        return "element inserted at the end of queue"

    # time: O(n) - removing elements from the beginning of list, every other element has to be shifted one space to the right
    # space: O(1)

    def dequeue(self):
        if self.isEmpty():
            return "No elements in the queue"
        else:
            return self.items.pop(0)

    # time : O(1)
    # space: O(1)

    def peek(self):
        if self.isEmpty():
            return "No elements in the queue"
        else:
            return self.items[0]

    # time: O(1)
    # space: O(1)

    def deleteQueue(self):
        self.items = None

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(7)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print("peek :" + str(customQueue.peek()))
print(customQueue)
customQueue.deleteQueue()