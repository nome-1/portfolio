class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = value
        else:
            tail = self.head
            while True:
                if tail.next is None:
                    break
                tail = tail.next
            tail.next = value
            # print(tail.data)
            # print(tail.next.data)

    def printList(self):
        cur = self.head
        while True:
            if cur is None:
                break
            print(cur.data)
            cur = cur.next


l = LinkedList()
t = Node("john")
t1 = Node("frank")
t2 = Node("bill")
l.insert(t)
l.insert(t1)
l.insert(t2)
l.printList()
