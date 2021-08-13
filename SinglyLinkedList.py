# Linked list is a form of a sequential collection and it does not have to be in order. A linked list is made up of
# independent nodes that may contain any type of data and each node has a reference to the next node in the link.
# They are not contiguous in memory

# 4 types of linked list
# Singly Linked List
# Circular Singly Linked List
# Doubly Linked List
# Circular Doubly Linked List

# LL in memory - Random memory locations. Address is saved as a link to the previous node
# needs extra memory location to save the address of the next

# creation of singly linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # to print the elements of the LL

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in LL

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # adding a new node at the beginning of the LL
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # adding a new node at the end of the LL
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # adding a new node at the given location of the LL
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.next = nextNode
                tempNode.next = newNode
                if tempNode == self.tail:
                    self.tail = newNode

    # traverse SLL

    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # search element in the SLL

    def searchSLL(self, value):
        if self.head is None:
            print("The singly linked list doesn't exist")
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return (node.value)
                node = node.next
            return "Value doesn't exist in the SLL"

    # deletion of a node from the SLL

    def deleteNodeSLL(self, location):
        if self.head is None:
            print("The singly linked list doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    print("There is only one node in the SLL")
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            if location == -1:
                if self.head == self.tail:
                    print("There is only one node in the SLL")
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    temp = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # delete entire SLL

    def deleteSLL(self):
        if self.head is None:
            print("The singly linked list doesn't exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
print([node.value for node in singlyLinkedList])

node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
node1.next = node2  # or singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

print([node.value for node in singlyLinkedList])

# insertion to LL - beginning/middle/end
# time complexity - O(n) and space complexity - O(1)

singlyLinkedList.insertSLL(5, -1)
singlyLinkedList.insertSLL(3, 1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(4, 2)

print([node.value for node in singlyLinkedList])

singlyLinkedList.traverseSLL()

print(singlyLinkedList.searchSLL(10))

singlyLinkedList.deleteNodeSLL(0)
print([node.value for node in singlyLinkedList])

# singlyLinkedList.deleteNodeSLL(-1)
# print([node.value for node in singlyLinkedList])

# singlyLinkedList.deleteNodeSLL(1)
# print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteSLL()
print([node.value for node in singlyLinkedList])
