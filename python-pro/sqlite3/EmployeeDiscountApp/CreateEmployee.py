import sqlite3

con = sqlite3.connect("test.sql")
cur = con.cursor()


class CreateEmployee:
    def __init__(self, EmployeeID: int, EmployeeName: str, EmployeeType: str,
                 YearsWorked: int, EmployeeDiscountNumber: int, TotalPurchased: int = 0, TotalDiscount: int = 0):
        self.EmployeeID = EmployeeID.__int__()
        self.EmployeeName = EmployeeName.__str__()
        self.EmployeeType = EmployeeType.__str__()
        self.YearsWorked = YearsWorked.__int__()
        self.TotalPurchased = TotalPurchased.__int__()
        self.TotalDiscount = TotalDiscount.__int__()
        self.EmployeeDiscountNumber = EmployeeDiscountNumber.__int__()
        self.table = cur.execute("CREATE TABLE IF NOT EXISTS employee(EmployeeID, EmployeeName, EmployeeType,"
                                 "YearsWorked,"
                                 "TotalPurchased,TotalDiscount,EmployeeDiscountNumber)")

    def createemployee(self):
        employee = [
            self.EmployeeID,
            self.EmployeeName,
            self.EmployeeType,
            self.YearsWorked,
            self.TotalPurchased,
            self.TotalDiscount,
            self.EmployeeDiscountNumber
        ]
        check = [box for box in cur.execute("SELECT EmployeeID FROM employee")]
        if (employee[0],) in check:
            print(f"the id {employee[0]} has already been used please call admin for support")
        else:
            cur.execute("INSERT INTO employee VALUES(?, ?, ?,?,?,?,?)", employee)
            con.commit()


#  data = [1500, "fizz root", 'salad', 8, 0, 0, 1101]
# a=data[0]
# b=data[1]
# c=data[2]
# d=data[3]
# e=data[4]
#
#em = CreateEmployee(a,b,c,d,e)
#em.createemployee()
#for row in cur.execute("SELECT * FROM employee"):
    #print(row)
