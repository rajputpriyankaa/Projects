import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

def student_registration():
    global std_win, student_name, roll_no, student_class, Father_name, address, mobile_no
    std_win = tkinter.Tk()
    std_win.title("Student registration")
    std_win.geometry('600x500')
    std_win.resizable(False,False)
    std_win.configure(bg = '#1e8e64')
    std_frame = Frame(std_win)
    std_frame.place(height=470, width=570, x=10, y=10)
    std_frame.config(bd=5, bg="#487978")
    std_frame.config(relief=SUNKEN)

    Label(std_win, text="Student's Name", font='Arial').place(x=20, y=80)
    student_name = Entry(std_win, font='Arial', bd = 5)
    student_name.place(x=200, y=80)

    Label(std_win, text='Roll No', font='Arial').place(x=20, y=130)
    roll_no = Entry(std_win, font='Arial',bd = 5)
    roll_no.place(x=200, y=130)

    Label(std_win, text='Class', font='Arial').place(x=20, y=180)
    student_class = Entry(std_win, font='Arial',bd = 5)
    student_class.place(x=200, y=180)

    Label(std_win, text="Father's Name", font='Arial').place(x=20, y=230)
    Father_name = Entry(std_win, font='Arial',bd = 5)
    Father_name.place(x=200, y=230)

    Label(std_win, text='Address', font='Arial').place(x=20, y=280)
    address = Entry(std_win, font='Arial',bd = 5)
    address.place(x=200, y=280)

    Label(std_win, text='Mobile no', font='Arial').place(x=20, y=330)
    mobile_no = Entry(std_win, font='Arial',bd = 5)
    mobile_no.place(x=200, y=330)

    Button(std_win, text='Facilities', font='Arial',bd = 5, command=facilities).place(x=50, y=400)
    Button(std_win, text='Register', font='Arial',bd = 5, command=ask_class).place(x=180, y=400)
    Button(std_win, text='Student details', font='Arial',bd = 5, command=search_student_details).place(x=300, y=400)
    Button(std_win, text='close', font='Arial',bd = 5, command=quit).place(x=450, y=400)

    std_win.mainloop()

def ask_class():
    global ask_student_class,ask
    ask = tkinter.Tk()
    ask.title("class?")
    ask.geometry('400x100')
    ask.configure(bg='#8b0020')
    Label(ask,text = 'Enter class', font=('Arial', 15, 'bold')).place(x=5,y=10)
    ask_student_class = Entry(ask,font=('Arial', 15, 'bold'))
    ask_student_class.place(x=150,y=10)
    Button(ask, text='Register', font=('Arial', 15, 'bold'),command = submit).place(x=100,y=50)
    ask.mainloop()

def submit():
    global student_name, roll_no, student_class, Father_name, address, mobile_no,ask_student_class
    ask_std_class=ask_student_class.get()
    std_name = student_name.get()
    std_roll_no = roll_no.get()
    std_class = student_class.get()
    std_father_name = Father_name.get()
    std_address = address.get()
    std_mobile = mobile_no.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    if ask_std_class == "bca" or ask_std_class == "BCA":
        mycursor.execute("insert into bca(Name,Roll_no,class,father_name,Address,Mobile_No) values(%s,%s,%s,%s,%s,%s) ",
                     (std_name, std_roll_no,std_class, std_father_name, std_address, std_mobile))
    elif ask_std_class == "mca" or ask_std_class == "MCA":
        mycursor.execute("insert into mca(Name,Roll_no,class,father_name,Address,Mobile_No) values(%s,%s,%s,%s,%s,%s) ",
            (std_name, std_roll_no, std_class, std_father_name, std_address, std_mobile))
    elif ask_std_class == "msc" or ask_std_class == "MSC":
        mycursor.execute("insert into msc(Name,Roll_no,class,father_name,Address,Mobile_No) values(%s,%s,%s,%s,%s,%s) ",
            (std_name, std_roll_no, std_class, std_father_name, std_address, std_mobile))
    elif ask_std_class == "mtech" or ask_std_class == "MTech":
        mycursor.execute("insert into mtech(Name,Roll_no,class,father_name,Address,Mobile_No) values(%s,%s,%s,%s,%s,%s) ",
            (std_name, std_roll_no, std_class, std_father_name, std_address, std_mobile))

    messagebox.showinfo("Registration", "student registered successfully")
    student_name.delete(0, END)
    roll_no.delete(0, END)
    student_class.delete(0, END)
    Father_name.delete(0, END)
    address.delete(0, END)
    mobile_no.delete(0,END)
    ask.destroy()
    mydb.commit()

def search_student_details():
    global std_window, std_window_frame, std_class,std_name
    std_window = Tk()
    std_window.title('Search Student details')
    std_window.geometry('700x400')
    std_window.resizable(False, False)
    std_window.configure(bg='#c10d3f')
    std_window_frame = Frame(std_window)
    std_window_frame.place(height=280, width=645, x=23, y=100)
    std_window_frame.config(bd=5, bg="#56943f")
    std_window_frame.config(relief=RIDGE)
    Label(std_window,text='Enter Class', font=('Arial', 15, 'bold')).place(x=20, y=20)
    Label(std_window,text='Enter Name', font=('Arial', 15, 'bold')).place(x=20, y=60)

    std_class = Entry(std_window, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    std_class.place(x=160, y=20)
    std_name = Entry(std_window, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    std_name.place(x=160,y=60)
    Button(std_window, text='Search', font=('Arial', 15, 'bold'), command=result_std_details).place(x=500, y=20)
    std_window.mainloop()

def result_std_details():
    global std_window, std_window_frame, std_class,std_name
    cls = std_class.get()
    nm = std_name.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    query = "select * from "+cls+" where Name ='"+ nm +"'"
    print(query)
    mycursor.execute(query)
    output = mycursor.fetchall()
    heading = ['Name','Roll No','Class','Father Name','Address','Mobile No']
    output.insert(0,heading)
    for nm in output:
        rows = len(output)
        columns = len(output[0])
        for i in range(rows):
            for j in range(columns):
                e = Entry(std_window_frame, bd=2, width=14, bg='#8fb9f8', font=('Arial', 10, 'bold'))
                if i==0:
                    e.configure(bg="#1005f8")
                e.grid(row=i, column=j)
                e.insert(END, output[i][j])
                std_name.delete(0, END)
                std_class.delete(0, END)


    if nm not in output:
        messagebox.showerror('Error!', 'Record does not exists😐')
        std_name.delete(0, END)
        std_class.delete(0, END)



def facilities():
    global std_win
    std_win.destroy()

def student_details_class():
    global std_class,class_choosen
    ask_std_class = tkinter.Tk()
    ask_std_class.title("class?")
    ask_std_class.geometry('400x100')
    ask_std_class.configure(bg='#8b0020')
    Label(ask_std_class,text = 'Enter class', font=('Arial', 15, 'bold')).place(x=5,y=10)
    a = StringVar()
    class_choosen = ttk.Combobox(ask_std_class, width=30, textvariable=a)
    class_choosen['values'] = ('BCA', 'MCA', 'MSC', 'MTech')
    class_choosen.place(x=150, y=10)
    class_choosen.current(1)
    Button(ask_std_class, text='show', font=('Arial', 15, 'bold'),command = student_details).place(x=100,y=50)
    ask_std_class.mainloop()

def student_details():
    global class_choosen,std_class
    choosen_class = class_choosen.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    if choosen_class == "MCA" or choosen_class == "mca":
        mycursor.execute('select * from mca')
    elif choosen_class == "BCA" or choosen_class == "bca":
        mycursor.execute('select * from bca')
    elif choosen_class == "MSC" or choosen_class == "msc":
        mycursor.execute('select * from msc')
    elif choosen_class == "MTech" or choosen_class == "mtech":
        mycursor.execute('select * from mtech')

    std_heading = ['Name', 'Roll no', 'Class','Father Name','Address', 'Mobile no']
    record = mycursor.fetchall()
    record.insert(0, std_heading)
    rows = len(record)
    columns = len(record[0])
    print(rows, columns)

    temp = Tk()
    temp.title("Student details")
    temp.geometry('1300x1300')
    f4 = Frame(temp)
    f4.place(height=650, width=1350, x=10, y=20)
    f4.config(bd=5, bg="#b38092")
    f4.config(relief=RIDGE)
    for i in range(rows):
        for j in range(columns):
            e = Entry(f4, bd=2, width=20, fg='blue', font=('Arial', 15, 'bold'))
            if i==0:
                e.configure(fg="black")
            e.grid(row=i, column=j)
            e.insert(END, record[i][j])

    temp.mainloop()

