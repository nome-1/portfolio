import UseQueue as Queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = treeNode("Drinks")
leftc = treeNode("hot")
left = treeNode("coffe")
right = treeNode("chocolateMilk")
rightc = treeNode("cold")
l1 = treeNode("appleJuice")
r1 = treeNode("IcedTea")
new = treeNode("wine")
tom =treeNode("SweatTea")
newBT.leftChild = leftc
newBT.rightChild = rightc
newBT.leftChild.leftChild = left
newBT.leftChild.rightChild = right
newBT.rightChild.leftChild = l1
newBT.rightChild.rightChild = r1


def inOrderTraversal(tree):
    if tree is None:
        return
    inOrderTraversal(tree.leftChild)
    print(tree.data)
    inOrderTraversal(tree.rightChild)


inOrderTraversal(newBT)
print("_____" * 3)


def postOrderTraversal(tree):
    if tree is None:
        return
    postOrderTraversal(tree.leftChild)
    postOrderTraversal(tree.rightChild)
    print(tree.data)


postOrderTraversal(newBT)

print("_____" * 3)


def preOrderTraversal(tree):
    if tree is None:
        return
    print(tree.data)
    preOrderTraversal(tree.leftChild)
    preOrderTraversal(tree.rightChild)


preOrderTraversal(newBT)
print("_____" * 3)


def levelOrderTraversal(tree):
    if tree is None:
        return
    else:
        cusQueue = Queue.lQueue()
        cusQueue.enqueue(tree)
        while not cusQueue.isEmpty():
            root = cusQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                cusQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                cusQueue.enqueue(root.value.rightChild)


levelOrderTraversal(newBT)


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue.lQueue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"


insertNodeBT(newBT, new)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.lQueue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.lQueue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = Queue.lQueue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"


print("_____" * 3)
insertNodeBT(newBT,tom)
deleteNodeBT(newBT,"wine")
postOrderTraversal(newBT)
