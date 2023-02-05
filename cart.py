import tkinter
from tkinter import *
import mysql.connector
import csv
from tkinter import messagebox,ttk
from ovenstory_pizza import check_out
import datetime

def cart():
    global cart,main_frame,place_order,back_btn
    cart = tkinter.Tk()
    cart.title('Foodiz Cart')
    width = cart.winfo_screenwidth()
    height = cart.winfo_screenheight()
    cart.geometry("%dx%d" % (width, height))
    cart.resizable(False, False)
    cart.configure(bg="#9f96fc")
    Label(cart, text="      Foodiz cart     ", font=("times", 20,"bold"),bg="orange").place(x=50, y=20)
    back_btn=Button(cart, text="     Back        ", font=("times", 15, "bold"), bg='green', command=home_page)
    back_btn.place(x=850,y=20)
    main_frame = Frame(master=cart)
    main_frame.place(height=550, width=1320, x=20, y=120)
    main_frame.config(bd=5, relief=RIDGE)
    filename = "login.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        join_name = list(csvreader)

    user = "".join(join_name[0])
    Label(cart, text="  User : "+user+" ", font=("times", 20,"bold"),bg="orange").place(x=1100, y=20)
    place_order = Button(cart, text="  Place Order ", font=("times", 15,"bold"),bg="green",command=askrestaurantname)
    place_order.place(x=1100, y=680)
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sql@#987",
            database="shopping"

        )
    mycursor = mydb.cursor()
    mycursor.execute("select count(*) from cart where username = %s", (user,))
    count = mycursor.fetchall()
    print(count[0][0],type(count))
    if count[0][0]>0:
        mycursor.execute("select restaurant,item,quantity,price from cart where username = %s", (user,))
        record = mycursor.fetchall()
        heading = ['Restaurant', 'Item', 'Quantity','Price']
        record.insert(0, heading)
        row = len(record)
        col = len(record[0])
        for i in range(row):
            for j in range(col):
                e = Entry(main_frame, bd=2, width=29, fg='red', font=('Arial', 15, 'bold'))
                if i == 0:
                    e.configure(fg="black")
                e.grid(row=i, column=j)
                e.insert(END, record[i][j])

    else:
        messagebox.showinfo("Status", "Nothing is in cart!")
        Label(main_frame, text="Cart empty [0]", font=("times", 20, "bold"),bg='#e295a9').pack(fill='both', expand=True)
        cart.deiconify()
        place_order.destroy()
        Button(cart, text="     Back        ", font=("times", 15, "bold"), bg='green', command=home_page).place(x=550,y=680)
    cart.mainloop()

def askrestaurantname():
    global cart,main_frame,reschoosen,second_frame,display_frame,place_order,res_name,get_detail,chk_out
    main_frame.destroy()
    place_order.destroy()
    chk_out=Button(cart, text="  Check Out ", font=("times", 15, "bold"), bg="green", command=check_out)
    chk_out.place(x=1100, y=680)
    second_frame = Frame(master=cart)
    second_frame.place(height=550, width=1320, x=20, y=120)
    second_frame.config(bd=5, relief=RIDGE)
    res_name=Label(second_frame, text="  Restaurant Name ", font=("times", 20,"bold"),bg="orange")
    res_name.place(x=100, y=20)
    get_detail=Button(second_frame, text="Get details", font=("times", 20,"bold"),bg="orange",command=get_details)
    get_detail.place(x=1050, y=20)
    display_frame = Frame(master=second_frame)
    display_frame.place(height=300, width=1280, x=20, y=200)
    display_frame.config(bd=5, relief=RIDGE)
    n = StringVar()
    reschoosen = ttk.Combobox(second_frame, width=30, textvariable=n)
    reschoosen['values'] = ('Ovenstory Pizza', 'Dunkin Donuts', 'Cakes Star','Burger Factory', 'Singh Dhaba','Behrouz Biryani')
    reschoosen.place(height=30,x=600, y=30)
    reschoosen.current(0)

def get_details():
    global display_frame,q1,p1,q2,p2,q3,p3,q4,p4,price1_cal,price2_cal,price3_cal,price4_cal,refresh_button,reschoosen,res_choosen,total_price,count
    res_choosen=reschoosen.get()
    refresh_button=Button(display_frame, text="Refresh", font=("times", 15,"bold"),bg="orange",command=refresh)
    refresh_button.place(x=550, y=220)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sql@#987",
        database="shopping"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select restaurant,item,quantity,price from cart where restaurant = %s", (reschoosen.get(),))
    record = mycursor.fetchall()
    heading = ['Restaurant', 'Item', 'Quantity','Price']
    record.insert(0, heading)
    row = len(record)
    col = len(record[0])
    for i in range(row):
        for j in range(col):
            e = Entry(display_frame, bd=2, width=28, fg='red', font=('Arial', 15, 'bold'))
            if i == 0:
                e.configure(fg="black")
            if i == 1:
                if j == 2:
                    q1=e
                if j == 3:
                    p1=e
            if i == 2:
                if j == 2:
                    q2=e
                if j == 3:
                    p2=e
            if i == 3:
                if j == 2:
                    q3=e
                if j == 3:
                    p3=e
            if i == 4:
                if j == 2:
                    q4=e
                if j == 3:
                    p4=e
            e.grid(row=i, column=j)
            e.insert(END, record[i][j])
    mycursor.execute("select count(*) from cart where restaurant = %s", (reschoosen.get(),))
    count = mycursor.fetchone()
    total=0
    print(count)
    if count[0]>0:
        p1_get = p1.get()
        price1_split = p1_get.split()
        price1_cal = int(price1_split[1]) / int(q1.get())
        total += int(price1_split[1])
    if count[0]>1:
        p2_get = p2.get()
        price2_split = p2_get.split()
        price2_cal = int(price2_split[1]) / int(q2.get())
        total += int(price2_split[1])
    if count[0] > 2:
        p3_get = p3.get()
        price3_split = p3_get.split()
        price3_cal = int(price3_split[1]) / int(q3.get())
        total += int(price3_split[1])
    if count[0] > 3:
        p4_get = p4.get()
        price4_split = p4_get.split()
        price4_cal = int(price4_split[1]) / int(q4.get())
        total += int(price4_split[1])

    total_price=Label(display_frame, text="Total:   "+str(total), font=("times", 15, "bold"), bg="green")
    total_price.place(x=10, y=220)


def refresh():
    global q1,p1,q2,p2,q3,p3,q4,p4,price1_cal,price2_cal,price3_cal,price4_cal,total_price,total
    total=0
    if count[0] > 0:
        quan1 = int(q1.get())
        final_price1_cal = price1_cal * quan1
        p1.delete(0, END)
        p1_text = "Rs. " + str(final_price1_cal)
        p1.insert(END, p1_text)
        total += final_price1_cal
    if count[0] > 1:
        quan2 = int(q2.get())
        final_price2_cal = price2_cal * quan2
        p2.delete(0, END)
        p2_text = "Rs. " + str(final_price2_cal)
        p2.insert(END, p2_text)
        total += final_price2_cal
    if count[0] > 2:
        quan3 = int(q3.get())
        final_price3_cal = price3_cal * quan3
        p3.delete(0, END)
        p3_text = "Rs. " + str(final_price3_cal)
        p3.insert(END, p3_text)
        total += final_price3_cal
    if count[0] > 3:
        quan4 = int(q4.get())
        final_price4_cal = price4_cal * quan4
        p4.delete(0, END)
        p4_text = "Rs. " + str(final_price4_cal)
        p4.insert(END, p4_text)
        total += final_price4_cal

    total_price.config(text="Total:   "+str(total))

def check_out():
    global cart, second_frame,display_frame,refresh_button,res_name,get_detail,reschoosen,chk_out,total_price,buy,coupon_button
    refresh_button.destroy()
    display_frame.place(height=200, width=1300,x=5, y=340)
    res_name.destroy()
    get_detail.destroy()
    reschoosen.destroy()
    chk_out.destroy()
    current_date=datetime.date.today()
    print(current_date)
    Label(second_frame, text="  Order details   ", font=("times", 15, "bold"),bg="green").place(x=500, y=10)
    Label(second_frame, text="Name: Priyanka ", font=("times", 15, "bold")).place(x=20, y=50)
    Label(second_frame, text="Address: Sec 95,Gurgaon", font=("times", 15, "bold")).place(x=20, y=100)
    Label(second_frame, text="Mobile no: 9809812389", font=("times", 15, "bold")).place(x=20, y=150)
    Label(second_frame, text="Email address: priya98rajput@gmail.com", font=("times", 15, "bold")).place(x=20, y=200)
    Label(second_frame, text="Restaurant: Ovenstory Pizza", font=("times", 15, "bold")).place(x=20, y=250)
    Label(second_frame, text="Date: "+str(current_date), font=("times", 15, "bold")).place(x=20, y=300)
    total_price.place(x=550,y=152)
    buy=Button(cart, text="  Buy now ", font=("times", 15, "bold"), bg="green", command=buy_now)
    buy.place(x=1100, y=680)
    coupon_button = Button(cart, text="Add Coupon code", font=("times", 15, "bold"), bg="orange",command=promo_code)
    coupon_button.place(x=100, y=680)

def promo_code():
    global user_input, code
    code = tkinter.Tk()
    code.title("promo code")
    code.geometry('250x150')
    code.resizable(False, False)
    Label(code, text="Code", font=("times", 15, "bold")).place(x=10, y=20)
    user_input = Entry(code, bd=2, fg='red', font=('Arial', 10, 'bold'))
    user_input.place(x=70, y=20)
    Button(code, text="Add Coupon code", font=("times", 15, "bold"), bg="orange", command=coupon_price).place(x=50, y=70)

def coupon_price():
    global res_choosen,coupon_input,total_price,total,cart,code
    coupon_input = user_input.get()
    if res_choosen == "Ovenstory Pizza":
        if coupon_input == "STEALDEAL":
            final_total = total-(total*0.60)
            total_price.config(text="Total:   "+str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        elif coupon_input == "UNLIMITED":
            final_total = total - (total * 0.20)
            total_price.config(text="Total:   " + str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        else:
            messagebox.showerror("Error", "Coupon code is not correct!")
            code.destroy()
            cart.deiconify()
    elif res_choosen == "Dunkin Donuts":
        if coupon_input == "SPECIALS":
            final_total = total-(total*0.30)
            total_price.config(text="Total:   "+str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        elif coupon_input == "TRYNEW":
            final_total = total - (total * 0.20)
            total_price.config(text="Total:   " + str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        else:
            messagebox.showerror("Error", "Coupon code is not correct!")
            code.destroy()
            cart.deiconify()
    elif res_choosen == "Cakes Star":
        if coupon_input == "SPECIALS":
            final_total = total-(total*0.30)
            total_price.config(text="Total:   "+str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        elif coupon_input == "TRYNEW":
            final_total = total - (total * 0.20)
            total_price.config(text="Total:   " + str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        else:
            messagebox.showerror("Error", "Coupon code is not correct!")
            code.destroy()
            cart.deiconify()
    elif res_choosen == "Burger Factory":
        if coupon_input == "STEALDEAL":
            final_total = total-(total*0.60)
            total_price.config(text="Total:   "+str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        elif coupon_input == "UNLIMITED":
            final_total = total - (total * 0.20)
            total_price.config(text="Total:   " + str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        else:
            messagebox.showerror("Error", "Coupon code is not correct!")
            code.destroy()
            cart.deiconify()
    elif res_choosen == "Singh Dhaba":
        if coupon_input == "JUMBO":
            final_total = total-(total*0.30)
            total_price.config(text="Total:   "+str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        elif coupon_input == "TRYNEW":
            final_total = total - (total * 0.20)
            total_price.config(text="Total:   " + str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        else:
            messagebox.showerror("Error", "Coupon code is not correct!")
            code.destroy()
            cart.deiconify()
    elif res_choosen == "Behrouz Biryani":
        if coupon_input == "SPECIALS":
            final_total = total-(total*0.30)
            total_price.config(text="Total:   "+str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        elif coupon_input == "UNLIMITED":
            final_total = total - (total * 0.20)
            total_price.config(text="Total:   " + str(final_total))
            messagebox.showinfo("Success", "Coupon code placed successfully!")
            code.destroy()
            cart.deiconify()
        else:
            messagebox.showerror("Error", "Coupon code is not correct!")
            code.destroy()
            cart.deiconify()

def buy_now():
    global res_choosen,second_frame,buy,coupon_button,cart
    buy.destroy()
    back_btn.destroy()
    messagebox.showinfo("status","your order is placed successfully😀")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sql@#987",
        database="shopping"

    )
    mycursor = mydb.cursor()
    mycursor.execute("delete from cart where restaurant = %s", (res_choosen,))
    mydb.commit()
    empty_cart_frame = Frame(master=cart)
    empty_cart_frame.place(height=550, width=1320, x=20, y=120)
    empty_cart_frame.config(bd=5, relief=RIDGE)
    Label(empty_cart_frame,text="Cart is empty for the hotel you selected", font=("times", 20, "bold"),bg='#e295a9').pack(fill='both',expand=True)
    coupon_button.destroy()
    Button(cart,text="Go to Home page", font=("times", 20, "bold"),bg='#e295a9',command=home_page).place(x=550,y=20)
    cart.deiconify()

def home_page():
    global cart
    cart.destroy()

