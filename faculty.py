from tkinter import *
import mysql.connector
from tkinter import messagebox

def faculty_registration():
    global root, faculty_name,faculty_id,faculty_address,faculty_mobile,faculty_email
    root = Tk()
    root.title('Faculty registration')
    root.geometry('600x500')
    root.resizable(False, False)
    root.configure(bg = '#9e3e48')
    f2 = Frame(root)
    f2.place(height=300, width=400, x=100, y=50)
    f2.config(bd=5, bg="#b38092")
    f2.config(relief=RIDGE)
    Label(f2, text='Name', font=('Arial', 15, 'bold')).place(x=20, y=30)
    faculty_name = Entry(f2, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    faculty_name.place(x=130, y=30)

    Label(f2, text='ID', font=('Arial', 15, 'bold')).place(x=20, y=80)
    faculty_id = Entry(f2, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    faculty_id.place(x=130, y=80)

    Label(f2, text='Address', font=('Arial', 15, 'bold')).place(x=20, y=130)
    faculty_address = Entry(f2, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    faculty_address.place(x=130, y=130)

    Label(f2, text='Mobile no', font=('Arial', 15, 'bold')).place(x=20, y=180)
    faculty_mobile = Entry(f2, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    faculty_mobile.place(x=130, y=180)

    Label(f2, text='Email ID', font=('Arial', 15, 'bold')).place(x=20, y=230)
    faculty_email = Entry(f2, font=('Arial', 15, 'bold'), fg='red', bd='2')
    faculty_email.place(x=130, y=230)

    Button(root, text='Back', font=('Arial', 15, 'bold'), command=root.destroy).place(x=40, y=420)
    Button(root, text='Search details', font=('Arial', 15, 'bold'), command=search_faculty_details).place(x=140, y=420)
    Button(root, text='Register', font=('Arial', 15, 'bold'), command=faculty_register).place(x=320, y=420)
    Button(root, text='Cancel', font=('Arial', 15, 'bold'), command=exit).place(x=450, y=420)

    root.mainloop()

def faculty_register():
    global faculty_name,faculty_id,faculty_address,faculty_mobile,faculty_email
    fac_name = faculty_name.get()
    fac_id = faculty_id.get()
    fac_address = faculty_address.get()
    fac_mobile = faculty_mobile.get()
    fac_email = faculty_email.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    mycursor.execute("insert into faculty(ID,Name,Address,Mobile_No,Email) values(%s,%s,%s,%s,%s) ",(fac_id,fac_name,fac_address,fac_mobile,fac_email))
    messagebox.showinfo("Registration","Faculty registered successfully")
    faculty_id.delete(0,END)
    faculty_name.delete(0,END)
    faculty_address.delete(0,END)
    faculty_mobile.delete(0,END)
    faculty_email.delete(0,END)

    mydb.commit()

def search_faculty_details():
    global fac_window, fac_window_frame, id
    fac_window = Tk()
    fac_window.title('Search Faculty details')
    fac_window.geometry('700x400')
    fac_window.resizable(False, False)
    fac_window.configure(bg='#9e3e48')
    fac_window_frame = Frame(fac_window)
    fac_window_frame.place(height=280, width=645, x=23, y=100)
    fac_window_frame.config(bd=5, bg="#b38092")
    fac_window_frame.config(relief=RIDGE)
    Label(fac_window,text='Enter ID', font=('Arial', 20, 'bold')).place(x=20, y=20)
    id = Entry(fac_window, font=('Arial', 20, 'bold'), fg = 'red', bd='2')
    id.place(x=160, y=20)
    Button(fac_window, text='Search', font=('Arial', 15, 'bold'), command=result_fac_details).place(x=500, y=20)
    fac_window.mainloop()

def result_fac_details():
    global fac_window, fac_window_frame, id
    ID = id.get()
    print(ID)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    mycursor.execute("Select * from faculty where ID = (%s) ",(ID,))
    heading=['ID', 'Name', 'Address', 'Mobile no', 'Email']
    output = mycursor.fetchall()
    output.insert(0,heading)
    print(output)
    rows = len(output)
    columns = len(output[0])
    for i in range(rows):
        for j in range(columns):
            e = Entry(fac_window_frame, bd=2, width=20, bg='#8fb9f8', font=('Arial', 8, 'bold'))
            if i==0:
                e.configure(bg="#1005f8")
            e.grid(row=i, column=j)
            e.insert(END, output[i][j])

def faculty_details():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="Attendance"

    )
    mycursor = mydb.cursor()
    mycursor.execute('Select * from faculty')
    record = mycursor.fetchall()
    heading = ['ID', 'Name', 'Address', 'Mobile no', 'Email']
    record.insert(0, heading)
    #print(record)
    # print(len(j))
    rows = len(record)
    columns = len(record[0])
    print(rows, columns)

    temp = Tk()
    temp.title("Faculty details")
    temp.geometry('1300x1300')
    f3 = Frame(temp)
    f3.place(height=650, width=1350, x=10, y=20)
    f3.config(bd=5, bg="#b38092")
    f3.config(relief=RIDGE)
    for i in range(rows):
        for j in range(columns):
            e = Entry(f3,bd = 2, width=22, fg='blue', font=('Arial', 16, 'bold'))
            if i==0:
                e.configure(fg="black")
            e.grid(row=i, column=j)
            e.insert(END, record[i][j])

    temp.mainloop()

