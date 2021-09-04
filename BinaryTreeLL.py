# DS where each node can have at most 2 children.
# BT is a family of data structure (BST,Heap tree, AVL, red black tree, syntax tree)
# why BT: it is a prerequisite for more advanced trees like BST, AVL, Red black tree
# Huffman coding problem, heap priority problem and expression parsing problems can be solved using BT

# types of BT:
# full BT (has 0 or 2 children but not 1)
# perfect BT (all non-leaf nodes have 2 children and has the same depth (so, leaf nodes are at the same level))
# complete BT (all levels are completely filled except the last one)
# balanced BT (each leaf is not more than a certain distance from the root node)

# create BT - Linked list / python list

import QueueLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# time = O(1)
# space = O(1)

newBT = TreeNode("Drinks")

# Traversal of binary tree

# Depth first search
#   -   preorder traversal - root node - left subtree - right subtree
#   -   inorder traversal - left subtree - root node - right subtree
#   -   post order traversal - left subtree - right subtree - root node
# Breadth first search
#   -   level order traversal - level by level. starts with Level 1

# **********************************************--------------------------------------------************************************#

leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

leftHotChild = TreeNode("Coffee")
rightHotChild = TreeNode("Tea")

newBT.leftChild.leftChild = leftHotChild
newBT.leftChild.rightChild = rightHotChild

print("Pre order traversal")


# time complexity = O(1)+O(1)+O(1)+O(N/2)+O(N/2) = O(n)
# space complexity = O(N)

def preOrderTraversal(rootNode):
    if not rootNode:  # O(1)
        return  # O(1)
    print(rootNode.data)  # O(1)
    preOrderTraversal(rootNode.leftChild)  # O(n/2)
    preOrderTraversal(rootNode.rightChild)  # O(n/2)


preOrderTraversal(newBT)

print("In order traversal")


# time complexity = O(1)+O(1)+O(1)+O(N/2)+O(N/2) = O(n)
# space complexity = O(N)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


inOrderTraversal(newBT)

print("Post order traversal")


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


postOrderTraversal(newBT)

print("Level order traversal")


# time complexity : O(n)
# space complexity : O(n)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)

            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)


print("levelOrderTraversal")
levelOrderTraversal(newBT)


# we use LOT for search, coz it uses queue as opposed to stack used in all other traversal methods.
# time complexity : O(n)
# space complexity : O(n)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == nodeValue:
                return "Found"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)

            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)

        return "Not found"


print("Tea : " + searchBT(newBT, "Tea"))
print("Cola : " + searchBT(newBT, "Cola"))


# inserting a node to a binary tree
# 2 options - when root is blank. i.e, no tree exists
#           - root exists and we have to look for a first vacant place
# LOT - level order traversal

# time complexity = O(n)
# space complexity = O(n)

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return "node added to the tree"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            else:
                newLeftChild = TreeNode(newNode)
                root.leftChild = newLeftChild
                return "node added to the tree"

            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)
            else:
                newRightChild = TreeNode(newNode)
                root.rightChild = newRightChild
                return "node added to the tree"


print(insertNodeBT(newBT, "Cola"))
levelOrderTraversal(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        deepestNode = root.data
        return deepestNode

print("deepest node is : " + getDeepestNode(newBT))


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data is dNode:
                root.data = None
                return
            if root.rightChild:
                if root.rightChild is dNode:
                    root.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.rightChild)
            if root.leftChild:
                if root.leftChild is dNode:
                    root.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.leftChild)

newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT,newNode)
levelOrderTraversal(newBT)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "Failed to delete"

print("Delete node")
deleteNodeBT(newBT,"Tea")
levelOrderTraversal(newBT)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted" 

inOrderTraversal(newBT)

           