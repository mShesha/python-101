# What is an AVL tree?
# named after their inventors - Adelson-Velskii and Landis
# AVL tree is a self-balancing binary tree. Where the difference between heights of 
# left and right subtrees cannot be more than one for all nodes.
# Since it is a BT, all properties of the BT applies to AVL tree. Left < Root < Right
# AVL tree = A balanced BST

# if any of the left or right sub trees are not balanced, i.e, teh difference in their height is > 1,
# then rebalancing is done. This process is called as rotation.

# Why AVL tree?
# Issue with BT was, it can become disbalanced tree and lead to performance issues.

import QueueLinkedList as queue

class AVLNode:

# creation of AVL tree
# time and space complexity = O(1)

    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

newAVL = AVLNode(10)



