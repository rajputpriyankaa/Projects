from tkinter import *
import mysql.connector
from tkinter import messagebox

def login():
    global  login_mail,login_password,var
    win = Tk()
    win.title('Login page')
    win.geometry('1200x600')
    win.configure(bg='#b30d36')
    win.resizable(False,False)

    bg = PhotoImage(file=r"C:\Users\Admin\Downloads\image.png")
    canvas1 = Canvas(win, width=400, height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    f1 = Frame(win)
    f1.place(height=500, width=400, x=400, y=50)
    f1.config(bd=5, bg='#e77e89')
    f1.config(relief=RIDGE)
    Label(f1, text='Email ID', font=('Arial', 20, 'bold')).place(x=40, y=20)
    login_mail = Entry(f1, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    login_mail.place(x=40, y=70)

    Label(f1, text='Password', font=('Arial', 20, 'bold')).place(x=40, y=120)
    login_password = Entry(f1, font=('Arial', 15, 'bold'), fg = 'red', bd='2',show="*")
    login_password.place(x=40, y=170)

    var=IntVar()
    bt = Checkbutton(f1,command=show,offvalue=0,onvalue=1,variable=var)
    bt.place(x=300, y=175)
    Button(f1, text='Cancel', font=('Arial', 20, 'bold','underline'), command=exit).place(x=40, y=220)
    Button(f1, text='Login', font=('Arial', 20, 'bold','underline'),command=access).place(x=200, y=220)
    Button(f1, text='create a new account', font=('Arial', 15, 'italic','underline'),fg ="red", command=exit).place(x=40, y=300)
    win.mainloop()

def show():
    global var,login_password
    if var.get()==0:
        login_password.configure(show="*")
    elif var.get()==1:
        login_password.configure(show="")

def access():
    global login_mail,login_password
    email = login_mail.get()
    password = login_password.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="student"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select emailid, password from students")
    data = mycursor.fetchall()
    for i,j in data:
        if email == i and password == j:
            messagebox.showinfo("success!","login successfully☺")
            break
    else:
        messagebox.showerror("failure!","login not successful☹")
        login_mail.delete(0,END)
        login_password.delete(0,END)


login()