# circular singly linked list is same as singly linked list,
# except the last node is connected back to the first node.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # printing the values of the Linked List
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # create a circular singly linked list

    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "The circular singly linked list is created"

    # insert new node at the beginning, any location or at the end of a circular singly linked list

    def insertCSLL(self, value, location):
        if self.head is None:
            return "the circular singly linked list doesn't exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode  # link between new node and last node
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "the node has been successfully inserted"

    # traverse the circular singly linked list

    def traverseCSLL(self):
        if self.head is None:
            return "the circular singly linked list doesn't exist"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # search for a node in CSLL

    def searchCSLL(self, nodevalue):
        if self.head is None:
            return "the circular singly linked list doesn't exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodevalue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "the node doesn't exist in the CSLL"

    # deletion of a node from CSLL

    def deleteNodeCSLL(self, location):
        if self.head is None:
            return "the circular singly linked list doesn't exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # delete entire CSLL

    def deleteCSLL(self):
        if self.head is None:
            return "the circular singly linked list doesn't exist"
        else:
            self.tail.next = None
            self.tail = None
            self.head = None


circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)

print([node.value for node in circularSLL])

circularSLL.insertCSLL(2, 0)
print([node.value for node in circularSLL])

circularSLL.insertCSLL(0, -1)
print([node.value for node in circularSLL])

circularSLL.insertCSLL(1.5, 1)
print([node.value for node in circularSLL])

circularSLL.traverseCSLL()

print(circularSLL.searchCSLL(15))

circularSLL.insertCSLL(2.5, 0)
print([node.value for node in circularSLL])

circularSLL.deleteNodeCSLL(0)
print([node.value for node in circularSLL])

circularSLL.deleteNodeCSLL(1)
print([node.value for node in circularSLL])

circularSLL.deleteNodeCSLL(-1)
print([node.value for node in circularSLL])

circularSLL.deleteCSLL()
print([node.value for node in circularSLL])