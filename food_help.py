import tkinter
from tkinter import *
import webbrowser

def help():
    global main_frame,partner_onb_frame,root
    root = tkinter.Tk()
    root.title('Help page')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.resizable(False, False)
    root.configure(bg="#9f96fc")

    main_frame = Frame(master=root)
    main_frame.place(height=550, width=1300, x=20, y=120)
    main_frame.config(bd=5, relief=RIDGE)
    Label(root, text=" Help & Support ", font=("Arial", 20, "bold"),bg="#9f96fc").place(x=10, y=25)
    Label(root, text="     Let's take a step ahead and help you better.", font=("Arial", 10, "italic"),bg="#9f96fc").place(x=10, y=68)

    side_frame = Frame(master=main_frame)
    side_frame.place(height=450, width=250, x=20, y=30)
    side_frame.config(bd=5, relief=RIDGE)
    Button(side_frame,text = "Partner Onboarding", font=('times', 15, 'bold'), command=partner_onboarding).place(x=10, y=20)
    Button(side_frame,text = "Legal                       ", font=('times', 15, 'bold'), command=legal).place(x=10, y=80)
    Button(side_frame,text = "FAQs                       ", font=('times', 15, 'bold'), command=faq).place(x=10, y=140)

    middle_frame = Frame(master=main_frame)
    middle_frame.place(height=450, width=980, x=300, y=30)
    middle_frame.config(bd=5, relief=RIDGE)
    Button(root,text = "Back", font=('times', 15, 'bold'), command=back).place(x=600, y=680)
    root.mainloop()

def back():
    global root
    root.destroy()

def partner_onboarding():
    global partner
    partner_onb_frame = Frame(master=main_frame)
    partner_onb_frame.place(height=450, width=980, x=300, y=30)
    partner_onb_frame.config(bd=5, relief=RIDGE)
    Label(partner_onb_frame,text='Partner Onboarding', font=('times', 20, 'bold')).place(x=20, y=20)
    mb = Menubutton(partner_onb_frame, text="I want to partner my restaurant with Foodiz",font=('Arial', 15, 'italic','bold') ,relief=RAISED)
    mb.place(x=20, y=40)
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    partner = StringVar()
    mb.menu.add_checkbutton(label="Partner with us?...send an email to: priyanka89@gmail.com",variable=partner, command=send_mail)
    mb.config(fg="orange")
    mb.place(x=40, y=60)

    mb1 = Menubutton(partner_onb_frame, text="What are the mandatory documents needed to list my restaurant on Foodiz?",font=('Arial', 15, 'italic','bold') ,relief=RAISED)
    mb1.place(x=20, y=80)
    mb1.menu = Menu(mb1, tearoff=0)
    mb1["menu"] = mb1.menu
    mb1.menu.add_checkbutton(label="-  (1) Copies of the below documents are mandatory "
                                "(2)FSSAI Licence OR FSSAI Acknowledgement "
                                " (3)Pan Card "
                                "  (4)GSTIN Certificate "
                                "  (5)Cancelled Cheque OR bank Passbook "
                                "  (6)Menu")
    mb1.config(fg="orange")
    mb1.place(x=40, y=100)

    mb2 = Menubutton(partner_onb_frame, text="After I submit all documents, how long will it take for my restaurant to go live on Foodiz?",
                                        font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb2.place(x=20, y=120)
    mb2.menu = Menu(mb2, tearoff=0)
    mb2["menu"] = mb2.menu
    mb2.menu.add_checkbutton(label="After all mandatory documents have been received and verified it takes upto 7-10 working days"
                                   " for the onboarding to be completed and make your restaurant live on the platform.")
    mb2.config(fg="orange")
    mb2.place(x=40, y=140)

    mb3 = Menubutton(partner_onb_frame,text="What is this one time Onboarding fees? Do I have to pay for it while registering?",
                                         font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb3.place(x=20, y=160)
    mb3.menu = Menu(mb3, tearoff=0)
    mb3["menu"] = mb3.menu
    mb3.menu.add_checkbutton(label="This is a one-time fee charged towards the system & admin costs incurred during the onboarding process."
                                    " It is deducted from the weekly payouts after you start receiving orders from Swiggy.")
    mb3.config(fg="orange")
    mb3.place(x=40, y=180)

    mb4 = Menubutton(partner_onb_frame,text="Who should I contact if I need help & support in getting onboarded?",
                     font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb4.place(x=20, y=200)
    mb4.menu = Menu(mb4, tearoff=0)
    mb4["menu"] = mb4.menu
    mb4.menu.add_checkbutton(label="You can connect with Partner Support on 080-67466777/68179777 or write to partnersuport@swiggy.in",
                             variable=partner,command=send_mail)
    mb4.config(fg="orange")
    mb4.place(x=40, y=220)

    mb5 = Menubutton(partner_onb_frame, text="How much commission will I be charged by Swiggy?",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb5.place(x=20, y=240)
    mb5.menu = Menu(mb5, tearoff=0)
    mb5["menu"] = mb5.menu
    mb5.menu.add_checkbutton(label="The commission charges vary for different cities. You will be able to see the commission applicable "
                                   "for you once the preliminary onboarding details have been filled.")
    mb5.config(fg="orange")
    mb5.place(x=40, y=260)

    mb6 = Menubutton(partner_onb_frame, text="I don’t have an FSSAI licence for my restaurant. Can it still be onboarded?",
                     font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb6.place(x=20, y=280)
    mb6.menu = Menu(mb6, tearoff=0)
    mb6["menu"] = mb6.menu
    mb6.menu.add_checkbutton(label="FSSAI licence is a mandatory requirement according to the government’s policies. "
                                   "However, if you are yet to receive the licence at the time of onboarding, you can proceed "
                                   "with the acknowledgement number which you will have received from FSSAI for your registration.")
    mb6.config(fg="orange")
    mb6.place(x=40, y=300)

def send_mail():
    webbrowser.open("https://accounts.google.com/ServiceLogin/signinchooser?")

def legal():
    global main_frame
    legal_frame = Frame(master=main_frame)
    legal_frame.place(height=450, width=980, x=300, y=30)
    legal_frame.config(bd=5, relief=RIDGE)
    Label(legal_frame, text='Legal', font=('times', 20, 'bold')).place(x=20, y=20)
    mb = Menubutton(legal_frame, text="Terms of Use",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb.place(x=20, y=40)
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    mb.menu.add_checkbutton(label="These terms of use (the 'Terms of Use') govern your use of our website www.swiggy.in " 
                                "(the 'Website') and our 'Swiggy' application for mobile and handheld devices (the 'App')")

    mb.config(fg="orange")
    mb.place(x=40, y=60)

    mb1 = Menubutton(legal_frame, text="Privacy Policy",font=('Arial', 15, 'italic','bold') ,relief=RAISED)
    mb1.place(x=20, y=80)
    mb1.menu = Menu(mb1, tearoff=0)
    mb1["menu"] = mb1.menu
    mb1.menu.add_checkbutton(label="We ( Bundl Technologies Private Limited, alias 'foodiz' ) are fully committed to " 
                                    "respecting your privacy and shall ensure that your personal information is safe with us.")
    mb1.config(fg="orange")
    mb1.place(x=40, y=100)

    mb2 = Menubutton(legal_frame, text="Cancellations and Refunds",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb2.place(x=20, y=120)
    mb2.menu = Menu(mb2, tearoff=0)
    mb2["menu"] = mb2.menu
    mb2.menu.add_checkbutton(label="Foodiz reserves the right to charge you cancellation fee for the orders constrained to be cancelled by "
                                   "Foodiz for reasons not attributable to Foodiz.")
    mb2.config(fg="orange")
    mb2.place(x=40, y=140)

    mb3 = Menubutton(legal_frame,text="Terms of Use for Foodiz ON-TIME / Assured",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb3.place(x=20, y=160)
    mb3.menu = Menu(mb3, tearoff=0)
    mb3["menu"] = mb3.menu
    mb3.menu.add_checkbutton(label="These terms of use (the 'Terms of Use') that govern your use of our service Foodiz "
                                   "ON-TIME / Assured  ('ON-TIME' / 'Assured') on our website www.Foodiz.in (the 'Website') ")
    mb3.config(fg="orange")
    mb3.place(x=40, y=180)

def faq():
    global main_frame
    faq_frame = Frame(master=main_frame)
    faq_frame.place(height=450, width=980, x=300, y=30)
    faq_frame.config(bd=5, relief=RIDGE)
    Label(faq_frame, text='FAQs', font=('times', 20, 'bold')).place(x=20, y=20)
    mb = Menubutton(faq_frame, text="What is Swiggy Customer Care Number?", font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb.place(x=20, y=60)
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    email=StringVar()
    mb.menu.add_checkbutton(label="You no longer have to go through the maze of an IVRS call support. "
                                    "You can email us your issue on support@foodiz.in",variable=email,command=send_mail)

    mb.config(fg="orange")
    mb.place(x=40, y=80)

    mb1 = Menubutton(faq_frame, text="I want to explore career opportunities with Swiggy.", font=('Arial', 15, 'italic', 'bold'),relief=RAISED)
    mb1.place(x=20, y=100)
    mb1.menu = Menu(mb1, tearoff=0)
    mb1["menu"] = mb1.menu
    mb1.menu.add_checkbutton(label="Join our team! send an email to support@foodiz.in ", variable=email, command=send_mail)

    mb1.config(fg="orange")
    mb1.place(x=40, y=120)

    mb2 = Menubutton(faq_frame,text="I want to provide feedback",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb2.place(x=20, y=140)
    mb2.menu = Menu(mb2, tearoff=0)
    mb2["menu"] = mb2.menu
    mb2.menu.add_checkbutton(label="send an email",variable=email, command=send_mail)
    mb2.config(fg="orange")
    mb2.place(x=40, y=160)

    mb3 = Menubutton(faq_frame,text="Can I edit my order?",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb3.place(x=20, y=180)
    mb3.menu = Menu(mb3, tearoff=0)
    mb3["menu"] = mb3.menu
    mb3.menu.add_checkbutton(label="Your can edit your order by calling contact customer support"
                                   "but once the restaurants starts preparing it,you may not edit.")
    mb3.config(fg="orange")
    mb3.place(x=40, y=200)

    mb4 = Menubutton(faq_frame, text="I want to cancel my order",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb4.place(x=20, y=220)
    mb4.menu = Menu(mb4, tearoff=0)
    mb4["menu"] = mb4.menu
    mb4.menu.add_checkbutton(label="We will do our best to accommodate your request if the order is not "
                                   "placed to the restaurant (Customer service number:  080-67466729) but we have the right to charge cancellation fee.")
    mb4.config(fg="orange")
    mb4.place(x=40, y=240)

    mb5 = Menubutton(faq_frame, text="Is there a minimum order value?",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb5.place(x=20, y=260)
    mb5.menu = Menu(mb5, tearoff=0)
    mb5["menu"] = mb5.menu
    mb5.menu.add_checkbutton(label="We have no minimum order value and you can order for any amount. ")
    mb5.config(fg="orange")
    mb5.place(x=40, y=280)

    mb6 = Menubutton(faq_frame, text="Do you charge for delivery?",font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb6.place(x=20, y=300)
    mb6.menu = Menu(mb6, tearoff=0)
    mb6["menu"] = mb6.menu
    mb6.menu.add_checkbutton(label="Delivery fee varies from city to city and is applicable if order value is below a certain amount.")
    mb6.config(fg="orange")
    mb6.place(x=40, y=320)

    mb7 = Menubutton(faq_frame, text="How long do you take to deliver?", font=('Arial', 15, 'italic', 'bold'), relief=RAISED)
    mb7.place(x=20, y=340)
    mb7.menu = Menu(mb7, tearoff=0)
    mb7["menu"] = mb7.menu
    mb7.menu.add_checkbutton(label="Standard delivery times vary by the location selected and prevailing conditions. Once you select your location, an estimated delivery time is mentioned for each restaurant.")
    mb7.config(fg="orange")
    mb7.place(x=40, y=360)

