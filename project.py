import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql.cursors
import re
from tkinter import scrolledtext
from prettytable import from_db_cursor

window=Tk()
window.geometry("1200x1200")
window.title("welcome")


db=pymysql.connect("localhost","root","","project")
cursor=db.cursor()

def valid():
     global value
     value=1
     
     p=entry1.get()
     if(len(p)==0):
         messagebox.showwarning("welcome","ENTER FIRST NAME")
         value=0
         
     p=entry2.get()
     if(len(p)==0):
        messagebox.showwarning("welcome","ENTER LAST NAME")
        value=0

     p=entry4.get()
     if(len(p)!=10):
        messagebox.showwarning("welcome","ENTER 10 DIGITD CONTACT NUMBER")
        value=0

     if(value==1):
        database()
    

    

def database():

    firstname=entry1.get()
    lastname=entry2.get()
    studentId=entry3.get()
    gender=variable.get()
    date=u.get() 
    month=v.get()
    year=w.get()
    contact=entry4.get()
    emailid=entry5.get()
    rollno=r.get()
    address=T.get("1.0","end-1c")

    sql="INSERT INTO sample4(firstname,lastname,studentId,gender,date,month,year,contact,emailid,rollno,address)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vari=(firstname,lastname,studentId,gender,date,month,year,contact,emailid,rollno,address)
    cursor.execute(sql,vari)
    db.commit()
    db.close


def display():

    window1=Tk()
    window1.geometry("1500x1500")
    window1.configure(bg="white")
    window1.title("DATA")
    e=Text(window1)
    e.place(x=0,y=0,width=2000,height=700)
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM sample4")
    x=from_db_cursor(mycursor)
    e.insert(INSERT,x)
    


    

#LABELS AND ENTRY

label=Label(window,text="STUDENT MANAGEMENT SYSTEM",relief="solid",width=30,fg="white",bg="#0a6ca8",font=" Times 30 bold",)
label.place(x=360,y=60)


label1=Label(window,text="ENTER FIRST NAME",width=20,fg="black",bg="white",font="bold")
label1.place(x=400,y=160)

entry1=Entry(window,width=50)
entry1.place(x=650,y=163)

label2=Label(window,text="ENTER LAST NAME",width=20,fg="black",bg="white",font="bold")
label2.place(x=400,y=200)

entry2=Entry(window,width=50)
entry2.place(x=650,y=205)

label3=Label(window,text="STUDENT ID",width=20,fg="black",bg="white",font="bold")
label3.place(x=400,y=240)

entry3=Entry(window,width=50)
entry3.place(x=650,y=243)

label4=Label(window,text="GENDER",width=20,fg="black",bg="white",font="bold")
label4.place(x=400,y=280)

choices={"Female","Male"}
variable=StringVar(window)
variable.set("select")

p=OptionMenu(window,variable,*choices)
p.place(x=650,y=280)


label5=Label(window,text="DATE OF BIRTH",width=20,fg="black",bg="white",font="bold")
label5.place(x=400,y=320)

#SPINBOX

u=Spinbox(window, from_=1,to=31,width=5)
u.place(x=650,y=323)

v=Spinbox(window, from_=1,to=12,width=5)
v.place(x=700,y=323)

w=Spinbox(window, from_=1972,to=2019,width=7)
w.place(x=750,y=323)

label6=Label(window,text="CONTACT NO.",width=20,fg="black",bg="white",font="bold")
label6.place(x=400,y=360)

entry4=Entry(window,width=50)
entry4.place(x=650,y=360)

label7=Label(window,text="EMAIL",width=20,fg="black",bg="white",font="bold")
label7.place(x=400,y=400)

entry5=Entry(window,width=50)
entry5.place(x=650,y=400)

label8=Label(window,text="ROLL NO.",width=20,fg="black",bg="white",font="bold")
label8.place(x=400,y=440)

r=Spinbox(window, from_=0,to=100,width=5)
r.place(x=650,y=443)


label9=Label(window,text="ADDRESS",width=20,fg="black",bg="white",font="bold")
label9.place(x=400,y=480)

#TEXTBOX
T =Text(window,height=3,width=40)
T.place(x=650,y=480)

#BUTTON
b1=Button(window,text="SUBMIT",width=12,bg="#de1414",fg="white",command=valid,font=" Times 15 bold")
b1.place(x=650,y=550)

b2=Button(window,text="DISPLAY",width=12,bg="#de1414",fg="white",command=display,font=" Times 15 bold")
b2.place(x=850,y=550)




window.config(bg="light blue")
window.mainloop()






