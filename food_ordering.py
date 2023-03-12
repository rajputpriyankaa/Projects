import mysql.connector
from PIL import ImageTk
import PIL.Image
from food_about import *
from food_help import *
from ovenstory_pizza import *
from dunkin_donuts import *
from cakes_star import *
from biryani import *
from burger_factory import *
from singh_dhaba import *
from cart import *
import time

def login():
    global  login_mail,login_password,var, main_frame,win,f1
    win = Tk()
    win.title('Login page')

    # win.geometry('1200x600')
    # win.attributes('-fullscreen', True)
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry("%dx%d" % (width, height))
    win.configure(bg='#b30d36')
    win.resizable(False,False)
    main_frame = Frame(win)
    main_frame.place(height=768, width=1366, x=0, y=0)

    bg = PhotoImage(file=r"C:\Users\Admin\Downloads\wallpaper.png")
    canvas1 = Canvas(main_frame, width=400, height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(700, 0, image=bg, anchor="nw")

    upr_fr = Frame(main_frame)
    upr_fr.place(height=80, width=680, x=0, y=0)
    upr_fr.config(bd=3,relief=RIDGE)
    bg1 = PhotoImage(file=r"C:\Users\Admin\Downloads\images.png")
    canvas2 = Canvas(upr_fr, width=100, height=100)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg1, anchor="nw")
    Label(upr_fr,text="Order food from your favourite restaurants.........😋",font = ("Arial", 15, "italic")).place(x = 200, y = 40)

    f1 = Frame(main_frame)
    f1.place(height=500, width=500, x=100, y=150)
    f1.config(bd=5,relief=RIDGE)
    Label(f1, text='Email ID', font=('Arial', 20, 'bold')).place(x=40, y=20)
    login_mail = Entry(f1, font=('Arial', 15, 'bold'), fg = 'red', bd='2')
    login_mail.place(width = 400,x=40, y=70)

    Label(f1, text='Password', font=('Arial', 20, 'bold')).place(x=40, y=120)
    login_password = Entry(f1, font=('Arial', 15, 'bold'), fg = 'red', bd='2',show="*")
    login_password.place(x=40, y=170)

    var=IntVar()
    bt = Checkbutton(f1,command=show,offvalue=0,onvalue=1,variable=var)
    bt.place(x=300, y=175)
    Button(f1, text='Cancel', font=('Arial', 20, 'bold','underline'), command=exit).place(x=40, y=250)
    Button(f1, text='Login', font=('Arial', 20, 'bold','underline'),command=restaurants).place(x=200, y=250)
    Button(f1, text='create a new account', font=('Arial', 15, 'italic','underline'),fg ="red", command=new_account).place(x=40, y=400)
    win.mainloop()

def show():
    global var,login_password
    if var.get()==0:
        login_password.configure(show="*")
    elif var.get()==1:
        login_password.configure(show="")

def new_account():
    global user_name,user_address,user_mobile,user_email,user_password,var1,win,f1,main_frame
    main_frame.pack_forget()
    f1 = Frame(win)
    f1.place(height=700, width=1300, x=20, y=20)
    f1.config(bd=5, relief=RIDGE,bg="pink")
    Label(f1, text='        Complete your profile       ', font=('Arial', 20, 'bold'),bg="green").place(x=450, y=20)

    Label(f1, text='Name', font=('Arial', 20, 'bold')).place(x=40, y=150)
    user_name = Entry(f1, font=('Arial', 20, 'bold'),width=40, fg='red', bd='2')
    user_name.place(x=500, y=150)

    Label(f1, text='Address', font=('Arial', 20, 'bold')).place(x=40, y=210)
    user_address = Entry(f1, font=('Arial', 20, 'bold'),width=40, fg='red', bd='2')
    user_address.place(x=500, y=210)

    Label(f1, text='Mobile no', font=('Arial', 20, 'bold')).place(x=40, y=270)
    user_mobile = Entry(f1, font=('Arial', 20, 'bold'),width=40, fg='red', bd='2')
    user_mobile.place(x=500, y=270)

    Label(f1, text='Email-id', font=('Arial', 20, 'bold')).place(x=40, y=320)
    user_email = Entry(f1, font=('Arial', 20, 'bold'),width=40, fg='red', bd='2')
    user_email.place(x=500, y=320)

    Label(f1, text='Password', font=('Arial', 20, 'bold')).place(x=40, y=390)
    user_password = Entry(f1, font=('Arial', 20, 'bold'),width=40, fg='red', bd='2',show="*")
    user_password.place(x=500, y=390)

    var1 = IntVar()
    bt1 = Checkbutton(f1, command=show1, offvalue=0, onvalue=1, variable=var1)
    bt1.place(x=1050, y=395)
    Button(f1, text='Create', font=('Arial', 20, 'italic'), command=new_login).place(x=400, y=600)
    Button(f1, text='Delete', font=('Arial', 20, 'italic'), command=delete).place(x=550, y=600)
    Button(f1, text='Exit', font=('Arial', 20, 'bold','underline'), command=exit).place(x=700, y=600)

def show1():
    global var1 ,user_password
    if var1.get()==0:
        user_password.configure(show="*")
    elif var1.get()==1:
        user_password.configure(show="")

def new_login():
    global user_name,user_password,user_address,user_mobile,user_email,f1
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="shopping"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from profiles where mobileno = %s and emailid = %s",(user_mobile.get(),user_email.get()))
    record = mycursor.fetchall()
    for i,j in record:
        if user_mobile.get()==i and user_email.get()==j:
            messagebox.showerror("error","account already exists")
            user_name.delete(0,END)
            user_password.delete(0,END)
            break

    if user_name and user_password and user_address and user_mobile and user_email!='':
        mycursor.execute("insert into profiles values(%s,%s,%s,%s,%s)",(user_name.get(),user_address.get(),user_mobile.get(),user_email.get(),user_password.get()))
        mydb.commit()
        messagebox.showinfo("Message","Account created successfully! Kindly login again")
        user_name.delete(0,END)
        user_password.delete(0,END)
        f1.destroy()
    else:
        messagebox.showerror("error","please enter complete details")

def delete():
    global user_name,user_password,user_address,user_mobile,user_email
    user_name.delete(0,END)
    user_address.delete(0,END)
    user_mobile.delete(0,END)
    user_email.delete(0,END)
    user_password.delete(0,END)

def restaurants():
    global login_mail,login_password,win,main_frame
    email = login_mail.get()
    password = login_password.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="shopping"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select emailid, password from profiles")
    data = mycursor.fetchall()
    for i,j in data:
        if email == i and password == j:
            access()
            break
    else:
        messagebox.showerror("failure!","login not successful☹")
        login_mail.delete(0,END)
        login_password.delete(0,END)

def access():
    global win,main_frame,login_mail,res_frame
    email=login_mail.get()
    main_frame.destroy()
    res_frame = Frame(win)
    res_frame.place(height=768, width=1366, x=0, y=0)

    heading_frame = Frame(res_frame)
    heading_frame.place(height=100, width=1360, x=0, y=0)
    heading_frame.config(bd=3, relief=RIDGE)
    image1 = PIL.Image.open(r"C:\Users\Admin\Downloads\images.png")
    image1 = image1.resize((150, 80), PIL.Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(heading_frame, image=test)
    label1.image = test
    label1.place(x=10, y=0)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="shopping"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select name from profiles where emailid = %s ",(email,))
    data = mycursor.fetchall()
    print(data[0][0])
    filename = "login.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data[0][0])
    Button(heading_frame,text = "ℹAbout", font=('Arial', 20, 'bold'),bd=0,cursor="hand1", command=about).place(x=720, y=40)
    Button(heading_frame,text = "✍Help", font=('Arial', 20, 'bold'),bd=0,cursor="hand1", command=help).place(x=840, y=40)
    Button(heading_frame,text = "🛒Cart", font=('Arial', 20, 'bold'),bd=0,cursor="hand1", command=cart).place(x=950, y=40)
    mb = Menubutton(heading_frame, text="welcome "+data[0][0],font=('Arial', 20, 'italic','bold') ,relief=RAISED)
    mb.place(x=1080, y=30)
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    signout = StringVar()
    mb.menu.add_checkbutton(label="sign out",variable=signout,command=sign_out)
    mb.place(x=1080,y=50)
    # Button(heading_frame,text = "welcome "+data[0][0], font=('Arial', 20, 'bold'),cursor="hand1",bd=5, command=exit).place(x=1080, y=30)

    middle_frame = Frame(res_frame)
    middle_frame.place(height=200, width=1360, x=0, y=102)
    middle_frame.config(bd=3, relief=RIDGE,bg = "#03002b")
    image_banner = PIL.Image.open(r"C:\Users\Admin\Downloads\banner1.png")
    image_banner = image_banner.resize((200, 150), PIL.Image.ANTIALIAS)
    test_im_banner = ImageTk.PhotoImage(image_banner)
    label2 = tkinter.Label(middle_frame, image=test_im_banner)
    label2.image = test_im_banner
    label2.place(x=20, y=12)

    image_banner = PIL.Image.open(r"C:\Users\Admin\Downloads\banner2.png")
    image_banner = image_banner.resize((200, 150), PIL.Image.ANTIALIAS)
    test_im_banner = ImageTk.PhotoImage(image_banner)
    label2 = tkinter.Label(middle_frame, image=test_im_banner)
    label2.image = test_im_banner
    label2.place(x=270, y=12)

    image_banner = PIL.Image.open(r"C:\Users\Admin\Downloads\banner4.png")
    image_banner = image_banner.resize((200, 150), PIL.Image.ANTIALIAS)
    test_im_banner = ImageTk.PhotoImage(image_banner)
    label2 = tkinter.Label(middle_frame, image=test_im_banner)
    label2.image = test_im_banner
    label2.place(x=550, y=12)

    image_banner = PIL.Image.open(r"C:\Users\Admin\Downloads\banner5.png")
    image_banner = image_banner.resize((200, 150), PIL.Image.ANTIALIAS)
    test_im_banner = ImageTk.PhotoImage(image_banner)
    label2 = tkinter.Label(middle_frame, image=test_im_banner)
    label2.image = test_im_banner
    label2.place(x=850, y=12)

    image_banner = PIL.Image.open(r"C:\Users\Admin\Downloads\banner3.png")
    image_banner = image_banner.resize((200, 150), PIL.Image.ANTIALIAS)
    test_im_banner = ImageTk.PhotoImage(image_banner)
    label2 = tkinter.Label(middle_frame, image=test_im_banner)
    label2.image = test_im_banner
    label2.place(x=1130, y=12)

    res_frame1 = Frame(res_frame)
    res_frame1.place(height=200, width=300, x=400, y=310)
    res_frame1.config(bd=3, relief=RIDGE)
    image_1 = PIL.Image.open(r"C:\Users\Admin\Downloads\ovenstory pizza.png")
    image_1 = image_1.resize((270, 120), PIL.Image.ANTIALIAS)
    test_1 = ImageTk.PhotoImage(image_1)
    label_1 = tkinter.Label(res_frame1, image=test_1)
    label_1.image = test_1
    label_1.place(x=10, y=2)
    Label(res_frame1, text='Ovenstory Pizza', font=('Arial', 15, 'italic','bold')).place(x=10, y=140)
    Label(res_frame1, text='Pizzas, Italian', font=('Arial', 8, 'italic')).place(x=10, y=170)
    Label(res_frame1, text='4.5*', font=('Arial', 10, 'bold'),bg="green").place(x=250, y=130)
    Button(res_frame1, text='Know more', font=('Arial', 10, 'bold'),fg="blue",bd=0,cursor="hand1", command=ovenstory_pizza).place(x=190, y=160)


    res_frame2 = Frame(res_frame)
    res_frame2.place(height=200, width=300, x=400, y=520)
    res_frame2.config(bd=3, relief=RIDGE)
    image_2 = PIL.Image.open(r"C:\Users\Admin\Downloads\dunkin donuts.png")
    image_2 = image_2.resize((270, 120), PIL.Image.ANTIALIAS)
    test_2 = ImageTk.PhotoImage(image_2)
    label_2 = tkinter.Label(res_frame2, image=test_2)
    label_2.image = test_2
    label_2.place(x=10, y=2)
    Label(res_frame2, text='Dunkin Donuts', font=('Arial', 15, 'italic', 'bold')).place(x=10, y=140)
    Label(res_frame2, text='Desserts, Bakery', font=('Arial', 8, 'italic')).place(x=10, y=170)
    Label(res_frame2, text='4.2*', font=('Arial', 10, 'bold'), bg="green").place(x=250, y=130)
    Button(res_frame2, text='Know more', font=('Arial', 10, 'bold'), fg="blue", bd=0, cursor="hand1",command=dunkin_donuts).place(x=190, y=160)

    res_frame3 = Frame(res_frame)
    res_frame3.place(height=200, width=300, x=720, y=310)
    res_frame3.config(bd=3, relief=RIDGE)
    image_3 = PIL.Image.open(r"C:\Users\Admin\Downloads\cakes star.png")
    image_3 = image_3.resize((270, 120), PIL.Image.ANTIALIAS)
    test_3 = ImageTk.PhotoImage(image_3)
    label_3 = tkinter.Label(res_frame3, image=test_3)
    label_3.image = test_3
    label_3.place(x=10, y=2)
    Label(res_frame3, text='Cakes Star', font=('Arial', 15, 'italic', 'bold')).place(x=10, y=140)
    Label(res_frame3, text='Bakery', font=('Arial', 8, 'italic')).place(x=10, y=170)
    Label(res_frame3, text='4.4*', font=('Arial', 10, 'bold'), bg="green").place(x=250, y=130)
    Button(res_frame3, text='Know more', font=('Arial', 10, 'bold'), fg="blue", bd=0, cursor="hand1",command=cakes_star).place(x=190, y=160)

    res_frame4 = Frame(res_frame)
    res_frame4.place(height=200, width=300, x=720, y=520)
    res_frame4.config(bd=3, relief=RIDGE)
    image_4 = PIL.Image.open(r"C:\Users\Admin\Downloads\behrouz biryani.png")
    image_4 = image_4.resize((270, 120), PIL.Image.ANTIALIAS)
    test_4 = ImageTk.PhotoImage(image_4)
    label_4 = tkinter.Label(res_frame4, image=test_4)
    label_4.image = test_4
    label_4.place(x=10, y=2)
    Label(res_frame4, text='Behrouz Biryani', font=('Arial', 15, 'italic', 'bold')).place(x=10, y=140)
    Label(res_frame4, text='Biryani, kebabs', font=('Arial', 8, 'italic')).place(x=10, y=170)
    Label(res_frame4, text='4.7*', font=('Arial', 10, 'bold'), bg="green").place(x=250, y=130)
    Button(res_frame4, text='Know more', font=('Arial', 10, 'bold'), fg="blue", bd=0, cursor="hand1",command=biryani).place(x=190, y=160)

    res_frame5 = Frame(res_frame)
    res_frame5.place(height=200, width=300, x=1040, y=310)
    res_frame5.config(bd=3, relief=RIDGE)
    image_5 = PIL.Image.open(r"C:\Users\Admin\Downloads\burger factory.png")
    image_5 = image_5.resize((270, 120), PIL.Image.ANTIALIAS)
    test_5 = ImageTk.PhotoImage(image_5)
    label_5 = tkinter.Label(res_frame5, image=test_5)
    label_5.image = test_5
    label_5.place(x=10, y=2)
    Label(res_frame5, text='Burger Factory', font=('Arial', 15, 'italic', 'bold')).place(x=10, y=140)
    Label(res_frame5, text='Snacks, Beverages', font=('Arial', 8, 'italic')).place(x=10, y=170)
    Label(res_frame5, text='4.1*', font=('Arial', 10, 'bold'), bg="green").place(x=250, y=130)
    Button(res_frame5, text='Know more', font=('Arial', 10, 'bold'), fg="blue", bd=0, cursor="hand1", command=burger_factory).place(x=190, y=160)

    res_frame6 = Frame(res_frame)
    res_frame6.place(height=200, width=300, x=1040, y=520)
    res_frame6.config(bd=3, relief=RIDGE)
    image_6 = PIL.Image.open(r"C:\Users\Admin\Downloads\singh dhaba.png")
    image_6 = image_6.resize((270, 120), PIL.Image.ANTIALIAS)
    test_6 = ImageTk.PhotoImage(image_6)
    label_6 = tkinter.Label(res_frame6, image=test_6)
    label_6.image = test_6
    label_6.place(x=10, y=2)
    Label(res_frame6, text='Singh Dhaba', font=('Arial', 15, 'italic', 'bold')).place(x=10, y=140)
    Label(res_frame6, text='Indian, Combo', font=('Arial', 8, 'italic')).place(x=10, y=170)
    Label(res_frame6, text='4.0*', font=('Arial', 10, 'bold'), bg="green").place(x=250, y=130)
    Button(res_frame6, text='Know more', font=('Arial', 10, 'bold'), fg="blue", bd=0, cursor="hand1",command=singh_dhaba).place(x=190, y=160)

    side_frame = Frame(res_frame)
    side_frame.place(height=410, width=380, x=10, y=310)
    side_frame.config(bd=3, relief=RIDGE,bg="#f44305")
    Label(side_frame, text='🎉 Special Offers', font=('Arial', 20, 'italic', 'bold'),borderwidth=3, relief="raised",cursor="dot").place(x=10, y=40)
    Label(side_frame, text='🔥 Top Picks', font=('Arial', 20, 'italic', 'bold'),borderwidth=3, relief="raised",cursor="dot").place(x=10, y=100)
    Label(side_frame, text="🥣 What's new", font=('Arial', 20, 'italic', 'bold'),borderwidth=3, relief="raised",cursor="dot").place(x=10, y=160)
    Label(side_frame, text='✔ Only on Foodiz', font=('Arial', 20, 'italic', 'bold'),borderwidth=3, relief="raised",cursor="dot").place(x=10, y=220)
    Label(side_frame, text='✅ Veg available', font=('Arial', 20, 'italic', 'bold'),borderwidth=3, relief="raised",cursor="dot").place(x=10, y=280)
    Label(side_frame, text='🥮 Festivals special', font=('Arial', 20, 'italic', 'bold'),borderwidth=3, relief="raised",cursor="dot").place(x=10, y=340)

def sign_out():
    global res_frame
    res_frame.destroy()
    main_frame.destroy()
    signout_frame = Frame(win)
    signout_frame.place(height=768, width=1366, x=0, y=0)
    label=Label(signout_frame, text="Signing out....\nwait for few seconds", font=("times", 20, "bold"), bg='#e295a9')
    label.pack(fill='both', expand=True)
    win.after(1000,destroy_timer)

def destroy_timer():
    exit()

login()
