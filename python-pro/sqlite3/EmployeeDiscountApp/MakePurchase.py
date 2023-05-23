import sqlite3
from MakeLog import makelog



def makeapurchase(iid, eid):
    con = sqlite3.connect("items.sql")
    cur = con.cursor()
    bob=(cur.execute("SELECT itemCost FROM itempage where iid=(?)", (iid,)))
    up=(bob.fetchone())
    con.close()
    #-----employee update
    con = sqlite3.connect("test.sql")
    cur = con.cursor()
    a=(cur.execute("SELECT EmployeeType,YearsWorked FROM employee where EmployeeID=(?)",(eid,)))
    cal=a.fetchone()
    discount=0
    if cal[0]=="hourly":
        discount=2*cal[1]
        if discount>=10:
            discount=0.10
        else:
            discount=discount/100
    elif cal[0]=="manager":
        discount = 2 * cal[1]+10
        if discount >= 20:
            discount = 0.20
        else:
            discount=discount/100

    totald=up[0]*discount
    totalbought=up[0]-totald
    cur.execute("update employee set TotalPurchased=(?),TotalDiscount=(?) where EmployeeID=(?)", (int(totalbought),int(totald),eid))
    makelog(iid, eid)
    con.commit()

