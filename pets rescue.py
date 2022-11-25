import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("Petsrescue.db")
import time
from tkinter import ttk
#from tkcalendar import Calendar, DateEntry
from datetime import datetime
import sqlite3
import webbrowser
root = Tk()
root.title("Pets Rescue")
root.geometry("1240x615+100+100")
root.resizable(False,False)
root.configure(bg='#F3F7AE')
root.iconbitmap('D:\\python\\pythonproject\\test1\\pets.ico')

#clinicname,doctorname,city,area,pagelink,mobile,address
clinicname = StringVar()
doctorname = StringVar()
city = StringVar()
area = StringVar()
pagelink = StringVar()
mobile = StringVar()
search_by = StringVar()
search_var = StringVar()
logo = PhotoImage(file='logo.PNG')
lbllogo =Label(root,image=logo,bg='#F3F7AE')
lbllogo.place(x=70,y=455)

#****************************انشاء نافذة للبرنامج*****************
entries_frame=Frame(root,bg='#F3F7AE')
entries_frame.place(x=1,y=1,width=390,height=510)
title= Label(entries_frame,text="Pets Rescue",font=("Calibri",20,"bold"),bg="#F3F7AE",fg="#6A6A61")
title.place(x=10,y=1)

lblclinicname=Label(entries_frame,text="Clinic Name",font=("Calibri",14,'bold'),bg="#F3F7AE",fg="#979787")
lblclinicname.place(x=10,y=50)
textclinicname=Entry(entries_frame,textvariable=clinicname,width=20,font=("Calibri",14))
textclinicname.place(x=120,y=50)
lbldoctorname=Label(entries_frame,text="Doctor Name",font=("Calibri",14,'bold'),bg="#F3F7AE",fg="#979787")
lbldoctorname.place(x=10,y=90)
textdoctorname=Entry(entries_frame,textvariable=doctorname,width=20,font=("Calibri",14))
textdoctorname.place(x=120,y=90)

lblcity=Label(entries_frame,text="City",font=("Calibri",14,'bold'),bg="#F3F7AE",fg="#979787")
lblcity.place(x=10,y=130)
combocity = ttk.Combobox(entries_frame,textvariable=city,state="readonly",width=18,font=("Calibri",14))
combocity['values']=('Cairo','Giza','Alex')
combocity.place(x=120,y=130)

lblarea=Label(entries_frame,text="Area",font=("Calibri",14,'bold'),bg="#F3F7AE",fg="#979787")
lblarea.place(x=10,y=170)
textarea=Entry(entries_frame,textvariable=area,width=20,font=("Calibri",14))
textarea.place(x=120,y=170)

lblpagelink=Label(entries_frame,text="Page Link",font=("Calibri",14,'bold'),bg="#F3F7AE",fg="#979787")
lblpagelink.place(x=10,y=210)
textpagelink=Entry(entries_frame,textvariable=pagelink,width=20,font=("Calibri",14))
textpagelink.place(x=120,y=210)

lblmobile=Label(entries_frame,text="Mobile",font=("Calibri",14,'bold'),bg="#F3F7AE",fg="#979787")
lblmobile.place(x=10,y=250)
textmobile=Entry(entries_frame,textvariable=mobile,width=20,font=("Calibri",14))
textmobile.place(x=120,y=250)

lbladdress=Label(entries_frame,text="Address:",font=("Calibri",16,'bold'),bg="#F3F7AE",fg="#979787")
lbladdress.place(x=10,y=290)
textaddress=Text(entries_frame,width=30,height=2,font=("Calibri",16),relief=RIDGE,bd=2)
textaddress.place(x=10,y=330)
#****************************define *****************
def hide():
    root.geometry("360x510")
def show():
    root.geometry("1240x615+100+100")
btnhide=Button(entries_frame,text='Hide',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btnhide.place(x=270,y=10)
btnshow=Button(entries_frame,text='Show',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnshow.place(x=310,y=10)


def getdata(ev):
    selected_row = tv.focus()
    data=tv.item(selected_row)
    global row
    row = data["values"]
    clinicname.set(row[1])
    doctorname.set(row[2])
    city.set(row[3])
    area.set(row[4])
    pagelink.set(row[5])
    mobile.set(row[6])
    textaddress.delete(1.0,END)
    textaddress.insert(END,row[7])
def dispalyall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def update():
    if textclinicname.get() == "" or textdoctorname.get() == "" or combocity.get() == "" or textarea.get() == "" or textpagelink.get() == "" or textmobile.get() == "" or textaddress.get(
            1.0, END) == "":
        messagebox.showerror("error", "please fill all the entry")
        return
    db.update(row[0],
              textclinicname.get(),
              textdoctorname.get(),
              combocity.get(),
              textarea.get(),
              textpagelink.get(),
              textmobile.get(),
              textaddress.get(1.0, END))
    messagebox.showinfo("success", "the data was updated")
    clear()
    dispalyall()

def delete():
    db.remove(row[0])
    clear()
    dispalyall()
def clear():
    clinicname.set("")
    doctorname.set("")
    city.set("")
    area.set("")
    pagelink.set("")
    mobile.set("")
    textaddress.delete(1.0,END)

def add_employee():
    if textclinicname.get()=="" or textdoctorname.get()=="" or combocity.get()=="" or textarea.get()=="" or textpagelink.get()=="" or  textmobile.get()=="" or textaddress.get(1.0,END)=="":
        messagebox.showerror("error","please fill all the entry")
        return
    db.insert(textclinicname.get(),
              textdoctorname.get(),
              combocity.get(),
              textarea.get(),
              textpagelink.get(),
              textmobile.get(),
              textaddress.get(1.0,END))
    messagebox.showinfo("success","added new clinic")
    clear()
    dispalyall()


def search():
    con = sqlite3.connect('Petsrescue.db')
    cur = con.cursor()
    cur.execute("select * from PetsRescue where " + str(search_by.get())+" LIKE '%"+str(search_var.get())+"%'")
    rows = cur.fetchall()
    if len(rows) != 0:
        tv.delete(*tv.get_children())
        for row in rows:
            tv.insert("", END, values=row)
            con.commit()
    con.close()
def about():
    messagebox.showinfo("developer Amal Ismail","Welcome to our program")
    messagebox.showinfo("Linkedin Account","https://www.linkedin.com/in/amal-ismail-09310729/")
about_btn = Button(entries_frame, text='About Us',bg='white',bd=1,relief=SOLID,cursor='hand2',command=about)
about_btn.place(x=205,y=10)


#****************************ازرار البرنامج *****************
btn_frame=Frame(entries_frame,bg="#F3F7AE",bd=1,relief=RIDGE)
btn_frame.place(x=10,y=400,width=335,height=100)

btnadd=Button(btn_frame,text="Add Details",width=14,height=1,font=("Calibri",16,'bold'),fg="#6A6A61",bg="silver",bd=0,command=add_employee).place(x=4,y=5)
btnupdate=Button(btn_frame,text="Update Details",width=14,height=1,font=("Calibri",16,'bold'),fg="#6A6A61",bg="silver",bd=0,command=update).place(x=4,y=50)
btndell=Button(btn_frame,text="Delete Details",width=14,height=1,font=("Calibri",16,'bold'),fg="#6A6A61",bg="silver",bd=0,command=delete).place(x=170,y=5)
btnclear=Button(btn_frame,text="Clear Details",width=14,height=1,font=("Calibri",16,'bold'),fg="#6A6A61",bg="silver",bd=0,command=clear).place(x=170,y=50)



#****************************table frame *****************
tree_frame=Frame(root,bg='#F3F7AE',relief=RIDGE,bd=2)
tree_frame.place(x=360,y=1,width=875,height=610)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview",font=('Calibri',13))

#****************************table frame *****************

Scroll_X = Scrollbar(tree_frame, orient=HORIZONTAL)
Scroll_Y = Scrollbar(tree_frame, orient=VERTICAL)
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),xscrollcommand=Scroll_X.set,yscrollcommand=Scroll_Y.set,style="mystyle.Treeview")
Scroll_X.pack(side=BOTTOM,fill=X)
Scroll_Y.pack(side=RIGHT,fill=Y)
Scroll_X.configure(command=tv.xview)
Scroll_Y.configure(command=tv.yview)
tv.heading("1",text="ID")
tv.column("1",width="40")

tv.heading("2",text="Clinic Name")
tv.column("2",width="140")

tv.heading("3",text="Doctor Name")
tv.column("3",width="120")

tv.heading("4",text="City")
tv.column("4",width="50")

tv.heading("5",text="Area")
tv.column("5",width="90")

tv.heading("6",text="Page Link")
tv.column("6",width="150")

tv.heading("7",text="Mobile")
tv.column("7",width="110")

tv.heading("8",text="Address")
tv.column("8",width="190")

tv['show']='headings'


tv.bind("<ButtonRelease-1>",getdata)
tv.place(x=10,y=110,height=480,width=845)
#****************************نظام البحث  *****************
Search_Frame = Frame(root,bg='white',relief=RIDGE,bd=3)
Search_Frame.place(x=370,y=30,width=845,height=60)
lbl_Search=Label(Search_Frame,text='Search Data',bg='White')
lbl_Search.place(x=580,y=20)
combo_Search = ttk.Combobox(Search_Frame,textvariable=search_by,justify='right',state='readonly')
combo_Search['value']=('ClinicName','DoctorName','City','Area')
combo_Search.place(x=430,y=20)
entry_Search=Entry(Search_Frame,textvariable= search_var,justify='right',bd=2,relief=GROOVE)
entry_Search.place(x=300,y=20)
Search_btn = Button(Search_Frame,text='Search',bg='#DADDDE',command=search)
Search_btn.place(x=210,y=20,width=100,height=20)
#*********************date-time************************************
filter_date_frm=LabelFrame(Search_Frame,width=830,height=60,bg='green',bd=3,font=('Arial',9,'bold'))
filter_date_frm.place(x=10,y=140)
app_date=datetime.now()
x_date=app_date.strftime('%d-%m-%y')
def app_time():
    string=time.strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000,app_time)
time_label=Label(Search_Frame,bg='white',fg='black',font=('Arial',9,'bold'))
time_label.place(x=710,y=20)
app_time()
date_label=Label(Search_Frame,text=x_date,bg='silver',fg='black',font=('Arial',10,'bold'))
date_label.place(x=70,y=20)
#***********************************************************




dispalyall()
root.mainloop()
