class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def Peek(Root):
    if Root is None:
        return
    else:
        return Root.customList[1]


def Sizeofheap(Root):
    if Root is None:
        return
    else:
        return Root.heapSize


newHeap = Heap(5)



def lvlOrderTraversal(Root):
    if Root is None:
        return
    else:
        for i in range(1, Root.heapSize + 1):
            print(Root.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def inserNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"


inserNode(newHeap, 4, "Max")
inserNode(newHeap, 7, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")
inserNode(newHeap, 6, "Max")
inserNode(newHeap, 13, "Max")
inserNode(newHeap, 20, "Max")
inserNode(newHeap, 8, "Max")
print(Sizeofheap(newHeap))
lvlOrderTraversal(newHeap)
