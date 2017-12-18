from Tkinter import *

import  sqlite3


#connection with database
conn = sqlite3.connect('hotel.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

import tkMessageBox




def a_frame():
    a_frame().Tkraise()
root = Tk()








# create the function of login



def login():
    username = text1.get()
    password = text2.get()

    if username == '123' and password == '123':
        username = text1.delete(0,END)
        password = text2.delete(0,END)

        root1 = Tk()
        root1.geometry("970x640")
        def logout():
            root1.destroy()
        # set front size of application

        root1.title("Hotel Reservation Management System")

        # set the lables background images and textboxes with thier properties
        la1 = Label(root1, text="Hotel Reservation Management System", fg="white", bg="brown",
                   font=('airal', 30, 'bold')).pack(side  =TOP)


        guest= Button(root1, fg="white", bg="darkgray",
                     font=('airal', 20), text="Guests Registration", command=guests, bd=10,width = 20)
        guest.pack(padx= 10,pady =10)


        guestsinfoo = Button(root1, fg="white", bg="darkgray",
                       font=('airal', 20), text="Guests information", command=guestsinfo, bd=10, width=20)
        guestsinfoo.pack(padx= 10,pady =10)

        roominfo = Button(root1, fg="white", bg="darkgray",
                       font=('airal', 20), text="Rooms information", command=roomsinfo, bd=10, width=20)
        roominfo.pack(padx= 10,pady =10)
        log = Button(root1, fg="white", bg="darkgray",
                          font=('airal', 20), text="Logout", command=logout, bd=10, width=20)
        log.pack(padx= 10,pady =10)









    else:
        tkMessageBox.showwarning("Warning","Incorrect Username or Password")

#create exit     function

    # create logout function





    def exit():

        sys.exit()



#create guest window
def guests():
    root3 =Tk()


    root3.geometry("970x1000")


    def exit():
        root3.destroy()

        # create insert function
    def insert():


        t1 = text1.get()
        t2 = text2.get()
        t3 = text3.get()
        t4 = text4.get()
        t5 = text5.get()
        t6 = text6.get()
        t7 = text7.get()
        t8 = text8.get()
        t9 = text9.get()

        if c.execute("INSERT INTO guests (guest_id,firstname,lastname,address,phone_no,check_in_date,check_out_date,payment_method,room_number) VALUES (?,?,?,?,?,?,?,?,?)",
                (t1,t2,t3,t4,t5,t6,t7,t8,t9)) :
            conn.commit()
            text1.delete(0, END)
            text2.delete(0, END)
            text3.delete(0, END)
            text4.delete(0, END)
            text5.delete(0, END)
            text6.delete(0, END)
            text7.delete(0, END)
            text8.delete(0, END)
            text9.delete(0, END)
            tkMessageBox.showinfo("Submit", "A row added successfully")
        else:
            tkMessageBox.showwarning("Warning", "Something went wrong or database has been locked")


    # set front size of application
    root3.title("Hotel Reservation Management System")


    # set the lables background images and textboxes with thier properties
    la1 = Label(root3, text="Hotel Reservation Management System", fg="white", bg="brown",
                font=('airal', 30, 'bold'))
    la1.pack(side  =TOP)

    label1 = Label(root3, text="Guest_id", fg="gray", bg="black",
               font=('airal', 12, 'bold')).pack(padx = 5)
    text1 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12), textvariable=StringVar())
    text1.pack(padx= 10,pady =10)
    label2 = Label(root3, text="Firstname", fg="gray", bg="black",
               font=('airal', 12, 'bold')).pack(padx = 5)
    text2= Entry(root3, fg="black", bg="white",
                  font=('airal', 12),textvariable=StringVar())
    text2.pack(padx= 10,pady =10)
    label3 = Label(root3, text="Lastname", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text3 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12),  textvariable=StringVar())
    text3.pack(padx= 10,pady =10)
    label4 = Label(root3, text="Address", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text4 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12), textvariable=StringVar())
    text4.pack(padx= 10,pady =10)
    label5= Label(root3, text="Phone#", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text5 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12),  textvariable=StringVar())
    text5.pack(padx= 10,pady =10)
    label6= Label(root3, text="Check_in_date", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text6 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12),  textvariable=StringVar())
    text6.pack(padx= 10,pady =10)

    label7= Label(root3, text="Check_out_date", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text7 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12),  textvariable=StringVar())
    text7.pack(padx= 10,pady =10)

    label8 = Label(root3, text="Payment Method", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text8 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12),textvariable=StringVar())
    text8.pack(padx= 10,pady =10)

    label9= Label(root3, text=" Registered Room Number", fg="gray", bg="black",
                   font=('airal', 12, 'bold')).pack(padx = 5)
    text9 = Entry(root3, fg="black", bg="white",
                  font=('airal', 12),textvariable=StringVar())
    text9.pack(padx= 10,pady =10)

    btn = Button(root3, fg="black", bg="white",
                 font=('airal', 12), text="Add", command=insert,width = 20)
    btn.pack(pady= 10)
    btnquite = Button(root3, fg="black", bg="white",
                      font=('airal', 12) ,width = 20,text="Exit", command=exit)
    btnquite.pack(pady = 10)







    #create rooms function
def roomsinfo():
    root4 = Tk()
    root4.geometry("970x880")
    root4.title("Hotel Reservation Management System")

    # set the lables background images and textboxes with thier properties
    l1 = Label(root4, text="Hotel Reservation Management System", fg="white", bg="brown",
               font=('airal', 30, 'bold'))
    l1.pack(side=TOP)



    def exit():
        root4.destroy()
    def insert():


        t1 = text1.get()
        t2 = text2.get()
        t3 = text3.get()


        if c.execute("INSERT INTO room (room_no,rate,type) VALUES (?,?,?)",
                (t1,t2,t3)) :
            conn.commit()
            tkMessageBox.showinfo("Submit", "A row added successfully")
            text1.delete(0, END)
            text2.delete(0, END)
            text3.delete(0, END)




        else:
            tkMessageBox.showwarning("Warning", "Something went wrong or database has been locked")


    label1 = Label(root4, text="Room Number", fg="gray", bg="black",
                   font=('airal', 15, 'bold')).pack(pady=50)
    text1 = Entry(root4, fg="black", bg="white",
                  font=('airal', 15), textvariable=StringVar())
    text1.pack(pady = 5)

    label2 = Label(root4, text="Rate", fg="gray", bg="black",
                   font=('airal', 15, 'bold')).pack(pady=50)
    text2 = Entry(root4, fg="black", bg="white",
                  font=('airal', 15), textvariable=StringVar())
    text2.pack(pady = 5)

    label3 = Label(root4, text="Type", fg="gray", bg="black",
                   font=('airal', 15, 'bold')).pack(pady=50)
    text3 = Entry(root4, fg="black", bg="white",
                  font=('airal', 15), textvariable=StringVar())
    text3.pack(pady=5)

    btn = Button(root4, fg="black", bg="white",
                 font=('airal', 15), text="Add", command=insert, width=50)
    btn.pack(pady=20)
    btnquite = Button(root4, fg="black", bg="white",
                      font=('airal', 15), width=50, text="Exit", command=exit)
    btnquite.pack(pady=20)


#create guestsinformation function

def guestsinfo():
    root5 = Tk()
    root5.geometry("970x880")
    root5.title("Hotel Reservation Management System")

    # set the lables background images and textboxes with thier properties
    l1 = Label(root5, text="Hotel Reservation Management System", fg="white", bg="brown",
               font=('airal', 30, 'bold'))
    l1.pack(side=TOP)
    scrollbar = Scrollbar(root5)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root5, width=970, height=880,font = ('arial',20,'bold'),fg= "dark green")
    listbox.pack()
    listbox.focus_set()
    r = c.execute("SELECT * from guests")
    e = c.fetchone()
    t = e.keys()





    for i in r.fetchall() or t:
        listbox.insert(END,*map(unicode,i))
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)


#create registration function







#set front size of application
root.geometry("970x880")
root.title("Hotel Reservation Management System")

#set the lables background images and textboxes with thier properties
l1 = Label(root,text="Hotel Reservation Management System",fg = "black",bg = "white",
           font = ('arial',30,'bold'))
l1.pack(side = TOP)

#set the image

canvas = Canvas(width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

image = PhotoImage(file = "C:\Users\MEHREEN\PycharmProjects\hotel\image.gif")
canvas.create_image(10, 10, image = image, anchor = NW)



l2 = Label(root,text="Please enter your Username and Password to Login",fg = "white",bg = "gray",
           font = ('airal',20,'bold'))
l2.pack(padx = 30,pady=30)



l3 = Label(root,text="Username",fg = "gray",bg = "black",
           font = ('airal',15,'bold'),bd = 10)

l3.pack(pady = 10,padx= 10)


text1 = Entry(root,fg = "black",bg = "white",
           font = ('airal',15),bd = 10,textvariable = StringVar())
text1.pack(pady = 10,padx= 10)





l4 = Label(root,text="Password",fg = "gray",bg = "black",
           font = ('airal',15,'bold'))
l4.pack(pady = 10,padx= 10)

text2 = Entry(root,fg = "black",bg = "white",
           font = ('airal',15),bd = 10,textvariable =StringVar(),show  ='*')
text2.pack(pady = 10,padx= 10)


#create login button
btn = Button(root,fg = "black",bg = "white",
           font = ('airal',15),text = "Login",command = login)
btn.pack(pady = 10,padx= 10)
btnquite= Button(root,fg = "black",bg = "white",
           font = ('airal',15),text = "Exit",command  = exit)
btnquite.pack(pady = 10,padx= 10)









root.mainloop()