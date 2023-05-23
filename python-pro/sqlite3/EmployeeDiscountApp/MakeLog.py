import sqlite3

def makelog(iid,eid):
    con = sqlite3.connect("items.sql")
    cur = con.cursor()
    bob = (cur.execute("SELECT iid,itemCost FROM itempage where iid=(?)", (iid,)))
    up = (bob.fetchone())
    con.close()
    # -----employee update
    con = sqlite3.connect("test.sql")
    cur = con.cursor()
    a = (cur.execute("SELECT EmployeeID,TotalPurchased FROM employee where EmployeeID=(?)", (eid,)))
    cal = a.fetchone()
    con.close()
    new = sqlite3.connect("purchasehistory.sql")
    newcur=new.cursor()
    newcur.execute("CREATE TABLE IF NOT EXISTS history(iid integer primary key autoincrement,"
                "itemID,itemCost,EmployeeID,TotalPurchased)")
    log=[
        None,
        up[0],
        up[1],
        cal[0],
        cal[1]
    ]
    newcur.execute("INSERT INTO history VALUES(?, ?, ?,?,?)", log)
    #for row in newcur.execute("SELECT * FROM history"):
        #print(row)
    new.commit()
    new.close()

