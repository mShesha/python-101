# Circular queues : Queues have a max capacity and are enqueued/dequeued in circular manner

class CircularQueue:
    # time:  O(1)
    # space: O(n)
    def __init__(self, maxsize):
        self.maxSize = maxsize
        self.items = [None] * maxsize
        self.start = -1
        self.end = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # time : O(1)
    # Space : O(1)

    def isEmpty(self):
        if self.end == -1:
            return True
        else:
            return False

    # time : O(1)
    # Space : O(1)

    def isFull(self):
        if (self.end + 1 == self.start) or (self.start == 0 and self.end + 1 == self.maxSize):
            return True
        else:
            return False

    # time : O(1)
    # Space : O(1)

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.end + 1 == self.maxSize:
                self.end = 0
            else:
                self.end += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.end] = value
            return "Element is inserted at the end of the Queue"

    # time : O(1)
    # space : O(1)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty to dequeue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.end == self.start:
                # last element in the queue. Setting the start and end to -1
                self.end = -1
                self.start = -1
            elif self.start + 1 == self.maxSize:
                # the queue has reached the end. Circling back to first position.
                self.start = 0
            else:
                # incrementing the start by one after dequeueing the queue by 1 element
                self.start += 1
            # setting the dequeued position to None. So it can be reused.
            self.items[start] = None
            return firstElement

    # time : O(1)
    # space : O(1)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty to have a peek at it's top element"
        else:
            return self.items[self.start]

    # time : O(1)
    # space : O(1)

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.end = -1

circularQueue = CircularQueue(10)
print(circularQueue.isEmpty())
print(circularQueue.isFull())
print(circularQueue.enqueue(1))
print(circularQueue.enqueue(10))
print(circularQueue.enqueue(21))
print(circularQueue.enqueue(17))
print(circularQueue.enqueue(19))
print(circularQueue)
print(circularQueue.dequeue())
print(circularQueue)
print("peek: " + str(circularQueue.peek()))
circularQueue.delete()
print(circularQueue)
