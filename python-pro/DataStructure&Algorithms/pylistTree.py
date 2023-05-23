class BinaryTree:
    def __init__(self, size):
        self.list = size * [None]
        self.lastUSedINdex = 0
        self.maxsize = size

    def insertNode(self, value):
        if self.lastUSedINdex + 1 == self.maxsize:
            return "Tree is full"
        self.list[self.lastUSedINdex + 1] = value
        self.lastUSedINdex += 1
        return "The value has been inserted"

    def print(self):
        return self.list[1:]


newbt = BinaryTree(6)
print(newbt.insertNode("Drinks"))
print(newbt.insertNode("Hot"))
print(newbt.insertNode("COld"))
print(newbt.print())
