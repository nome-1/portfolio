class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:  # construct the data structure
    def __init__(self):
        self.head = None
        self.id = 0  # index for head, also the length of mylist
        # self.list =[] # debug mode, remove # at each method to enable

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:  # add to empty list
            self.head = node
        # self.list.append(val)
        else:  # add to exist list
            self.head, node.next = node, self.head
        # self.list = [val] + self.list
        self.id += 1

    # self.debug()
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            pre = self.head
            for _ in range(self.id - 1):  # find previous node of tail(=None)
                pre = pre.next
            pre.next = Node(val)
            self.id += 1

        # self.list.append(val)
        # self.debug()

    def deleteAtIndex(self, index: int) -> None:
        if index < self.id:
            pre = self.head
            for _ in range(index - 1):  # find previous node of where to delete
                pre = pre.next
            # pre -> original pre.next.next(= current pre.next)
            if index == 0 and pre:
                self.head = pre.next
            elif pre.next:
                pre.next = pre.next.next
            self.id -= 1

            # del self.list[index]
            # self.debug()

    def get(self, index: int) -> int:
        # if index == self.iid, the elements will be None which doesn't have val
        if index < self.id:
            x = self.head
            for _ in range(index):
                x = x.next
                # self.debug()
            return x.val
        return -1
