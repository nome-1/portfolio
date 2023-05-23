class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next


class lQueue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        v=[str(x) for x in self.LinkedList]
        return " ".join(v)

    def enqueue(self, value):
        newNode = node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.LinkedList.head


cq = lQueue()
cq.enqueue(4)
cq.enqueue(3)
cq.enqueue(8)
cq.enqueue(1)
cq.dequeue()
print(cq.peek())
print(cq)
