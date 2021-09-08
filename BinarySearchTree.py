# what is a binary search tree?
# basically a binary tree with additional properties.
#   left subtree, the value is less than or equal to its parent node's value
#   rigth subtree, the value is greater than or equal to its parent node's value

# doesn't store index of each state element.instead relies on implicite structure to keep a record of where element is.
# hence, performs better than binary tree when inserting and deleting.

# create a tree, insert a node, delete a note, search a node, traverse all node, delete the entire BST

import QueueLinkedList as queue

class BSTNode:
    # time complexity : O(1)
    # space complexity : O(1)

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# time complexity : O(log n)
# space complexity : O(log n)

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "element inserted successfully!"

# for all 4 below
# time complexity : O(n)
# space complexity : O(n)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    inOrderTraversal(rootNode.rightChild)    
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)

# time complexity : O(log N)
# space complexity : O(log N)

def searchBST(rootNode, nodeVale):
    if rootNode.data == nodeVale:
        print("Found the value")
    elif nodeVale < rootNode.data:
        if rootNode.leftChild.data == nodeVale:
            print("Found the value")
        else:
             searchBST(rootNode.leftChild, nodeVale)
    elif nodeVale > rootNode.data:
        if rootNode.rightChild.data == nodeVale:
            print("Found the value")
        else:
             searchBST(rootNode.rightChild, nodeVale) 
    else:
        print("Value not found")

# delete BST
# The node to be deleted is a leaf node
# The node has one child
# The node has two children

# time complexity : O(log N)
# space complexity: O(log N)

def minValue(bstNode):
    currentNode = bstNode
    while (currentNode.leftChild is not None):
        currentNode = currentNode.leftChild
    return currentNode

def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

# time complexity : O(1)
# space complexity : O(1)

def deleteBST(rootNode):
    rootNode.leftChild = None
    rootNode.rightChild = None
    rootNode.data = None
    return "the BST has been sucessfully deleted"    

newBST = BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,60))
print(insertNode(newBST,10))
print(insertNode(newBST,20))
print(insertNode(newBST,80))
print(insertNode(newBST,90))
print(insertNode(newBST,30))
print(insertNode(newBST,50))
print("preOrderTraversal")
preOrderTraversal(newBST)
print("inOrderTraversal")
inOrderTraversal(newBST)
print("postOrderTraversal")
postOrderTraversal(newBST)
print("levelOrderTraversal")
levelOrderTraversal(newBST)
print("Searching BST")
searchBST(newBST, 80)
deleteNode(newBST,20)
print("levelOrderTraversal")
levelOrderTraversal(newBST)
deleteNode(newBST,90)
print("levelOrderTraversal")
levelOrderTraversal(newBST)
print(deleteBST(newBST))
levelOrderTraversal(newBST)

