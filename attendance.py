import mysql.connector
from faculty import *
from student import *
from take_attendance import *
from PIL import ImageTk, Image
import csv

def facility():

    global login_name, login_password, win,name
    name = login_name.get()
    password = login_password.get()
    filename = "login.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(name)
    print(name,password)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from login_details")
    record = mycursor.fetchall()
    print(record)
    for i,j in record:
        if name == i and password == j:
            win.destroy()
            root = Tk()
            root.title('Facilities')
            root.geometry('600x400')
            root.configure(bg = '#8b86b3')
            root.resizable(False, False)
            p1 = PhotoImage(file='gju_logo.png')
            root.iconphoto(False, p1)
            Facilities_frame = Frame(root)
            Facilities_frame.place(height=370, width=570, x=10, y=10)
            Facilities_frame.config(bd=5,bg = '#b30d36')
            Facilities_frame.config(relief=RIDGE)

            # bg = PhotoImage(file="background.png")
            # label1 = Label(root, image=bg, width=600, height=600)
            # label1.place(x=0, y=0)
            Label(root, text=("welcome "+name+"..."),fg="#4c4bd3", font=('Arial', 15, 'bold')).place(x=40, y=20)
            Button(root, text='Faculty Registration', font=('Arial', 15, 'bold'), command=faculty_registration).place(x=80, y=80)
            Button(root, text='Faculty Details', font=('Arial', 15, 'bold'), command=faculty_details).place(x=350, y=80)
            Button(root, text='Student Registration', font=('Arial', 15, 'bold'), command=student_registration).place(x=80, y=160)
            Button(root, text='Student Details', font=('Arial', 15, 'bold'), command=student_details_class).place(x=350, y=160)
            Button(root, text='Take Attendance', font=('Arial', 15, 'bold'), command=attendance_interface).place(x=200, y=240)
            Button(root, text='Close', font=('Arial', 15, 'bold'), command=exit).place(x=250, y=300)
            root.mainloop()
            break
    else:
        messagebox.showinfo("warning","wrong login credentials!")
        login_name.delete(0, END)
        login_password.delete(0, END)

def new_account():
    global user_name,user_password,new_acc_win,var1
    new_acc_win = tkinter.Toplevel()
    new_acc_win.title('create a new account')
    new_acc_win.geometry('400x400')
    new_acc_win.configure(bg='#b30d36')
    frame = Frame(new_acc_win)
    frame.place(height=370, width=370, x=10, y=10)
    frame.config(bd=5, bg='#1e8e64')
    frame.config(relief=SUNKEN)
    Label(frame, text='User name', font=('Arial', 20, 'bold')).place(x=40, y=20)
    user_name = Entry(frame, font=('Arial', 20, 'bold'), fg='red', bd='2')
    user_name.place(x=40, y=70)

    Label(frame, text='Password', font=('Arial', 20, 'bold')).place(x=40, y=120)
    user_password = Entry(frame, font=('Arial', 20, 'bold'), fg='red', bd='2',show="*")
    user_password.place(x=40, y=170)

    var1 = IntVar()
    bt1 = Checkbutton(frame, command=show1, offvalue=0, onvalue=1, variable=var1)
    bt1.place(x=300, y=175)
    Button(frame, text='Create', font=('Arial', 20, 'italic'), command=new_login).place(x=50, y=220)
    Button(frame, text='Delete', font=('Arial', 20, 'italic'), command=delete).place(x=200, y=220)
    Button(frame, text='Exit', font=('Arial', 20, 'bold','underline'), command=exit).place(x=120, y=300)

    new_acc_win.mainloop()

def show1():
    global var1 ,user_password
    if var1.get()==0:
        user_password.configure(show="*")
    elif var1.get()==1:
        user_password.configure(show="")

def new_login():
    global user_name,user_password,new_acc_win
    new_user_name = user_name.get()
    new_user_password = user_password.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from login_details")
    record = mycursor.fetchall()
    for i,j in record:
        if new_user_name==i and new_user_password==j:
            messagebox.showerror("error","account already exists")
            user_name.delete(0,END)
            user_password.delete(0,END)
            break

    if user_name and user_password!='':
        mycursor.execute("insert into login_details(user_name,user_password) values(%s,%s)",(new_user_name,new_user_password))
        mydb.commit()
        messagebox.showinfo("Message","Account created successfully")
        user_name.delete(0,END)
        user_password.delete(0,END)
        new_acc_win.withdraw()
        faculty_registration()
    else:
        messagebox.showerror("error","please enter complete details")

def delete():
    global user_name,user_password
    user_name.delete(0,END)
    user_password.delete(0,END)

def main_interface():
    global win, login_name, login_password,new_acc_win,var
    win = Tk()
    win.title('Login page')
    win.geometry('600x600')
    win.configure(bg = '#b30d36')
    p1 = PhotoImage(file='gju_logo.png')
    win.iconphoto(False, p1)
    image1 = Image.open("gju_logo.png")
    image1 = image1.resize((150, 150), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=220, y=25)
    win.resizable(False,False)


    f1 = Frame(win)
    f1.place(height=370, width=400, x=100, y=200)
    f1.config(bd=5, bg = '#430d79')
    f1.config(relief=RIDGE)

    Label(f1, text='User name', font=('Arial', 20, 'bold')).place(x=40, y=20)
    login_name = Entry(f1, font=('Arial', 20, 'bold'), fg = 'red', bd='2')
    login_name.place(x=40, y=70)

    Label(f1, text='Password', font=('Arial', 20, 'bold')).place(x=40, y=120)
    login_password = Entry(f1, font=('Arial', 20, 'bold'), fg = 'red', bd='2',show="*")
    login_password.place(x=40, y=170)

    var=IntVar()
    bt = Checkbutton(f1,command=show,offvalue=0,onvalue=1,variable=var)
    bt.place(x=300, y=175)
    Button(f1, text='Cancel', font=('Arial', 20, 'bold','underline'), command=exit).place(x=40, y=220)
    Button(f1, text='Login', font=('Arial', 20, 'bold','underline'),command=facility).place(x=200, y=220)
    Button(f1, text='create a new account', font=('Arial', 15, 'italic','underline'),fg ="red", command=new_account).place(x=40, y=300)

    win.mainloop()

def show():
    global var,login_password
    if var.get()==0:
        login_password.configure(show="*")
    elif var.get()==1:
        login_password.configure(show="")


main_interface()

