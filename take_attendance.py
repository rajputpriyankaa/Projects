import tkinter
from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import Calendar
import mysql.connector
import csv
import copy

def attendance_interface():
    global semchoosen, deptchoosen, cal,date,att_faculty
    filename = "login.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        join_name = list(csvreader)
        # for row in csvreader:
        #     print(row)
        #     join_name = "".join(row)

    print(join_name)
    att_faculty = "".join(join_name[0])
    print(att_faculty)
    attendance_calender = tkinter.Tk()
    attendance_calender.title("Attendance")
    attendance_calender.geometry("600x500")
    attendance_calender.configure(bg = "#1e8e64")
    Label(attendance_calender, text = "Take Attendance", font=('Arial', 20, 'bold')).place(x=150, y=20)

    Label(attendance_calender, text = "Department", font=('Arial', 15, 'bold')).place(x=20, y=300)
    n = StringVar()
    deptchoosen = ttk.Combobox(attendance_calender, width=30, textvariable=n)
    deptchoosen['values'] = ('BCA', 'MCA', 'MSC', 'MTech')
    deptchoosen.place(x=200, y=310)
    deptchoosen.current(1)

    Label(attendance_calender,text = "Semester", font=('Arial', 15, 'bold')).place(x=20, y=350)
    a = StringVar()
    semchoosen = ttk.Combobox(attendance_calender, width=30, textvariable=a)
    semchoosen['values'] = ('FIRST', 'SECOND', 'THIRD', 'FOURTH')
    semchoosen.place(x=200, y=360)
    semchoosen.current(3)

    Button(attendance_calender, text='Back', font='Arial',bd = 5, command=attendance_calender.destroy).place(x=50, y=420)
    Button(attendance_calender, text='Close', font='Arial',bd = 5, command=quit).place(x=200, y=420)
    Button(attendance_calender, text='Next', font='Arial',bd = 5, command=choice).place(x=350, y=420)

    cal = Calendar(attendance_calender, selectmode='day', year=2021, month=6, day=22)

    #cal.pack(pady=20)
    cal.place(x = 300, y = 100)
    def selected_data():
        date.config(text="" + cal.get_date())

    Button(attendance_calender, text="Get Date", command=selected_data).place(x=50, y=100)
    date = Label(attendance_calender, text="")
    date.place(x = 50, y = 150)
    attendance_calender.mainloop()

def choice():
    global semchoosen,sem_choice,choice_window, deptchoosen,cal,date, output,absent,present,a,b,c,d,data,choice_date,dept_choice,mycursor,att_faculty,fac_name
    sem_choice = semchoosen.get()
    dept_choice = deptchoosen.get()
    choice_date = date.cget("text")
    choice_window = tkinter.Tk()
    choice_window.title("Attendance register")
    choice_window.geometry("400x500")
    choice_window.configure(bg='#8b0012')
    choice_window.resizable(False,False)
    fac_name = Label(choice_window,text='Faculty:'+att_faculty, font=('Arial', 15, 'bold'))
    fac_name.place(x=5, y=60)
    Label(choice_window,text='Attendance Register', font=('Arial', 15, 'bold')).place(x=180, y=60)
    Label(choice_window,text=choice_date, font=('Arial', 10, 'bold')).place(x=5, y=10)
    Button(choice_window,text='Total', font=('Arial', 10, 'bold'),command = total_attendance).place(x=300, y=120)
    data = sem_choice+" "+dept_choice
    Label(choice_window,text=data,font=('Arial', 10, 'bold')).place(x=270, y=10)
    Label(choice_window,text='P', font=('Arial', 15, 'bold')).place(x=20, y=160)
    present = Entry(choice_window,font=('Arial', 10, 'bold'), fg = 'red', bd='2')
    present.place(x=50,y=160)
    Label(choice_window,text='A', font=('Arial', 15, 'bold')).place(x=220, y=160)
    absent = Entry(choice_window, font=('Arial', 10, 'bold'), fg='red', bd='2')
    absent.place(x=250, y=160)


    print(semchoosen.get())
    print(deptchoosen.get())
    #if dept_choice == "MCA" and sem_choice == "FOURTH":
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abc",
            database="Attendance"

    )
    mycursor = mydb.cursor()
    query1="select Roll_No, Name, '' as Attendance from "
    query2 = " order by Roll_No"
    mycursor.execute(query1+dept_choice+query2)
    #mycursor.execute("Select Roll_No, Name,'' as Attendance from MCA order by Roll_No")
    output = mycursor.fetchall()
    choice_heading = ['Roll No', 'Name', 'Attendance']
    output.insert(0, choice_heading)
    print(output)
    choice_window_frame = Frame(choice_window)
    choice_window_frame.place(height=280, width=370, x=10, y=200)
    choice_window_frame.config(bd=5, bg="#56943f")
    choice_window_frame.config(relief=RIDGE)
    rows = len(output)
    columns = 3
    for i in range(rows):
        for j in range(columns):
            e = Entry(choice_window_frame, bd=2, width=16, fg='black', font=('Arial', 10, 'bold'))
            e.grid(row=i, column=j)
            e.insert(END, output[i][j])
            if i == 1 and j == 2:
                a = e
            elif i == 2 and j == 2:
                b = e
            elif i == 3 and j == 2:
                c = e
            # elif i == 4 and j == 2:
            #     d = e
    choice_window.mainloop()

def total_attendance():
    global output,absent, present,a,b,c,d,choice_date,data,mycursor,mydb,dept_choice,choice_window,mycursor,fac_name
    dept = dept_choice.lower()
    faculty_name = fac_name.cget("text")
    a1=a.get()
    b1=b.get()
    c1=c.get()
    # d1=d.get()
    lst = [a1,b1,c1]
    print(lst)
    absent_std = 0
    present_std = 0
    for i in lst:
        if i=='A':
            absent_std+=1
        elif i=='P':
            present_std+=1
        else:
            messagebox.showwarning("warning","enter correct abbreviations")
            absent.delete(0,END)
            present.delete(0,END)

    print(absent_std,present_std)
    absent.insert(END, absent_std)
    present.insert(END, present_std)
    messagebox.showinfo("Info","Attendance has been recorded")
    query="select Name from "
    table = dept
    print(query+table)
    mycursor.execute(query+table)
    record = mycursor.fetchall()
    lst=["Date",choice_date,dept_choice,sem_choice,faculty_name,record[0],a1,record[1],b1,record[2],c1]
    print(lst)

    filename = "practice.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(lst)

