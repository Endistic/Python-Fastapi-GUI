from turtle import width

import crud as crud
import json
import pandas as pd
import numpy as np
import test_crud as tc
from tkinter import *
from tkinter import ttk, messagebox

mainFrm = Tk()
mainFrm.title("-CRUD-")
ttk.Frame(mainFrm, height=410, width=430).pack()  # กำหนดขนาด frame
mainFrm.resizable(width=0, height=0)  # ขยายหน้าต่างไม่ได้


def clearEntryData():
    entName.delete(0, END)
    entAge.delete(0, END)
    entDetail.delete(0, END)


def SelectRowData():
    clearEntryData()
    item = viewSub.selection()
    for i in item:
        entName.insert("", viewSub.item(i, "values")[1])
        entAge.insert("", viewSub.item(i, "values")[2])
        entDetail.insert("", viewSub.item(i, "values")[3])


def showData():
    for c in viewSub.get_children():
        viewSub.delete(c)
    data = tc.fetch_user()
    data_user = data
    for d in data_user:
        viewSub.insert("", "end", values=(d['id'], d['name'], d['age'], d['info']))


def insert_data():
    if entName.get() == "" or entAge.get() == "" or entDetail.get() == "":
        print("Error Input")
    else:
        print(entName.get())
        print(entAge.get())
        print(entDetail.get())
        tc.create_user(entName.get(), entAge.get(), entDetail.get())
        clearEntryData()
        showData()


def delete_data():
    if not viewSub.selection():
        print("Please Select Data")
    else:
        item = viewSub.selection()
        item_id = ''
        for i in item:
            item_id = viewSub.item(i, 'values')[0]
        tc.delete_user(item_id)
        clearEntryData()
        showData()


def update_data():
    if not viewSub.selection():
        print('Select !')
    else:
        item = viewSub.selection()
        item_id = ''
        for i in item:
            item_id = viewSub.item(i, 'values')[0]
        tc.edit_user(item_id, entName.get(), entAge.get(), entDetail.get())
        clearEntryData()
        showData()


viewSub = ttk.Treeview(mainFrm, columns=("id", "name", "age", "detail"), show="headings", selectmode="extended")
viewSub.place(height=200, width=410, x=10, y=200)

sc = ttk.Scrollbar(mainFrm, orient="vertical", command=viewSub.yview)
sc.place(height=200, x=500, y=200)
viewSub.configure(yscrollcommand=sc.set)

viewSub.column("#1", width=30)
viewSub.column("#2", width=50)
viewSub.column("#3", width=30)
viewSub.column("#4", width=150)

viewSub.heading("id", text="ID")
viewSub.heading("name", text="Name")
viewSub.heading("age", text="Age")
viewSub.heading("detail", text="Detail")

ttk.LabelFrame(mainFrm, text="Test").place(height=130, width=300, x=10, y=10)
ttk.Label(mainFrm, text="Name : ").place(height=20, width=50, x=20, y=40)
ttk.Label(mainFrm, text="Age : ").place(height=20, width=50, x=20, y=70)
ttk.Label(mainFrm, text="Detail : ").place(height=20, width=50, x=20, y=100)

entStyle = ttk.Style()
entName = ttk.Entry(mainFrm)
entAge = ttk.Entry(mainFrm)
entDetail = ttk.Entry(mainFrm)

entName.place(height=25, width=150, x=110, y=40)
entAge.place(height=25, width=150, x=110, y=70)
entDetail.place(height=25, width=150, x=110, y=100)

btnStyle = ttk.Style()
btnStyle.configure("btnSave.TButton", font=("Time", "10", "bold"))
btnStyle.configure("btnEdit.TButton", font=("Time", "10", "bold"))
btnStyle.configure("btnDelete.TButton", font=("Time", "10", "bold"))
btnStyle.configure("btnClear.TButton", font=("Time", "10", "bold"))
btnStyle.configure("btnExit.TButton", font=("Time", "10", "bold"))

btnSave = ttk.Button(mainFrm, text="Save", style="btnSave.TButton", command=insert_data)
btnEdit = ttk.Button(mainFrm, text="Edit", style="btnEdit.TButton", command=update_data)
btnDelete = ttk.Button(mainFrm, text="Delete", style="btnDelete.TButton", command=delete_data)
btnCancel = ttk.Button(mainFrm, text="Clear", style="btnClear.TButton", command=clearEntryData)
btnExit = ttk.Button(mainFrm, text="Exit", style="btnExit.TButton", command=mainFrm.destroy)

btnSave.place(height=35, width=100, x=320, y=20)
btnEdit.place(height=35, width=100, x=320, y=55)
btnDelete.place(height=35, width=100, x=320, y=90)
btnCancel.place(height=35, width=100, x=320, y=125)
btnExit.place(height=35, width=100, x=320, y=160)

###########################################################################################################
mainFrm.mainloop()
