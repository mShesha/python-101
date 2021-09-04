# time complexity = O(1)
# space complexity = O(n)

from BinaryTreeLL import deleteDeepestNode


class BinaryTree:
    def __init__(self,size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # inserting value to a binary tree (list)
    # time complexity = O(1)
    # space complexity = O(1)

    def insertBT(self,value):
        if(self.lastUsedIndex+1 == self.maxSize):
            return "the binary tree is full"
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
            return "Value has been sucessfully added to the tree"

    # search for a node in BT using python list
    # time complexity = O(n)
    # space complexity = O(1)

    def searchBT(self, searchValue):
        for i in range(1, len(self.customList)):
            if self.customList[i] == searchValue:
                return "Success. Found the given value"
        return "Value not found"

    # time complexity : O(n/2) + O(n/2) + O(1) = O(n)
    # space complexity : O(n)

    def preOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 +1)

    # time complexity : O(n/2) + O(n/2) + O(1) = O(n)
    # space complexity : O(n)

    def inOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    # time complexity : O(n/2) + O(n/2) + O(1) = O(n)
    # space complexity : O(n)

    def postOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)        
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])

    # time complexity : O(n)
    # space complexity : O(1)

    def levelOrderTraversal(self, index=1):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    # time complexity : O(n)
    # space complexity : O(1)

    def deleteNode(self, node):
        if self.lastUsedIndex == 0:
            return "No element to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == node:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Delete successful"
        return "Element not found"    

    # time complexity : O(1)
    # space complexity : O(1)

    def deleteEntireBT(self):
        self.customList = None
        return "BT has been sucessfully deleted"

newBt = BinaryTree(8)
print(newBt.insertBT("Drinks"))
print(newBt.insertBT("Hot"))
print(newBt.insertBT("Cold"))
print(newBt.insertBT("Coffee"))
print(newBt.insertBT("Tea"))
print(newBt.customList)
print(newBt.searchBT("Hot"))
print(newBt.searchBT("Hotty"))
print("pre order traversal")
newBt.preOrderTraversal()
print("in order traversal")
newBt.inOrderTraversal()
print("post order traversal")
newBt.postOrderTraversal()
print("level order traversal")
newBt.levelOrderTraversal()
print("delete node")
newBt.deleteNode("Hot")
newBt.levelOrderTraversal()
print("delete entire BT")
newBt.deleteEntireBT()
newBt.levelOrderTraversal()



