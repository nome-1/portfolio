class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertsll(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == 1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextnode = tempNode.next
                tempNode.next = newnode
                newnode.next = nextnode

    def traveling(self):
        if self.head is None:
            print("the single linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


sll = linkedlist()
sll.insertsll(1, 0)
sll.insertsll(7, 1)
sll.insertsll(3, 1)
sll.insertsll(5, 1)
sll.insertsll(0, 2)
sll.insertsll(20, 3)
sll.insertsll(10, 5)

print([node.value for node in sll])
sll.traveling()
