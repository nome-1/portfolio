import sqlite3

con = sqlite3.connect("items.sql")
cur = con.cursor()


class CreateItems:
    def __init__(self, itemName: str, itemCost: int):
        self.itemName = itemName.__str__()
        self.itemCost = itemCost.__int__()
        self.table = cur.execute("CREATE TABLE IF NOT EXISTS itempage(iid integer primary key autoincrement,"
                                 "itemName,itemCost)")

    def createitems(self):
        item = [
            None,
            self.itemName,
            self.itemCost,
        ]
        check = [box for box in cur.execute("SELECT itemName FROM itempage")]
        if (item[1],) in check:
            print(f"the itm {item[0]} already exists")
        else:
            cur.execute("INSERT INTO itempage VALUES(?, ?,?)", item)
            con.commit()


# dd = CreateItems("green Shoes", 100)
# dd.createitems()
#print("Item Number | Item Name   | Item Cost")
#tes = "{0}           |{1} |   {2}"
#for row in cur.execute("SELECT * FROM itempage"):
    #print(tes.format(row[0], row[1], row[2]))
