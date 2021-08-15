# queue using list with the max capacity

class QueueMaxLimit:
    def __init__(self,maxsize):
        self.maxSize = maxsize
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items)== self.maxSize:
            return True
        else:
            return False

    def enqueue(self,item):
        if self.isFull():
            return "No new item can be added to the queue as the queue is full"
        else:
            self.items.append(item)
            return "Element added to the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[0]

    def deleteQueue(self):
        self.items = None

customQueue = QueueMaxLimit(10)
print(customQueue.isEmpty())
print(customQueue.isFull())
print(customQueue.enqueue(1))
customQueue.enqueue(19)
customQueue.enqueue(21)
customQueue.enqueue(17)
print(customQueue)
customQueue.dequeue()
customQueue.enqueue(11)
customQueue.enqueue(119)
customQueue.enqueue(211)
customQueue.enqueue(117)
print(customQueue)
customQueue.enqueue(1219)
customQueue.enqueue(2211)
print(customQueue.enqueue(1217))
print(customQueue.enqueue(12211))
print(customQueue.enqueue(21217))
print(customQueue)
print("peek : " + str(customQueue.peek()))
print(customQueue)
