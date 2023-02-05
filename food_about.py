import tkinter
from tkinter import *

def about():
    global temp
    temp = tkinter.Toplevel()
    temp.title('About page')
    width = temp.winfo_screenwidth()
    height = temp.winfo_screenheight()
    temp.geometry("%dx%d" % (width, height))
    temp.resizable(False,False)
    bg_about = PhotoImage(file=r"C:\Users\Admin\Downloads\images.png")
    canvas_about = Canvas(master=temp, width=100, height=100)
    canvas_about.pack(fill="both", expand=True)
    canvas_about.create_image(550, 0, image=bg_about, anchor="nw")
    Label(temp, text="______F   O   O   D   I   Z______", font=("Arial", 20, "italic","bold"),fg="orange").place(x=500, y=80)

    Label(temp, text='Founder : Miss. Priyanka Rajput', font=('Arial', 20, 'bold')).place(x=10, y=150)
    text = ("Foodiz has been successfully been through its ups and downs but what has majorly contributed in the "
                   "company’s success is the will and dedication of its founders. The consistent efforts put "
                   "in by the team to adapt to everyday changes in the trends and the passion "
                   "to serve as many people as possible with a standard experience is what founders: Priyanka Rajput, Sangeeta Rajput."
                    "They have believed in and inculcated into the ethics and culture at Foodiz."
                     "Foodiz was started in a small office space in Koramangala, Bangalore and the company started off with limitations."
                    " The initial setup of food delivery was targeted at a single neighbourhood with 25 partner restaurants. ")
    msg1 = Message(temp,text=text,width=1350)
    msg1.config(bg='lightgreen', font=('times', 20, 'italic'))
    msg1.place(x=0,y=190)

    Label(temp, text='Co-Founder : Miss. Sangeeta Rajput', font=('Arial', 20, 'bold')).place(x=10, y=420)
    text2 =(" Foodiz can be called a second entrepreneurial venture of co-founder Sangeeta Rajput.,"
                        " first one being, Bundl. Both the co-founders ate alumni of BITS, Pilani and after years of working and "
                        "interning, they got together to introduce their joint venture, Bundle which is a logistics aggregator "
                        "that joins together SMEs to Courier Service Providers.\n The business was doing perfectly fine but the "
                        "founders were not satisfied and realised that there is a great unexplored potential in the food industry of India."
                        "On the footprints of logistics, both the founders wanted something in the food industry which was related to technology"
                        " and operational offline as well.")
    msg2 = Message(temp,text=text2,width=1350)
    msg2.config(bg='lightgreen', font=('times', 20, 'italic'))
    msg2.place(x=0,y=460)

    Button(master=temp,text="   Back   ",font=("Arial",15,"bold"),command=back).place(x=600,y=680)
    temp.mainloop()

def back():
    global temp
    temp.destroy()