from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql


def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "admin" and password == "login@123":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        login_successful()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")




def passenger():
    
    master = Tk()
    master.geometry("500x400")
    master.title( "Passengers details" )

    textName = StringVar()
    textDob = StringVar()
    textPassnum = StringVar()
    textAdh = StringVar()
    textNat = StringVar()
    

    Label(master, text="Passenger-Name : ").grid(row=0)
    Label(master, text="Date Of Birth : ").grid(row=1)
    Label(master, text="Pass Number : ").grid(row=2)
    Label(master, text="Passenger Aadhar : ").grid(row=3)
    Label(master, text="Nationality : ").grid(row=4)
    

    
    Message(master, text="*** NOTE : Enter the Correct details of the Passengers***",font=("times new roman", 10, "bold"), width = 200).grid(row=19)

    name= Entry(master,text =textName)
    dob= Entry(master,text = textDob)
    passnum= Entry(master,text = textPassnum)
    aadhar = Entry(master,text = textAdh)  
    nationality = Entry(master,text = textNat) 
    
    def done():
        texta = "{}".format(name.get())
        textb = "{}".format(dob.get())
        textc = "{}".format(passnum.get())
        texte = "{}".format(aadhar.get())
        textf = "{}".format(nationality.get())
        
        print(texta)

        dataa = (texta, textb, textc,texte,textf)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Passenger VALUES""" + str(dataa))
        db.commit()
        cursor.execute("""SELECT * FROM Passenger;""")
        print(cursor.fetchall())

        db.close()

    def deletePassenger():
        deletePass = Tk()
        deletePass.geometry("700x220")
        deletePass.title("Delete Passenger")

        deletePassInput = StringVar()

        Label(deletePass, text="Pass number : ").grid(row=0)
        
        Label(deletePass, text="NOTE : Enter the valid passenger name ",font=("times new roman", 10, "bold")).grid(row=2)

        passDelete = Entry(deletePass, text=deletePassInput)
        passDelete.grid(row=0, column=1)
            
        def delete():
            texta = "{}".format(passDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''
            cursor.execute("""DELETE FROM Passenger WHERE passnum=""" + str(dataa))
            cursor.execute("""SELECT * FROM passenger;""")
            
            print(cursor.fetchall())
                
            db.close()

        Buttonh = Button(deletePass, text="Done", command=delete,bg="#4CAF50",fg="white").place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done,bg="#4CAF50",fg="white").place(x=20, y=300)
    Buttong = Button(master, text="Delete Passenger",command=deletePassenger,bg="red",fg="white").place(x=20, y=330)

    name.grid(row=0, column=1)
    dob.grid(row=1, column=1)
    passnum.grid(row=2, column=1)
    aadhar.grid(row=3, column=1)
    nationality.grid(row=4, column=1)
def ticket():

    master = Tk()
    master.geometry("500x250")
    master.title("Tickets")

    textTicketNum = StringVar()
    textSeatNum = StringVar()
    textSfrom=StringVar()
    textTo=StringVar()

    Label(master, text="Ticket Number : ").grid(row=0)
    Label(master, text="Seat Number : ").grid(row=1,pady=5)
    Label(master, text="From : ").grid(row=2)
    Label(master, text="To : ").grid(row=3,pady=5)
    
   
    Label(master, text="NOTE : Enter the details to Book the tickets ",font=("times new roman", 10, "bold")).grid(row=16)

#Change seat number

    ticketNum = Entry(master, text=textTicketNum)
    seatNum = Entry(master, text=textSeatNum)
    sfrom=Entry(master, text=textSfrom)
    to=Entry(master, text=textTo)

    def done():

        texta = "{}".format(ticketNum.get())
        textb = "{}".format(seatNum.get())
        textc = "{}".format(sfrom.get())
        textd = "{}".format(to.get())
        print(texta)

        dataa = (texta, textb, textc,textd)
        print(dataa)


        db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)
        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Ticket VALUES""" + str(dataa))
        db.commit()


        cursor.execute("""SELECT * FROM Ticket;""")

        print(cursor.fetchall())

        db.close()

        
    def deleteTicket():


        deleteTick = Tk()
        deleteTick.geometry("450x220")
        deleteTick.title("Delete Tickets")

        deleteTickInput = StringVar()

        Label(deleteTick, text="Ticket Number: ").grid(row=0)

        Label(deleteTick, text="NOTE : Enter the valid Ticket number that to be deleted",font=("times new roman", 10, "bold")).grid(row=2)

        ticketDelete = Entry(deleteTick, text=deleteTickInput)

        ticketDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(ticketDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Ticket WHERE ticketNum="""+str(dataa));
            cursor.execute("""SELECT * FROM Ticket;""")

            print(cursor.fetchall())

            db.close()


        Buttonf = Button(deleteTick, text="Done", command=delete, bg="#4CAF50",fg="white").place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50",fg="white").place(x=20, y=150)
    Buttong = Button(master, text="Delete Ticket", command=deleteTicket, bg="red",fg="white").place(x=20, y=180)

    ticketNum.grid(row=0, column=1)
    seatNum.grid(row=1, column=1,pady=5)
    sfrom.grid(row=2, column=1)
    to.grid(row=3, column=1,pady=5)


def flight():

    master = Tk()
    master.geometry("500x360")
    master.title("Flights")

    textFlightId = StringVar()
    textFlightTerm = StringVar()
    textFlighname = StringVar()
    textArrival = StringVar()
    textDeparture = StringVar()
    textDuration = StringVar()
    textCost = StringVar()

    Label(master, text="Flight I.D : ").grid(row=0)
    Label(master, text="Flight Terminal : ").grid(row=1,pady=5)
    Label(master, text="Flight Name : ").grid(row=2)
    Label(master, text="Flight Arrival : ").grid(row=3,pady=5)
    Label(master, text="Flight Departure : ").grid(row=4,pady=5)
    Label(master, text="Journey Duration : ").grid(row=5,pady=5)
    Label(master, text="Cost : ").grid(row=6)
    
    Message(master, text="NOTE : Enter the correct Flight Details",font=("times new roman", 10, "bold"),width = 200).grid(row=24)


    flightId = Entry(master, text=textFlightId)
    flightTerm = Entry(master, text=textFlightTerm)
    flightname = Entry(master, text=textFlighname)
    arrival = Entry(master, text=textArrival)
    departure = Entry(master, text=textDeparture)
    duration = Entry(master, text=textDuration)
    cost = Entry(master, text=textCost)



    def done():

        texta = "{}".format(flightId.get())
        textb = "{}".format(flightTerm.get())
        textc = "{}".format(flightname.get())
        textd = "{}".format(arrival.get())
        texte = "{}".format(departure.get())
        textf= "{}".format(duration.get())
        textg = "{}".format(cost.get())
        print(texta)

        dataa = (texta, textb, textc, textd,texte, textf, textg)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Flight VALUES""" + str(dataa))
        db.commit()
        cursor.execute("""SELECT * FROM Flight;""")

        print(cursor.fetchall())

        db.close()

       

    def deleteFlight():
        deleteFli = Tk()
        deleteFli.geometry("700x220")
        deleteFli.title("Delete Flights")

        deleteFliInput = StringVar()

        Label(deleteFli, text="Flight ID: ").grid(row=0)
    
        Label(deleteFli, text="NOTE : Enter the valid Flight Id that to be deleted ",font=("times new roman", 10, "bold")).grid(row=2)

        fliDelete = Entry(deleteFli, text=deleteFliInput)

        fliDelete.grid(row=0, column=1)


        def delete():
            texta = "{}".format(fliDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Flight WHERE flightId=""" + str(dataa));

            cursor.execute("""SELECT * FROM Flight;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deleteFli, text="Done", command=delete, bg="#4CAF50",fg="white").place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50",fg="white").place(x=20, y=280)
    Buttong = Button(master, text="Delete flight", command=deleteFlight, bg="red",fg="white").place(x=20, y=310)

    flightId.grid(row=0, column=1)
    flightTerm.grid(row=1, column=1,pady=5)
    flightname.grid(row=2, column=1)
    arrival.grid(row=3, column=1,pady=5)
    departure.grid(row=4, column=1)
    duration.grid(row=5, column=1,pady=5)
    cost.grid(row=6, column=1)

def Essentials():

    master = Tk()
    master.geometry("850x300")
    master.title("Other Essentials")

    textPackage = StringVar()
    textFood = StringVar()
    textOrderid = StringVar()
    textDrinks = StringVar()
    textOrders = StringVar()

    Label(master, text="Package Weight: ").grid(row=0)
    Label(master, text="Food: ").grid(row=1)
    Label(master, text="Order-ID(Food): ").grid(row=2)
    Label(master, text="Drinks: ").grid(row=3)
    Label(master, text="Order-ID(Drinks): ").grid(row=4)


    package_weight= Entry(master, text = textPackage)
    foods= Entry(master,  text = textFood)
    ordid1= Entry(master,  text = textOrderid)
    drinks = Entry(master,  text = textDrinks)
    ordid2 = Entry(master, text=textOrders)


    def done():
        texta = "{}".format(package_weight.get())
        textb = "{}".format(foods.get())
        textc = "{}".format(ordid1.get())
        textd = "{}".format(drinks.get())
        texte = "{}".format(ordid2.get())
        print(texta)

        dataa = (texta, textb, textc, textd, texte)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Jawad@2003', db='airlines',autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO essential values""" + str(dataa));
        db.commit()


        cursor.execute("""SELECT * FROM essential;""")

        print(cursor.fetchall())

        db.close()

        #print('"{}"'.format(name.get()))
       # print(texta)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50",fg="white").place(x=20, y=270)

    package_weight.grid(row=0, column=1)
    foods.grid(row=1, column=1)
    ordid1.grid(row=2, column=1)
    drinks.grid(row=3, column=1)
    ordid2.grid(row=4, column=1)
    
def login_successful():
    # Hide the login form
    root = Tk()
    root.title("Air Reservation System")
    root.geometry("400x400")
    root.config(bg="#F0F0F0")
    

    # Create the main application window
    

    # Create and place the welcome label
    label = tk.Label(root, text="WELCOME TO THE AIR RESERVATION SYSTEM", font=("Algerian", 30, "bold"), fg="#0052CC", bg="#F0F0F0")
    label.pack(pady=20)

    # Create buttons with creative colors and fonts
    myButtonb = tk.Button(root, text="Flights", command=flight, font=("arial black", 18, "bold"), fg="#FFFFFF", bg="#0052CC", activeforeground="#FFFFFF", activebackground="#003399")
    myButtonb.pack(pady=20)

    myButtonc = tk.Button(root, text="Tickets", command=ticket, font=("arial black", 18), fg="#FFFFFF", bg="#009933", activeforeground="#FFFFFF", activebackground="#006600")
    myButtonc.pack(pady=20)

    myButtone =Button(root, text = "Passenger", command=passenger, font=("Arial black", 18), fg="#FFFFFF", bg="#CC3300", activeforeground="#FFFFFF", activebackground="#993300")
    myButtone.pack(pady=20)
    
    myButtond = Button(root, text = "Essentials", command=Essentials, font=("Arial black", 18), fg="#FFFFFF", bg="#CC0000", activeforeground="#FFFFFF", activebackground="#990000")
    myButtond.pack(pady=20)

 
    root.mainloop()
parent = tk.Tk()
parent.title("Login Form")
parent.geometry("300x200")

# Create a frame for the form
form_frame = tk.Frame(parent, padx=20, pady=20)
form_frame.pack()

# Create and place the username label and entry
username_label = tk.Label(form_frame, text="User-Id:", font=("times new roman", 10, "bold"))
username_label.grid(row=0, column=0, sticky="e")

username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1)

# Create and place the password label and entry
password_label = tk.Label(form_frame, text="Password:", font=("times new roman", 10, "bold"))
password_label.grid(row=1, column=0, sticky="e",pady=10)

password_entry = tk.Entry(form_frame, show="*")  # Show asterisks for password
password_entry.grid(row=1, column=1,pady=10)

# Create and place the login button
login_button = tk.Button(form_frame, text="Login", command=validate_login,font=("times new roman", 10, "bold"),bg="#4CAF50",fg="white")
login_button.grid(row=5, column=0, columnspan=4,pady=15)

# Set the background color
parent.configure(bg="#f0f0f0")

# Set the label and entry colors
username_label.configure(bg="#f0f0f0", fg="black")
password_label.configure(bg="#f0f0f0", fg="black")

username_entry.configure(bg="#ffffff", fg="black")
password_entry.configure(bg="#ffffff",fg="black")

# Start the Tkinter event loop
parent.mainloop()




