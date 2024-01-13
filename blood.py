import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import pymysql

from tkinter import *
from PIL import Image,ImageTk



def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['BD_ID'])
    e2.insert(0, select['BD_NAME'])
    e3.insert(0, select['BD_AGE'])
    e4.insert(0, select['BD_SEX'])
    e5.insert(0, select['BD_BGROUP'])
    e6.insert(0, select['CITY_ID'])
    e7.insert(0, select['RECI_ID'])
    e8.insert(0, select['RECI_NAME'])
    e9.insert(0, select['RECI_AGE'])
    e10.insert(0, select['RECI_SEX'])
    e11.insert(0, select['RECI_BRGP'])
    e12.insert(0, select['RECI_BQNTY'])
    e13.insert(0, select['CITY_ID'])


def Add():
    BD_ID= e1.get()
    BD_NAME= e2.get()
    BD_AGE= e3.get()
    BD_SEX = e4.get()
    BD_BGROUP=e5.get()
    CITY_ID=e6.get()
    RECI_ID=e7.get()
    RECI_NAME=e8.get()
    RECI_AGE=e9.get()
    RECI_SEX=e10.get()
    RECI_BRGP=e11.get()
    RECI_BQNTY=e12.get()



    mysqldb = pymysql.connect(host="localhost", user="root", password="Nish@562003", database="Bloodbank")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  Blood_Donor (BD_ID,BD_NAME,BD_AGE,BD_SEX,BD_BGROUP,CITY_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (BD_ID,BD_NAME,BD_AGE,BD_SEX,BD_BGROUP,CITY_ID)
        sql1 = "INSERT INTO  Recipient(RECI_ID,RECI_NAME,RECI_AGE,RECI_SEX,RECI_BRGP,RECI_BQNTY,CITY_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val1 = (RECI_ID,RECI_NAME,RECI_AGE,RECI_SEX,RECI_BRGP,RECI_BQNTY,CITY_ID)
        
        mycursor.execute(sql, val)
        mysqldb.commit()
        mycursor.execute(sql1, val1)
        mysqldb.commit()


        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)

        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = pymysql.connect(host="localhost", user="root", password="Nish@562003", database="Bloodbank")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT BD_ID,BD_NAME,BD_AGE,BD_SEX,BD_BGROUP,CITY_ID FROM Blood_Donor")
    records = mycursor.fetchall()
    print(records)
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT RECI_ID,RECI_NAME,RECI_AGE,RECI_SEX,RECI_BRGP,RECI_BQNTY,CITY_ID FROM Recipient")
    record = mycursor.fetchall()
    print(record)
    

    for i, (BD_ID,BD_NAME,BD_AGE,BD_SEX,BD_BGROUP,CITY_ID) in enumerate(records, start=1):
        listBox.insert("", "end", values=(BD_ID,BD_NAME,BD_AGE,BD_SEX,BD_BGROUP,CITY_ID))

    for i, (RECI_ID,RECI_NAME,RECI_AGE,RECI_SEX,RECI_BRGP,RECI_BQNTY,CITY_ID) in enumerate(record, start=1):
        listBox.insert("", "end", values=(RECI_ID,RECI_NAME,RECI_AGE,RECI_SEX,RECI_BRGP,RECI_BQNTY,CITY_ID))



root = Tk()
root.geometry("2000x2000")
image=Image.open("C:\\Users\\NISH\\OneDrive\\Desktop\\BLOOD BANK MANAGEMENT SYSTEM\\blood.png")
back=ImageTk.PhotoImage(image)
l1=Label(root,image=back).place(x=0,y=0)

global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global e9
global e10
global e11
global e12
global e13




tk.Label(root, text="BLOOD BANK MANAGEMENT SYSTEM", fg="red", font=(None, 30)).place(x=300, y=5)
##personal data table
Label(root,text="Donor Information",fg="blue",font="arial 30").place(x=10,y=70)
tk.Label(root, text="Donor ID",font="20").place(x=10, y=140)
Label(root, text="Name",font="20").place(x=10, y=180)
Label(root, text="Age",font="20").place(x=10, y=220)
Label(root, text="Sexuality ",font="20").place(x=10, y=260)
Label(root, text="Blood group",font="20").place(x=10, y=300)
Label(root, text="City",font="20").place(x=10, y=340)


e1 = Entry(root)
e1.place(x=170, y=140)

e2 = Entry(root)
e2.place(x=170, y=180)

e3 = Entry(root)
e3.place(x=170, y=220)

e4 = Entry(root)
e4.place(x=170, y=260)

e5 = Entry(root)
e5.place(x=170, y=300)

e6 = Entry(root)
e6.place(x=170, y=340)


Button(root, text="Submit", command=Add, height=3, width=13).place(x=500, y=500)




Label(root,text="Receiver Information",fg="blue",font="arial 30").place(x=800,y=70)
tk.Label(root, text="Receiver Id",font="20").place(x=800, y=140)
Label(root, text="Name",font="20").place(x=800, y=180)
Label(root, text="Age",font="20").place(x=800, y=220)
Label(root, text="Sexuality",font="20").place(x=800, y=260)
Label(root, text="Blood group",font="20").place(x=800, y=300)
Label(root, text="Blood quantity",font="20").place(x=800, y=340)
Label(root, text="City",font="20").place(x=800, y=380)

e7 = Entry(root)
e7.place(x=1000, y=140)

e8 = Entry(root)
e8.place(x=1000, y=180)

e9 = Entry(root)
e9.place(x=1000, y=220)

e10 = Entry(root)
e10.place(x=1000, y=260)

e11 = Entry(root)
e11.place(x=1000, y=300)

e12 = Entry(root)
e12.place(x=1000, y=340)

e6 = Entry(root)
e6.place(x=1000, y=380)

"""cols = ('BD_ID','BD_NAME','BD_AGE','BD_SEX','BD_BGROUP','CITY_ID','RECI_ID','RECI_NAME','RECI_AGE','RECI_SEX','RECI_BRGP','RECI_BQNTY','CITY_ID')
listBox = ttk.Treeview(root, columns=cols, show='headings')


for col in cols:

    listBox.heading(col, text=col)
    listBox.grid(row=0, column=0)
    listBox.place(x=10, y=500)

show()
listBox.bind('<Double-Button-1>', GetValue)"""

root.mainloop()