from tkinter import *
from mysql import connector
import tkinter.messagebox as msg
root = Tk()
root.title("REGISTRATION FORM")
def database():
    conn=connector.connect(
        user='root',
        password='root',
        host='localhost',
        port='3306',
        database='registration_form')
    mycursor=conn.cursor()
    mycursor.execute("insert into registration values(%s,%s,%s,%s)",(name_entry.get(),rollno_entry.get(),var.get(),c.get()))
    conn.commit()
    msg.showinfo("Registration","Registed successfully")
registration_label =Label(root,text="REGISTRATION FORM", fg='Black',font=("bold",15))
registration_label.place(x=10,y=20)
name_label =Label(root,text="NAME", fg='Black')
name_label.place(x=15,y=60)
name_entry=Entry(root)
name_entry.place(x=70,y=60)
rollno_label=Label(root,text="ROLL_NO", fg='Black')
rollno_label.place(x=15,y=100)
rollno_entry=Entry(root)
rollno_entry.place(x=70,y=100)
gender_label =Label(root,text="GENDER", fg='Black').place(x=15,y=140)
var=StringVar()
r1=Radiobutton(root,text="Male",value=1,variable=var).place(x=70,y=138)
r2=Radiobutton(root,text="Female",value=2,variable=var).place(x=130,y=138)

branch_label =Label(root,text="BRANCH", fg='Black').place(x=15,y=180)
list_of_Branches=[ 'CSE' ,'ELECTRICAL' , 'CIVIL' ,'MECHANICAL' ,'AUTO MOBILE']
c=StringVar()
droplist=OptionMenu(root,c, *list_of_Branches)
droplist.config(width=15)
c.set('Select your Branch')
droplist.place(x=70,y=175)
b1=Button(root,text='login',fg='black',command=database)
b1.place(x=80,y=250)
root.mainloop()