from tkinter import *
from tkinter import ttk

window = Tk()


def km_to_miles():
    miles = float(b2_value.get()) * 1.6
    print(miles)
    b3.insert(END, miles)


b1 = Button(window, text='execute', command=km_to_miles)
b1.grid(row=0, column=0)

b2_value = StringVar()
b2 = Entry(window, textvariable=b2_value)
b2.grid(row=0, column=1)

b3 = Text(window, height=1, width=20)
b3.grid(row=0, column=2)

window.mainloop()
