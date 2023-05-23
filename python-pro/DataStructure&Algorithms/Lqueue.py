class line:
    def __init__(self):
        self.QLine = []

    def NotEmpty(self):
        if len(self.QLine)>0:
            return True
        else:
            return False

    def addtoqueue(self, item):
        self.QLine.append(item)

    def peek(self):
        if self.NotEmpty():
            return self.QLine[0]

    def removefromqueue(self):
        if self.NotEmpty():
            self.QLine.pop(0)
        else:
            return None

    def __str__(self):
        if self.NotEmpty():
            return str(self.QLine)

    def __getitem__(self, item):
        return [x for x in self.QLine]


tom = line()
tom.addtoqueue(88)
tom.addtoqueue(1)
tom.addtoqueue(15)
tom.addtoqueue(9)
print(tom.peek())
tom.removefromqueue()
print(tom.peek())
print(tom)
