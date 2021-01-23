def adddatas():
    def submitadd():
        firstname = firstnameval.get()
        lastname = lastnameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        #dob = dobval.get()
        addedtime = time.strftime('%H:%M:%S')
        addeddate = time.strftime('%d/%m/%Y')
        print(addedtime)

        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(firstname,lastname,mobile,email,address,gender,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification.','firstname {} lastname {} Added sucessfully and want to clean the form'.format(firstname,lastname),parent=addroot)
            if(res==True):
                firstnameval.set('')
                lastnameval.set('')
                mobileval.set('') 
                emailval.set('')
                addressval.set('') 
                genderval.set('')
                #dobval.set('')
                dateval.set('')


        except:
            messagebox.showerror('Notification','Id alredy exist try another id.',parent=addroot)

        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        #studenttable.de
        #print(datas)


    addroot = Toplevel(master=insertDataFrame)
    addroot.grab_set()  # showing of windows at a time.
    addroot.geometry('470x470+220+200')
    addroot.config(bg='black')
    addroot.iconbitmap('mng.ico')
    addroot.resizable(False, False)

    firstnamelabel = Label(addroot, text='Enter FN:', font=('times', 20, 'bold'))
    firstnamelabel.place(x=10, y=10)

    lastnamelabel = Label(addroot, text='Enter LN:', font=('times', 20, 'bold'))
    lastnamelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile:', font=('times', 20, 'bold'))
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email:', font=('times', 20, 'bold'))
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Add:', font=('times', 20, 'bold'))
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender:', font=('times', 20, 'bold'))
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B:', font=('times', 20, 'bold'))
    doblabel.place(x=10, y=370)

    firstnameval = StringVar()
    lastnameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    firstnameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=firstnameval)
    firstnameentry.place(x=250, y=10)

    lastnameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=lastnameval)
    lastnameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    submitButton = Button(addroot, text='Submit', font=('roman', 15, 'bold'), bd=5, width=20, command=submitadd)
    submitButton.place(x=150, y=420)

    addroot.mainloop()

    print('Student added sucssesfully.')





def deletestudent():
    print('Student deleted sucssesfully.')





def showstudent():
    print('Showing.')


def exportstudent():
    print('Export.')


def exitstudent():
    a = messagebox.askyesnocancel('Notification', 'Do You Want To Exit')
    if(a == True):
        root.destroy()
    # print('Exit.')


# connection to database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostVal.get()
        user = userVal.get()
        password = passwordVal.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification', 'Data is incorrect please try again.')
            return
        try:
            strr = 'create database studentmanagementsystem4'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem4'
            mycursor.execute(strr)
            strr = 'create table studentdata1(firstName varchar(12),lastName varchar(20),mobile varchar(10),email varchar(20),address varchar(20),gender varchar(2),date varchar(20),time varchar(20))'
            mycursor.execute(strr)

            strr = 'alter table studentdata1 modify column id numeric not null'
            mycursor.execute(strr)

            messagebox.showinfo('Notification', 'Database base created.Now you are connected.',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem4'
            mycursor.execute(strr)

            messagebox.showinfo('Notification', 'Now you are connected to database.',parent=dbroot)

        dbroot.destroy()


            #strr = 'alter table studentdata1 modify column id numeric primary key'
            #mycursor.execute(strr)



    

    dbroot = Toplevel()
    dbroot.grab_set() # showing of windows at a time.
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('mng.ico')
    dbroot.resizable(False, False)

    hostlabel = Label(dbroot, text='host name:', font=('times', 20, 'bold'))
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text='db name:', font=('times', 20, 'bold'))
    userlabel.place(x=10, y=80)

    passwordlabel = Label(dbroot, text='db password:', font=('times', 20, 'bold'))
    passwordlabel.place(x=10, y=150)

    hostVal = StringVar()
    userVal = StringVar()
    passwordVal = StringVar()

    hostEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostVal)
    hostEntry.place(x=200, y=10)

    userEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userVal)
    userEntry.place(x=200, y=80)

    hostEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordVal)
    hostEntry.place(x=200, y=150)

    submitButton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bd=5, width=20, command=submitdb)
    submitButton.place(x=150, y=190)

    dbroot.mainloop()


from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
#import mysql.connector



root = Tk()
root.title("Registration Form")
root.config(bg='white')
root.geometry('1174x700+100+100')
root.iconbitmap('mng.ico')
root.resizable(False, False)
# Creating frame.

insertDataFrame = Frame(root, bg='black', borderwidth='5')
insertDataFrame.place(x=10, y=80, width=500, height=600)

# Creating contents of insertDataFrame.
addbutton = Button(insertDataFrame, text='Register Now.', width=25, font=('chiller', 20, "bold"), bd=6, command=adddatas)
addbutton.pack(side=TOP, expand=True)

searchbutton = Button(insertDataFrame, text='Search Student', width=25, font=('chiller', 20, "bold"), bd=6, command=searchstudent)
searchbutton.pack(side=TOP, expand=True)

deletebutton = Button(insertDataFrame, text='Delete contact', width=25, font=('chiller', 20, "bold"), bd=6, command=deletestudent)
deletebutton.pack(side=TOP, expand=True)

updatebutton = Button(insertDataFrame, text='Update contact', width=25, font=('chiller', 20, "bold"), bd=6, command=updatestudent)
updatebutton.pack(side=TOP, expand=True)

showbutton = Button(insertDataFrame, text='Show All', width=25, font=('chiller', 20, "bold"), bd=6, command=showstudent)
showbutton.pack(side=TOP, expand=True)

exportbutton = Button(insertDataFrame, text='Export Data', width=25, font=('chiller', 20, "bold"), bd=6, command=exportstudent)
exportbutton.pack(side=TOP, expand=True)

exitbutton = Button(insertDataFrame, text='Exit', width=25, font=('chiller', 20, "bold"), bd=6, command=exitstudent)
exitbutton.pack(side=TOP, expand=True)

# Creating for showing data from data base.

showDataFrame = Frame(root, bg='black', borderwidth='5')
showDataFrame.place(x=540, y=80, width=620, height=600)

# show data frame.

scroll_x = Scrollbar(showDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(showDataFrame, orient=VERTICAL)
studenttable = Treeview(showDataFrame, column=('First Name', 'Last Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('First Name', text='First Name')
studenttable.heading('Last Name', text='Last Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
#studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.pack(fill=BOTH, expand=1)

# generating tittle for project.

a = "Registration Form"
sliderLabel = Label(root, text=a, font=('chiller', 29, 'italic bold'), relief=RIDGE, borderwidth=5, bg='cyan')
sliderLabel.place(x=300, y=0)

# Connect to database button.

connectButton = Button(root, text='connect', width=23, bg='white', command=Connectdb)
connectButton.place(x=930, y=0)

root.mainloop()
