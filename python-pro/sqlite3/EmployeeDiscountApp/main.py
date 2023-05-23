import sqlite3

from CreateEmployee import CreateEmployee
from CreateItem import CreateItems
from MakePurchase import makeapurchase

menu = {1: "1- Create Employee",
        2: "2- Create Item |",
        3: "3- Make Purchase |",
        4: "4-All Employee Summary |",
        5: "5-Exit |"}


def createEmployee():
    c = None
    while c != "no":
        print(f'do you want to add an employee, if yes input yes or y\n'
              f'if no input no')
        c = input()
        if c == "no":
            break
        else:
            print("please enter EmployeeID number")
            EmployeeID = int(input())
            print("please enter EmployeeName ")
            EmployeeName = str(input())
            print("please enter EmployeeType(hourly or salary)")
            EmployeeType = str(input())
            print("please enter how many years you worked hear")
            YearsWorked = int(input())
            print("please enter you EmployeeDiscountNumber")
            EmployeeDiscountNumber = int(input())
            em = CreateEmployee(EmployeeID, EmployeeName, EmployeeType, YearsWorked, EmployeeDiscountNumber)
            em.createemployee()


def createItem():
    c = None
    while c != "no":
        print(f'do you want to add an item to the list ?, if yes input yes or \n'
              f'if no input no')
        c = input()
        if c == "no":
            break
        else:
            print("please enter item name")
            itemName = str(input())
            print("please enter item price ")
            itemPrice = int(input())
            em = CreateItems(itemName, itemPrice)
            em.createitems()


def makePurchase():
    con = sqlite3.connect("items.sql")
    cur = con.cursor()
    print("Item Number | Item Name   | Item Cost")
    tes = "{0}           |{1} |   {2}"
    for row in cur.execute("SELECT * FROM itempage"):
        print(tes.format(row[0], row[1], row[2]))
    c = None
    while c != "no":
        print(f'would you like to make a purchase for the list ?, if yes input yes or \n'
              f'if no input no')
        c = input()
        if c == "no":
            break
        else:
            print("please enter the item iid of the object you'd like to buy")
            iid = int(input())
            print("please enter your employee iid")
            eid = int(input())
            makeapurchase(iid, eid)


def ShowAll():
    con = sqlite3.connect("test.sql")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM employee"):
        print(row)


run = {1: createItem,
       2: createEmployee,
       3: makePurchase,
       4: ShowAll}

print(f"———————————————\n"
      f"| {menu.get(1)}\n"
      f"| {menu.get(2)}\n"
      f"| {menu.get(3)}\n"
      f"| {menu.get(4)}\n"
      f"| {menu.get(5)}\n"
      f"———————————————")
a = 1
while a < 5:
    select = int(input())
    print(f"you have selected {menu.get(select)}")
    if select == 5:
        break
    run[select]()
print("The end")
