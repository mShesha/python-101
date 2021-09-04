## Trees are nonlinear data structure with hierarchical relationships between its elements without having any cycle.
## properties: used to represent hierarchical data
##             each node has 2 components: data and a link to it's sub category
##             base category is at the top of sub category
## why tree? : non-linear data is needed as array/list etc are all linear
##             quicker and easier access to data
##             naturally hierarchical (file system)
##             different type of tree DS which performs better in different situations
## tree terminologies: Root: root is a node which doesn't have any parent. 1 tree 1 root
##                     Edge: a link between parent and it's child
##                     Leaf: a leaf is a node which doesn't have any children
##                     Sibling: children of the same parent
##                     Ancestor: parent, grandparent or great grandparent of a node
##                     Depth of node: length of the path from root to node
##                     Height of node: length of the path from node to the deepest node
##                     Depth of tree: depth of root node == 0
##                     Height of tree: height of root node

class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
pepsi = TreeNode('Pepsi', [])
coke = TreeNode('Coke', [])
coffee = TreeNode('Coffee', [])
tea = TreeNode('Tea', [])
tree.addChild(cold)
tree.addChild(hot)
cold.addChild(coke)
cold.addChild(pepsi)
hot.addChild(coffee)
hot.addChild(tea)
print(tree)
