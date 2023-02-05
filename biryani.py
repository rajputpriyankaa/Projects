import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
import csv

def biryani():
    global d1, restaurant1, cart_frame, empty_cart, b1, b2, b3, b4, order1
    restaurant1 = tkinter.Toplevel()
    restaurant1.title('Behrouz Biryani')
    width = restaurant1.winfo_screenwidth()
    height = restaurant1.winfo_screenheight()
    restaurant1.geometry("%dx%d" % (width, height))
    restaurant1.resizable(False, False)
    Label(restaurant1, text="______F   O   O   D   I   Z______", font=("times", 20, "italic","bold"),fg="orange").place(x=50, y=20)
    Button(restaurant1, text="   Back    ", font=("times", 15,"bold"),bg="green",command=back).place(x=1200, y=5)

    heading_frame = Frame(master=restaurant1)
    heading_frame.place(height=300, width=1330, x=10, y=50)
    heading_frame.config(bd=5, relief=RIDGE)
    bg = PhotoImage(file=r"C:\Users\Admin\Downloads\bb.png")
    canvas1 = Canvas(heading_frame, width=100, height=800)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(10, 20, image=bg, anchor="nw")
    Label(heading_frame, text="Behrouz Biryani", font=("times", 20,"bold")).place(x=470, y=30)
    Label(heading_frame, text="Biryani, Mughlai, Lucknowi, Kebabs, Hyderabadi", font=("times", 15, "italic")).place(x=470, y=70)
    Label(heading_frame, text="Huda Complex,Sector 12A, Sector-14 ", font=("times", 15, "italic")).place(x=470, y=110)
    Label(heading_frame, text='4.7*', font=('times', 15, 'bold'),bg="green").place(x=470, y=150)
    Label(heading_frame, text='100+ratings', font=('times', 10)).place(x=470, y=180)
    Label(heading_frame, text='38 mins            Rs.500', font=('times', 15,'bold' )).place(x=560, y=150)
    Label(heading_frame, text='Delivery time                cost for two', font=('times', 10)).place(x=560, y=180)
    sub_heading_frame = Frame(master=heading_frame)
    sub_heading_frame.place(height=200, width=300, x=1000, y=40)
    sub_heading_frame.config(bd=5, relief=GROOVE)
    Label(sub_heading_frame, text="Offers", font=("times", 20,"bold")).place(x=5, y=5)
    Label(sub_heading_frame, text="➗ 30% off up to ₹75 on select \nitems | Use code SPECIALS", font=("times", 15,"bold")).place(x=5, y=40)
    Label(sub_heading_frame, text="➗ 20% off up to ₹50 | Use code\nUNLIMITED                           ", font=("times", 15,"bold")).place(x=5, y=90)
    Label(restaurant1, text="🥕 Veg only", font=("times", 15,"bold")).place(x=550, y=330)
    Label(restaurant1, text="Recommended items", font=("times", 15,"bold")).place(x=20, y=350)

    dishes_frame1 = Frame(master=restaurant1)
    dishes_frame1.place(height=350, width=420, x=20, y=380)
    dishes_frame1.config(bd=5, relief=GROOVE)
    bg_d1 = PhotoImage(file=r"C:\Users\Admin\Downloads\bb_d1.png")
    canvas_d1 = Canvas(dishes_frame1, width=50, height=50)
    canvas_d1.pack(fill="both", expand=True)
    canvas_d1.create_image(0, 0, image=bg_d1, anchor="nw")
    Label(dishes_frame1, text="Jashna-E-Zaitooni Paneer\n\nRs335\nA scrumptious Biryani made\nwith flavorful roasted\nveggies & soft paneer.", font=("times", 10,"italic")).place(x=250, y=50)
    b1 = Button(dishes_frame1, text='ADD TO CART', bg="green", command=lambda m='Jashna-E-Zaitooni Paneer': cart(m))
    b1.place(x=270, y=20)
    Label(dishes_frame1, text='________________________________________________________________________________').place(x=0, y=150)

    bg_d2 = PhotoImage(file=r"C:\Users\Admin\Downloads\bb_d2.png")
    canvas_d2 = Canvas(dishes_frame1, width=50, height=50)
    canvas_d2.pack(fill="both", expand=True)
    canvas_d2.create_image(200, 10, image=bg_d2, anchor="nw")
    Label(dishes_frame1,text="Subz-E-Biryani\n\nRs260\n Adorned with fresh vegetables,\ngolden-hued long-grain basmati.",font=("times", 10, "italic")).place(x=0, y=240)
    b2 = Button(dishes_frame1, text='ADD TO CART', bg="green", command=lambda m='Subz-E-Biryani': cart(m))
    b2.place(x=50, y=210)

    dishes_frame2 = Frame(master=restaurant1)
    dishes_frame2.place(height=350, width=420, x=490, y=380)
    dishes_frame2.config(bd=5, relief=GROOVE)
    bg_d3 = PhotoImage(file=r"C:\Users\Admin\Downloads\bb_d3.png")
    canvas_d3 = Canvas(dishes_frame2, width=50, height=50)
    canvas_d3.pack(fill="both", expand=True)
    canvas_d3.create_image(0, 0, image=bg_d3, anchor="nw")
    Label(dishes_frame2,text="Beetroot and peanut Kebab\n\nRs160\n[6 Pcs] Savour the flavours\nof fresh beetroots & roasted\npeanuts.",font=("times", 10, "italic")).place(x=230, y=50)
    b3 = Button(dishes_frame2, text='ADD TO CART', bg="green", command=lambda m='Beetroot and peanut Kebab': cart(m))
    b3.place(x=270, y=20)

    Label(dishes_frame2, text='________________________________________________________________________________').place(x=0, y=150)
    bg_d4 = PhotoImage(file=r"C:\Users\Admin\Downloads\bb_d4.png")
    canvas_d4 = Canvas(dishes_frame2, width=50, height=50)
    canvas_d4.pack(fill="both", expand=True)
    canvas_d4.create_image(200, 20, image=bg_d4, anchor="nw")
    Label(dishes_frame2,text="Ayran (Buttermilk)\n\nRs42\nAyran is a Persian take of\nbuttermilk topped with mint.",
                        font=("times", 10, "italic")).place(x=0, y=240)
    b4 = Button(dishes_frame2, text='ADD TO CART', bg="green", command=lambda m='Ayran (Buttermilk)': cart(m))
    b4.place(x=40, y=200)
    cart_frame = Frame(master=restaurant1)
    cart_frame.place(height=300, width=400, x=940, y=410)
    cart_frame.config(bd=5, relief=GROOVE)
    Label(cart_frame, text="Behrouz Biryani🛒", font=("times", 15, "bold"), width=32, bg="red").place(x=0, y=0)
    cartframe()
    restaurant1.mainloop()

def cartframe():
    global cart_frame, empty_cart, fake1, fake2, fake3, fake4, order1, order2, order3, order4, d1, d2, d3, d4, d1_price, d2_price, d3_price, d4_price
    cart_frame = Frame(master=restaurant1)
    cart_frame.place(height=350, width=400, x=940, y=380)
    cart_frame.config(bd=5, relief=GROOVE)
    Label(cart_frame, text="Behrouz Biryani🛒", font=("times", 15, "bold"), width=32, bg="red").place(x=0, y=0)

    order1 = Label(cart_frame, text="", font=("times", 10, "bold", "italic"))
    order1.place(x=0, y=60)
    Button(cart_frame, text='-', fg="blue", command=lambda: minus1(d1)).place(x=236, y=58)
    d1 = Entry(cart_frame, width=5, font=("times", 10, "bold", "italic"))
    d1.insert(END, 1)
    d1.place(x=250, y=60)
    Button(cart_frame, text='+', fg="blue", command=lambda: plus1(d1)).place(x=290, y=58)
    d1_price = Label(cart_frame, text="   ", font=("times", 10, "bold", "italic"))
    d1_price.place(x=330, y=60)
    fake1 = Label(cart_frame, text="", font=("times", 15, "bold"), width=32)
    fake1.place(x=0, y=60)

    order2 = Label(cart_frame, text="", font=("times", 10, "bold", "italic"))
    order2.place(x=0, y=110)
    Button(cart_frame, text='-', fg="blue", command=lambda: minus2(d2)).place(x=236, y=108)
    d2 = Entry(cart_frame, width=5, font=("times", 10, "bold", "italic"))
    d2.insert(END, 1)
    d2.place(x=250, y=110)
    Button(cart_frame, text='+', fg="blue", command=lambda: plus2(d2)).place(x=290, y=108)
    d2_price = Label(cart_frame, text="Rs. 0", font=("times", 10, "bold", "italic"))
    d2_price.place(x=330, y=110)
    fake2 = Label(cart_frame, text="", font=("times", 15, "bold"), width=32)
    fake2.place(x=0, y=110)

    order3 = Label(cart_frame, text="", font=("times", 10, "bold", "italic"))
    order3.place(x=0, y=160)
    Button(cart_frame, text='-', fg="blue", command=lambda: minus3(d3)).place(x=236, y=158)
    d3 = Entry(cart_frame, width=5, font=("times", 10, "bold", "italic"))
    d3.insert(END, 1)
    d3.place(x=250, y=160)
    Button(cart_frame, text='+', fg="blue", command=lambda: plus3(d3)).place(x=290, y=158)
    d3_price = Label(cart_frame, text="Rs. 0", font=("times", 10, "bold", "italic"))
    d3_price.place(x=330, y=160)
    fake3 = Label(cart_frame, text="", font=("times", 15, "bold"), width=32)
    fake3.place(x=0, y=160)

    order4 = Label(cart_frame, text="", font=("times", 10, "bold", "italic"))
    order4.place(x=0, y=210)
    Button(cart_frame, text='-', fg="blue", command=lambda: minus4(d4)).place(x=236, y=208)
    d4 = Entry(cart_frame, width=5, font=("times", 10, "bold", "italic"))
    d4.insert(END, 1)
    d4.place(x=250, y=210)
    Button(cart_frame, text='+', fg="blue", command=lambda: plus4(d4)).place(x=290, y=208)
    d4_price = Label(cart_frame, text="Rs. 0", font=("times", 10, "bold", "italic"))
    d4_price.place(x=330, y=210)
    fake4 = Label(cart_frame, text="", font=("times", 15, "bold"), width=32)
    fake4.place(x=0, y=210)
    empty_cart = Label(cart_frame, text="Cart is empty [0]\nPlease order something.", font=("times", 15, "bold"),
                       height=10, width=32, bg="orange")
    empty_cart.place(x=0, y=50)

def cart(dish):
    global cart_frame, empty_cart, fake1, fake2, fake3, fake4, order1, order2, order3, order4,restaurant1
    empty_cart.destroy()
    o1 = order1.cget('text')
    print(o1)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sql@#987",
        database="shopping"

    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from cart where item = %s", (dish,))
    data = mycursor.fetchall()
    if data:
        messagebox.showinfo("status", "this item is already in cart. Kindly see the cart")
        restaurant1.deiconify()
    else:
        if o1 == "":
            fake1.destroy()
            order1.config(text=dish)
            if order1.cget('text') == "Jashna-E-Zaitooni Paneer":
                price = 335
                d1_price.config(text="Rs. " + str(price))
                total()
            elif order1.cget('text') == "Subz-E-Biryani":
                price = 260
                d1_price.config(text="Rs. " + str(price))
                total()
            elif order1.cget('text') == "Beetroot and peanut Kebab":
                price = 160
                d1_price.config(text="Rs. " + str(price))
                total()
            elif order1.cget('text') == "Ayran (Buttermilk)":
                price = 42
                d1_price.config(text="Rs. " + str(price))
                total()

        elif order2.cget('text') == "":
            fake2.destroy()
            order2.config(text=dish)
            if order2.cget('text') == "Jashna-E-Zaitooni Paneer":
                price = 335
                d2_price.config(text="Rs. " + str(price))
                total()
            elif order2.cget('text') == "Subz-E-Biryani":
                price = 260
                d2_price.config(text="Rs. " + str(price))
                total()
            elif order2.cget('text') == "Beetroot and peanut Kebab":
                price = 160
                d2_price.config(text="Rs. " + str(price))
                total()
            elif order2.cget('text') == "Ayran (Buttermilk)":
                price = 42
                d2_price.config(text="Rs. " + str(price))
                total()

        elif order3.cget('text') == "":
            fake3.destroy()
            order3.config(text=dish)
            if order3.cget('text') == "Jashna-E-Zaitooni Paneer":
                price = 335
                d3_price.config(text="Rs. " + str(price))
                total()
            elif order3.cget('text') == "Subz-E-Biryani":
                price = 260
                d3_price.config(text="Rs. " + str(price))
                total()
            elif order3.cget('text') == "Beetroot and peanut Kebab":
                price = 160
                d3_price.config(text="Rs. " + str(price))
                total()
            elif order3.cget('text') == "Ayran (Buttermilk)":
                price = 42
                d3_price.config(text="Rs. " + str(price))
                total()

        elif order4.cget('text') == "":
            fake4.destroy()
            order4.config(text=dish)
            if order4.cget('text') == "Jashna-E-Zaitooni Paneer":
                price = 335
                d4_price.config(text="Rs. " + str(price))
                total()
            elif order4.cget('text') == "Subz-E-Biryani":
                price = 260
                d4_price.config(text="Rs. " + str(price))
                total()
            elif order4.cget('text') == "Beetroot and peanut Kebab":
                price = 160
                d4_price.config(text="Rs. " + str(price))
                total()
            elif order4.cget('text') == "Ayran (Buttermilk)":
                price = 42
                d4_price.config(text="Rs. " + str(price))
                total()

def plus1(d):
    global d1_price, order1
    new = int(d.get())
    new = new + 1
    d.delete(0, END)
    d.insert(END, new)
    if order1.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d1_price.config(text="Rs. " + str(price))
        total()
    elif order1.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d1_price.config(text="Rs. " + str(price))
        total()
    elif order1.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d1_price.config(text="Rs. " + str(price))
        total()
    elif order1.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d1_price.config(text="Rs. " + str(price))
        total()

def plus2(d):
    global d2_price, order2
    new = int(d.get())
    new = new + 1
    d.delete(0, END)
    d.insert(END, new)
    if order2.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d2_price.config(text="Rs. " + str(price))
        total()
    elif order2.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d2_price.config(text="Rs. " + str(price))
        total()
    elif order2.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d2_price.config(text="Rs. " + str(price))
        total()
    elif order2.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d2_price.config(text="Rs. " + str(price))
        total()

def plus3(d):
    global d3_price, order3
    new = int(d.get())
    new = new + 1
    d.delete(0, END)
    d.insert(END, new)
    if order3.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d3_price.config(text="Rs. " + str(price))
        total()
    elif order3.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d3_price.config(text="Rs. " + str(price))
        total()
    elif order3.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d3_price.config(text="Rs. " + str(price))
        total()
    elif order3.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d3_price.config(text="Rs. " + str(price))
        total()

def plus4(d):
    global d4_price, order4
    new = int(d.get())
    new = new + 1
    d.delete(0, END)
    d.insert(END, new)
    if order4.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d4_price.config(text="Rs. " + str(price))
        total()
    elif order4.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d4_price.config(text="Rs. " + str(price))
        total()
    elif order4.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d4_price.config(text="Rs. " + str(price))
        total()
    elif order4.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d4_price.config(text="Rs. " + str(price))
        total()

def minus1(d):
    global d1_price, order1
    new = int(d.get())
    if new != 0:
        new = new - 1
        d.delete(0, END)
        d.insert(END, new)
    else:
        d = IntVar()
        d.set(0)
    if order1.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d1_price.config(text="Rs. " + str(price))
        total()
    elif order1.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d1_price.config(text="Rs. " + str(price))
        total()
    elif order1.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d1_price.config(text="Rs. " + str(price))
        total()
    elif order1.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d1_price.config(text="Rs. " + str(price))
        total()

def minus2(d):
    global d2_price, order2
    new = int(d.get())
    if new != 0:
        new = new - 1
        d.delete(0, END)
        d.insert(END, new)
    else:
        d = IntVar()
        d.set(0)
    if order2.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d2_price.config(text="Rs. " + str(price))
        total()
    elif order2.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d2_price.config(text="Rs. " + str(price))
        total()
    elif order2.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d2_price.config(text="Rs. " + str(price))
        total()
    elif order2.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d2_price.config(text="Rs. " + str(price))
        total()

def minus3(d):
    global d3_price, order3
    new = int(d.get())
    if new != 0:
        new = new - 1
        d.delete(0, END)
        d.insert(END, new)
    else:
        d = IntVar()
        d.set(0)
    if order3.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d3_price.config(text="Rs. " + str(price))
        total()
    elif order3.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d3_price.config(text="Rs. " + str(price))
        total()
    elif order3.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d3_price.config(text="Rs. " + str(price))
        total()
    elif order3.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d3_price.config(text="Rs. " + str(price))
        total()

def minus4(d):
    global d4_price, order4
    new = int(d.get())
    print(new)
    if new != 0:
        new = new - 1
        d.delete(0, END)
        d.insert(END, new)
    else:
        d = IntVar()
        d.set(0)
    if order4.cget('text') == "Jashna-E-Zaitooni Paneer":
        price = 335 * new
        d4_price.config(text="Rs. " + str(price))
        total()
    elif order4.cget('text') == "Subz-E-Biryani":
        price = 260 * new
        d4_price.config(text="Rs. " + str(price))
        total()
    elif order4.cget('text') == "Beetroot and peanut Kebab":
        price = 160 * new
        d4_price.config(text="Rs. " + str(price))
        total()
    elif order4.cget('text') == "Ayran (Buttermilk)":
        price = 42 * new
        d4_price.config(text="Rs. " + str(price))
        total()

def total():
    global cart_frame, d1_price, d2_price, d3_price, d4_price, total_price, checkout, price_label
    d1 = d1_price.cget('text')
    pr_d1 = d1.split()

    d2 = d2_price.cget('text')
    pr_d2 = d2.split()

    d3 = d3_price.cget('text')
    pr_d3 = d3.split()

    d4 = d4_price.cget('text')
    pr_d4 = d4.split()
    total_price = int(pr_d1[1]) + int(pr_d2[1]) + int(pr_d3[1]) + int(pr_d4[1])
    price_label = Label(cart_frame, text="Total: " + str(total_price) + "     ", font=("times", 15, "bold"))
    price_label.place(x=10, y=300)
    checkout = Button(cart_frame, text='  CHECK OUT   ', bg="green", command=check_out)
    checkout.place(x=280, y=300)

def check_out():
    global total_price, checkout, order1, order2, order3, order4, d1, d2, d3, d4, d1_price, d2_price, d3_price, d4_price, price_label
    global check_out_frame, item_frame, final_price,coupon_button
    if total_price != 0:
        check_out_frame = Frame(master=restaurant1)
        check_out_frame.place(height=680, width=1330, x=10, y=50)
        check_out_frame.config(bd=5, relief=GROOVE)
        Button(check_out_frame, text="Place order", font=("times", 15, "bold"), bg="green", command=place_order).place(x=1150, y=10)
        Label(check_out_frame, text="Order Details", font=("times", 15, "bold")).place(x=500, y=50)
        Label(check_out_frame, text="Name: Priyanka ", font=("times", 15, "bold")).place(x=20, y=100)
        Label(check_out_frame, text="Address: Sec 95,Gurgaon", font=("times", 15, "bold")).place(x=20, y=150)
        Label(check_out_frame, text="Mobile no: 9809812389", font=("times", 15, "bold")).place(x=20, y=200)
        Label(check_out_frame, text="Email address: priya98rajput@gmail.com", font=("times", 15, "bold")).place(x=20,y=250)
        Label(check_out_frame, text="Restaurant: Behrouz Biryani", font=("times", 15, "bold")).place(x=20, y=300)

        item_frame = Frame(master=restaurant1)
        item_frame.place(height=280, width=1300, x=15, y=400)
        item_frame.config(bd=5, relief=GROOVE)
        record = [('Item', 'Quanitity', 'Price')]
        if order1.cget('text') != "":
            record.append((order1.cget('text'), d1.get(), d1_price.cget('text')))
        if order2.cget('text') != "":
            record.append((order2.cget('text'), d2.get(), d2_price.cget('text')))
        if order3.cget('text') != "":
            record.append((order3.cget('text'), d3.get(), d3_price.cget('text')))
        if order4.cget('text') != "":
            record.append((order4.cget('text'), d4.get(), d4_price.cget('text')))
        row = len(record)
        col = len(record[0])
        for i in range(row):
            for j in range(col):
                e = Entry(item_frame, bd=2, width=28, fg='red', font=('Arial', 20, 'bold'))
                if i == 0:
                    e.configure(fg="black")
                e.grid(row=i, column=j)
                e.insert(END, record[i][j])

        final_price = Label(item_frame, text=price_label.cget('text'), font=("times", 20, "bold"))
        final_price.place(x=10, y=230)
        coupon_button=Button(item_frame, text="Add Coupon code", font=("times", 15, "bold"), bg="orange", command=promo_code)
        coupon_button.place(x=1100, y=200)

    else:
        checkout.config(state=DISABLED)
        messagebox.showinfo("cart empty[0]", "Please order something.")

def place_order():
    global check_out_frame, item_frame, restaurant1
    messagebox.showinfo("Order info", "Congratulations! your order is placed successfully😀")
    item_frame.destroy()
    check_out_frame.destroy()
    restaurant1.destroy()

def promo_code():
    global e, code
    code = tkinter.Tk()
    code.title("promo code")
    code.geometry('250x150')
    code.resizable(False, False)
    Label(code, text="Code", font=("times", 15, "bold")).place(x=10, y=20)
    e = Entry(code, bd=2, fg='red', font=('Arial', 10, 'bold'))
    e.place(x=70, y=20)
    Button(code, text="Add Coupon code", font=("times", 15, "bold"), bg="orange", command=coupon_price).place(x=50, y=70)

def coupon_price():
    global final_price, e, code,restaurant1,coupon_button
    if e.get() == "SPECIALS":
        finalprice = final_price.cget('text')
        split_final_price = finalprice.split()
        change_price = int(split_final_price[1]) - int(split_final_price[1]) * 0.30
        final_price.config(text=str(change_price))
        messagebox.showinfo("Success", "Coupon code placed successfully!")
        restaurant1.deiconify()
        code.destroy()
        coupon_button.config(state=DISABLED)

    elif e.get() == "UNLIMITED":
        finalprice = final_price.cget('text')
        split_final_price = finalprice.split()
        change_price = int(split_final_price[1]) - int(split_final_price[1]) * 0.20
        final_price.config(text=str(change_price))
        messagebox.showinfo("Success", "Coupon code placed successfully!")
        restaurant1.deiconify()
        code.destroy()
        coupon_button.config(state=DISABLED)

    else:
        messagebox.showerror("Error", "Coupon code is not correct!")
        restaurant1.deiconify()
        code.destroy()

def back():
    global restaurant1,cart_frame, order1, order2, order3, order4, d1, d2, d3, d4, d1_price, d2_price, d3_price, d4_price
    restaurant1.withdraw()
    filename = "login.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        join_name = list(csvreader)

    print(join_name)
    user = "".join(join_name[0])
    print(user)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sql@#987",
        database="shopping"

    )
    mycursor = mydb.cursor()
    if order1.cget('text') != "":
        if d1.get() != 0:
            mycursor.execute("INSERT into cart(restaurant, item, quantity,price, username) values(%s, %s, %s, %s, %s)",
                             ("Behrouz Biryani", order1.cget('text'), int(d1.get()), d1_price.cget('text'), user))
            mydb.commit()
    if order2.cget('text') != "":
        if d2.get() != 0:
            mycursor.execute("INSERT into cart(restaurant, item, quantity,price, username) values(%s, %s, %s, %s, %s)",
                             ("Behrouz Biryani", order2.cget('text'), int(d2.get()), d2_price.cget('text'), user))
            mydb.commit()
    if order3.cget('text') != "":
        if d3.get() != 0:
            mycursor.execute("INSERT into cart(restaurant, item, quantity,price, username) values(%s, %s, %s, %s, %s)",
                             ("Behrouz Biryani", order3.cget('text'), int(d3.get()), d3_price.cget('text'), user))
            mydb.commit()
    if order4.cget('text') != "":
        if d4.get() != 0:
            mycursor.execute("INSERT into cart(restaurant, item, quantity,price, username) values(%s, %s, %s, %s, %s)",
                             ("Behrouz Biryani", order4.cget('text'), int(d4.get()), d4_price.cget('text'), user))
            mydb.commit()