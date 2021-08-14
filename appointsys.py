from tkinter import *
import sqlite3
import tkinter.messagebox as MessageBox
from tkinter import ttk
from tkcalendar import * #Calender,DateEntry
from tkinter.scrolledtext import *
import mysql.connector as mysql
from tkinter.font import Font
from tkinter import scrolledtext

root = Tk()
root.title('Kenyatta National Cancer Booking System') 
root.geometry('1720x980')

 

#db = Database('book_system.db')

#Register button function
def register():
     #reg = Toplevel()
     #reg.title("Register")
     #reg.geometry('400x400')

     #Database
     #conn = sqlite3.connect('bok_system.db')

     #Create a cursor
     #c = conn.cursor()

     global first_name
     global last_name
     global phone_num
     global email
     global age
     global patid
     global gender

     first_name = StringVar()
     last_name = StringVar()
     phone_num = StringVar()
     email = StringVar()
     age = StringVar()
     patid = StringVar()
     gender = StringVar()


     #Create textbox Label
     first_name_label = Label(root, text="first_name")
     first_name_label.grid(row=5, column=0)
     last_name_label = Label(root, text="last_name")
     last_name_label.grid(row=6, column=0)
     phone_num_label = Label(root, text="phone_num")
     phone_num_label.grid(row=5, column=3)
     email_label = Label(root, text="email")
     email_label.grid(row=6, column=3)
     age_label = Label(root, text="age")
     age_label.grid(row=7, column=0)
#     date_of_birth = Label(
     patid_label = Label(root, text="PatientId")
     patid_label.grid(row=7, column=3)
     gender_label = Label(root, text="Gender")
     gender_label.grid(row=8, column=0)
     

     

     #Create Text Boxes
     first_name_pat = Entry(root, width=20, textvariable = first_name)
     first_name_pat.grid(row=5, column=1)
     last_name_pat = Entry(root, width=20, textvariable = last_name)
     last_name_pat.grid(row=6, column=1)
     phone_num_pat = Entry(root, width=20, textvariable = phone_num)
     phone_num_pat.grid(row=5, column=4)
     email_pat = Entry(root, width=20, textvariable = email)
     email_pat.grid(row=6, column=4)
     age_pat = Entry(root, width=20, textvariable = age)
     age_pat.grid(row=7, column=1)
     patid_pat = Entry(root, width=20, textvariable = patid)
     patid_pat.grid(row=7, column=4)
     gender_pat = Entry(root, width=20, textvariable = gender)
     gender_pat.grid(row=8, column=1)

     

     #Booking button
     button  = Button(root, text="Book", command=insert,  bg="blue")
     button.grid(row=10, column=1) #register

     buton  = Button(root, text="Clear", bg="blue", command=clear) #command=clear,  
     buton.grid(row=10, column=3)    


     nutrition = Label(root, text="YOU CAN CHECK NUTRITIONAL CONTENT OF ANY FOOD SUBSTANCE BELOW!!!   STAY HEALTHY   !!!", bg="blue")
     nutrition.grid(row=12, column=1, columnspan=2)

     space = Label(root, text="")
     space.grid(row=13, column=1)

     global nutval

     nutval = StringVar()
     nutvalLabel = Button(root, text="CHECK YOUR NUTRITIONAL VALUE!!!", bg="green", command=nutvalue)  #, command=nutvalue
     nutvalLabel.grid(row=14, column=2)
     
     
     nutvalLabel_pat = Entry(root, width=30, textvariable = nutval) 
     nutvalLabel_pat.grid(row=14, column=1)

     global nutvalList

     nutvalList = StringVar() 


     nutvalList = Listbox(root, width=70) #, column=()
     nutvalList.grid(row=15, column=1)

     #report = Button(root, text="Report", command=
     #my_button = Button(root, text="Get Date", command=grab_date)
     #my_button.grid(row=8, column=1)

     date_label = Label(root, text="Choose your Date")
     date_label.grid(row=9, column=0)

     cal = Calendar(root, selectmode="day", year=2021, month=7, day=14)
     cal.grid(row=9, column=1)
     my_label = Label(root, text="")
     my_label.grid(row=8, column=3)
    
     conn = sqlite3.connect('bok_system.db', timeout=10)

     #Create a cursor
     c = conn.cursor()

     #c.execute("INSERT INTO nutrients(food) VALUES(calories, sugars, fat, sodium, carbohydrates, protein, fibers)")
     c.commit()
     conn.close()												
#def grab_date():
    #my_label.config(text=cal.get_date())


#from app_database import Database


#report function
def admin():
    bas = sqlite3.connect('bok_system.db', timeout=10)
    cas = bas.cursor()

    cas.execute("SELECT * from patient")
    rews = cas.fetchall()
    for rew in rews:
        nutvalList.insert(END,rew)
    
    bas.commit()
    bas.close()


#function
def nutvalue(): 
    if nutvalList=="":
        fut = sqlite3.connect('book_system.db', timeout=10)
        cur = fut.cursor()

        cur.execute('CREATE Table nutrients(food text)')
        cur.execute("INSERT INTO nutrients(food) VALUES(calories, fat, Sodium, Carbohydrate, Fiber, Sugars, Protein)")
        #if nutval=="spinach":
        cur.execute("SELECT * from nutrients")
        rows = cur.fetchall()
        for row in rows:
        #rac.insert(0, row[0])
            nutvalList.insert(END,row)
        
        #cur.execute("commit")
    #
        fut.commit()
        fut.close()


#Insert function
def insert():
    global first_name
    global last_name
    global phone_num
    global email
    global age
    global patid
    global gender

    #patid = patid.get()   #;
    #first_name = first_name.get()
    #last_name = last_name.get()
    #phone_num = phone_num.get()
    #email = email.get()
    #age = age.get()


    #or patid.get=="098765" 

    if patid.get=="" or first_name.get=="" or last_name.get=="" or phone_num.get=="" or email.get=="" or age.get=="" or gender.get=="":
        MessageBox.showerror("Database Connection", "Enter correct details")



    #if patid.get=="" or first_name.get=="" or last_name.get=="" or phone_num.get=="" or email.get=="" or age.get=="":
    else:
        #con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        #Database
        conn = sqlite3.connect('bok_system.db', timeout=10)

        #Create a cursor
        c = conn.cursor()
        c.execute('CREATE TABLE patient(f_name TEXT, l_name TEXT, phone_num INT, email TEXT, age INT, patid INT)')

        #mysql cursor  IF NOT EXIST
        #cursor = con.cursor()
        #cursor.execute("insert into patient values('"+ str(patid) +"','"+ first_name +"','"+ last_name + "','"+ str(phone_num)+ "','"+ email + "','", + str(age) +"')")

        #if patid.get=="" or first_name.get=="" or last_name.get=="" or phone_num.get=="" or email.get=="" or age.get=="":
        c.execute("INSERT INTO patient (patid, f_name, l_name, phone_num, email, age, Gender) VALUES (?,?,?,?,?,?,?)",(

            patid.get(),   #;
            first_name.get(),
            last_name.get(),
            phone_num.get(),
            email.get(),
            age.get(),
            gender.get(),
             ))
        #if patid =="654321":
        #if patid=="654321": 
        conn.commit()
        conn.close()
        MessageBox.showinfo("Booking Status", "Booked Successfully");     
   




def clear():	
    patid.delete(0, "end")
    first_name.delete(0, "end")
    last_name.delete(0, "end")
    phone_num.delete(0, "end")
    email.delete(0, "end")
    age.delete(0, "end")
	#show()
    MessageBox.showinfo("Delete status", "Deleted Successfully");

      


def clear():	
        patid.delete(0, 'end')
        first_name.delete(0, 'end')
        last_name.delete(0, 'end')
        phone_num.delete(0, 'end')
        email.delete(0, 'end')
        age.delete(0, 'end')
	#show()
        MessageBox.showinfo("Delete status", "Deleted Successfully");
        c.close();



    
def clear():
     f_name.delete(0, END)
     l_name.delete(0, END)
     phone_num.delete(0, END)
     email.delete(0, END)
     age.delete(0, END)

 
#Patient function
def patient():
     #pat = Toplevel()
     #pat.title("Patient booking system")
     #pat.geometry('800x800')
     
     #e = Entry(top, width=35, borderwidth=5)
     #e.grid(row=0, column=0, padx=10, pady=10)
     
     #newLabel = Label(root, text="New Patient? Register here!!!")
     #newLabel.grid(row=1, column=2)

     myLabel = Label(root, text="")
     myLabel.grid(row=8, column=2)

     button  = Button(root, text="Book", command=register,  bg="blue")
     button.grid(row=9, column=1)

     mineLabel = Label(root, text="")
     mineLabel.grid(row=10, column=1)
     
     #myLabel = Label(root, text="Current patient? Book here ")
     #myLabel.grid(row=5, column=2)

     #button  = Button(root, text="Book", command=book, bg="Yellow")
     #button.grid(row=6, column=2, columnspan=2)

     #mineLabel = Label(root, text="")
     #mineLabel.grid(row=8, column=1)

     

#Define out font      
bigFont = Font(
    family="Helvetica",
    size=12,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0)

#Patient button
home = Button(root, command=patient, text="Home", width="20", bg="sky blue") # 
home.grid(row=0, column=0, columnspan="1")

def about():
    contacts_label = Label(root, text="CONTACTS")
    contacts_label.grid(row=2, column=0, columnspan=2)

    
about = Button(root, text="About", width="20", bg="sky blue", command="about")
about.grid(row=0, column=1)


        
admin  = Button(root, text="Report", width="20", command=admin, bg="sky blue")
admin.grid(row=0, column=2)

contacts = Label(root, text="CONTACTS", font=bigFont)
contacts.grid(row=0, column=3)

num = Label(root, text="0756724528(Dr. Okiri Bob)", font=bigFont)
num.grid(row=0, column=4)

num1 = Label(root, text="0745356534(Dr. Cynthia Aketch)", font=bigFont)
num1.grid(row=1, column=4)



root.mainloop()


