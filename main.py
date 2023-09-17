from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import date
import backend as b

subDict = {
    "Bio-Maths": ["English", "Physics", "Chemistry", "Biology", "Maths"],
    "Bio-IP": ["English", "Physics", "Chemistry", "Biology", "IP"],
    "Bio-Eco": ["English", "Physics", "Chemistry", "Biology", "Economics"],
    "Maths-CS": ["English", "Physics", "Chemistry", "Maths", "CS"],
    "Commerce-IP": ["English", "Acct", "BS", "Eco", "IP"],
    "Commerce-Maths": ["English", "Acct", "BS", "Eco", "Maths"]
}

loginWindow = Tk()
loginWindow.title("Course Managment System")
size = "800x600"
loginWindow.geometry(size)
loginWindow.resizable(0, 0)

unm_var = StringVar()
pwd_var = StringVar()
ID_var = StringVar()
name_var = StringVar()
Stream_var = StringVar()
Email_var = StringVar()
passw_var = StringVar()
mrk1 = StringVar()
mrk2 = StringVar()
mrk3 = StringVar()
mrk4 = StringVar()
mrk5 = StringVar()
idSerVar = StringVar()


def cls(window):
    window.destroy()
    myProfBtn.focus_set()


def cls1(window):
    window.destroy()
    markEntryBtn.focus_set()


def myProf():
    myProfWin = Toplevel()
    myProfWin.title('My Profile')
    myProfWin.geometry("800x650")
    myProfWin.resizable(0, 0)
    teacher = []
    teacher = b.getTeacher(res[2], res[3])

    headLabel = Label(myProfWin,
                      text='User Information',
                      font=('calibre', 15, 'bold'))
    headLabel.place(x=20, y=50)

    IDLabel1 = Label(myProfWin, text='ID', font=('calibre', 10, 'bold'))
    IDLabel1.place(x=20, y=100)
    IDLabel2 = Label(myProfWin, text=res[0], font=('calibre', 10))
    IDLabel2.place(x=200, y=100)

    nameLabel1 = Label(myProfWin, text='Name', font=('calibre', 10, 'bold'))
    nameLabel1.place(x=20, y=130)
    nameLabel2 = Label(myProfWin, text=res[1], font=('calibre', 10))
    nameLabel2.place(x=200, y=130)

    classLabel1 = Label(myProfWin, text='Class', font=('calibre', 10, 'bold'))
    classLabel1.place(x=20, y=160)
    classLabel2 = Label(myProfWin, text=res[2], font=('calibre', 10))
    classLabel2.place(x=200, y=160)

    streamLabel1 = Label(myProfWin,
                         text='Stream',
                         font=('calibre', 10, 'bold'))
    streamLabel1.place(x=20, y=190)
    streamLabel2 = Label(myProfWin, text=res[3], font=('calibre', 10))
    streamLabel2.place(x=200, y=190)

    mailLabel1 = Label(myProfWin, text='Email', font=('calibre', 10, 'bold'))
    mailLabel1.place(x=20, y=220)
    mailLabel2 = Label(myProfWin, text=res[4], font=('calibre', 10))
    mailLabel2.place(x=200, y=220)

    pwdLabel1 = Label(myProfWin, text='Password', font=('calibre', 10, 'bold'))
    pwdLabel1.place(x=20, y=250)
    pwdLabel2 = Label(myProfWin, text=res[5], font=('calibre', 10))
    pwdLabel2.place(x=200, y=250)

    tnmLabel1 = Label(myProfWin,
                      text='Teacher In-Charge',
                      font=('calibre', 10, 'bold'))
    tnmLabel1.place(x=20, y=280)
    tnmLabel2 = Label(myProfWin, text=teacher[0], font=('calibre', 10))
    tnmLabel2.place(x=200, y=280)

    temLabel1 = Label(myProfWin,
                      text='Teacher Mail',
                      font=('calibre', 10, 'bold'))
    temLabel1.place(x=20, y=310)
    temLabel2 = Label(myProfWin, text=teacher[1], font=('calibre', 10))
    temLabel2.place(x=200, y=310)

    clsBtn = Button(myProfWin, text='Close', command=lambda: cls(myProfWin))
    clsBtn.place(x=140, y=340)


def myPerf():
    myPerfWin = Toplevel()
    myPerfWin.title('My Performance')
    myPerfWin.geometry("800x650")
    myPerfWin.resizable(0, 0)

    def callback(event):
        exm = selExamCombo.get()
        mList = b.searchMark(res[0], exm)
        if mList == 0:
            messagebox.showerror("Error", "No Mark is Entered")
        else:
            subList = subDict[res[3]]
            subList.extend(["Total", "Average"])

            exm1 = "Name of Examination: " + exm
            exmLabel = Label(myPerfWin,
                             text=exm1,
                             font=('calibre', 15, 'bold'),
                             width="100")
            exmLabel.place(x=30, y=100)

            treev = Treeview(myPerfWin, selectmode='browse')
            treev.place(x=30, y=150)
            treev["columns"] = ("1", "2")
            treev['show'] = 'headings'
            treev.column("1", width=90, anchor='c')
            treev.column("2", width=90, anchor='se')
            treev.heading("1", text="Subject")
            treev.heading("2", text="Mark")
            ml = mList[6:]
            for i in range(7):
                treev.insert("", 'end', text="L1", values=(subList[i], ml[i]))

    examList = [
        "--Select--", "First Mid", "Second Mid", "First Term", "Second Term"
    ]
    selExam = Label(myPerfWin, text="Select the Exam")
    selExam.place(x=30, y=50)
    selExamCombo = Combobox(myPerfWin)
    selExamCombo["values"] = examList
    selExamCombo.place(x=130, y=50)
    selExamCombo.current(0)
    selExamCombo.bind('<<ComboboxSelected>>', callback)

    clsBtn1 = Button(myPerfWin, text='Close', command=lambda: cls(myPerfWin))
    clsBtn1.place(x=80, y=400)


def logout2():
    studentWin.destroy()
    uname_entry.focus_set()


def studentMenu():
    global studentWin
    global myProfBtn

    studentWin = Toplevel()
    studentWin.title("Student Panel")
    studentWin.geometry("800x650")
    studentWin.resizable(0, 0)

    myProfBtn = Button(studentWin, text="My Profile", command=myProf)
    myProfBtn.place(x=10, y=10)

    myPerfBtn = Button(studentWin, text="My Performance", command=myPerf)
    myPerfBtn.place(x=10, y=40)

    btn_logout = Button(studentWin, text="Logout", command=logout2)
    btn_logout.place(x=650, y=10)


def submitMark():
    uid = ID_var.get()
    nm = name_var.get()
    cls = res[2]
    stream = res[3]
    exm = selExamCombo.get()
    m1 = mrk1.get()
    m2 = mrk2.get()
    m3 = mrk3.get()
    m4 = mrk4.get()
    m5 = mrk5.get()
    tot = int(m1) + int(m2) + int(m3) + int(m4) + int(m5)
    avg = tot / 5
    markList = [uid, nm, cls, stream, exm, m1, m2, m3, m4, m5, tot, avg]
    if mid == 0:
        b.addMark(markList)
    else:
        b.updateMark(mid, markList)
    messagebox.showinfo("Success", "Marks are Added Successfully")
    idEntry.config(state="enabled")
    nameEntry.config(state="enabled")
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    selExamCombo.current(0)
    sub1Entry.delete(0, END)
    sub2Entry.delete(0, END)
    sub3Entry.delete(0, END)
    sub4Entry.delete(0, END)
    sub5Entry.delete(0, END)
    idEntry.focus_set()


def markEntry():
    markWin = Toplevel()
    markWin.title('Mark Entry')
    markWin.geometry("800x650")
    markWin.resizable(0, 0)

    def rem_item(event):
        global idEntry
        global nameEntry
        global selExamCombo

        def callback1(event):
            global mid
            global sub1Entry
            global sub2Entry
            global sub3Entry
            global sub4Entry
            global sub5Entry

            exm1 = selExamCombo.get()
            mark1 = b.searchMark(selected_item[0], exm1)
            if mark1 == 0:
                mrk1.set("0")
                mrk2.set("0")
                mrk3.set("0")
                mrk4.set("0")
                mrk5.set("0")
                mid = 0
            else:
                mrk1.set(mark1[6])
                mrk2.set(mark1[7])
                mrk3.set(mark1[8])
                mrk4.set(mark1[9])
                mrk5.set(mark1[10])
                mid = mark1[0]

            subList = subDict[res[3]]

            sub1Label = Label(markWin, text=subList[0])
            sub1Label.place(x=250, y=140)
            sub1Entry = Entry(markWin, textvariable=mrk1)
            sub1Entry.place(x=350, y=140)

            sub2Label = Label(markWin, text=subList[1])
            sub2Label.place(x=250, y=170)
            sub2Entry = Entry(markWin, textvariable=mrk2)
            sub2Entry.place(x=350, y=170)

            sub3Label = Label(markWin, text=subList[2])
            sub3Label.place(x=250, y=200)
            sub3Entry = Entry(markWin, textvariable=mrk3)
            sub3Entry.place(x=350, y=200)

            sub4Label = Label(markWin, text=subList[3])
            sub4Label.place(x=250, y=230)
            sub4Entry = Entry(markWin, textvariable=mrk4)
            sub4Entry.place(x=350, y=230)

            sub5Label = Label(markWin, text=subList[4])
            sub5Label.place(x=250, y=260)
            sub5Entry = Entry(markWin, textvariable=mrk5)
            sub5Entry.place(x=350, y=260)

            markBtn = Button(markWin, text="Submit", command=submitMark)
            markBtn.place(x=300, y=290)

        index = list_box1.curselection()
        if index:
            selected_item = list_box1.get(index)

            ID_var.set(selected_item[0])
            name_var.set(selected_item[1])

            idLabel = Label(markWin, text='ID')
            idLabel.place(x=250, y=50)
            idEntry = Entry(markWin, textvariable=ID_var, state='disabled')
            idEntry.place(x=350, y=50)

            nameLabel = Label(markWin, text='Name')
            nameLabel.place(x=250, y=80)
            nameEntry = Entry(markWin, textvariable=name_var, state='disabled')
            nameEntry.place(x=350, y=80)

            examList = [
                "--Select--", "First Mid", "Second Mid", "First Term",
                "Second Term"
            ]
            selExam = Label(markWin, text="Select the Exam")
            selExam.place(x=250, y=110)
            selExamCombo = Combobox(markWin)
            selExamCombo["values"] = examList
            selExamCombo.place(x=350, y=110)
            selExamCombo.current(0)
            selExamCombo.bind('<<ComboboxSelected>>', callback1)

    cls = res[2]
    stream = res[3]
    stuList = b.searchStud(cls, stream)

    lbl1 = Label(markWin,
                 text='List of Student',
                 font=('calibre', 15, 'bold'),
                 width="20")
    lbl1.place(x=20, y=10)

    list_box1 = Listbox(markWin)
    list_box1.place(x=20, y=50)
    list_box1.bind("<<ListboxSelect>>", rem_item)
    j = 0
    for i in stuList:
        list_box1.insert(j, i)
        j = j + 1

    clsBtn2 = Button(markWin, text='Close', command=lambda: cls1(markWin))
    clsBtn2.place(x=50, y=250)


def logout1():
    teacherWin.destroy()
    uname_entry.focus_set()


def teacherMenu():
    global teacherWin
    global markEntryBtn

    teacherWin = Toplevel()
    teacherWin.title("Teacher Control Panel")
    teacherWin.geometry("800x650")
    teacherWin.resizable(0, 0)

    markEntryBtn = Button(teacherWin, text="Mark Entry", command=markEntry)
    markEntryBtn.place(x=10, y=10)

    btn_logout = Button(teacherWin, text="Logout", command=logout1)
    btn_logout.place(x=650, y=10)


def deleteUser():
    UID = ID_var.get()
    b.deleteUser(UID)
    messagebox.showinfo("Success", "Record is Deleted Successfully")
    idEntry.config(state='enabled')
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    classCombo.current(0)
    streamCombo.current(0)
    emailEntry.delete(0, END)
    roleCombo.current(0)
    pwdEntry.delete(0, END)
    serEntry.focus_set()


def updateUser():
    UID = ID_var.get()
    Name = name_var.get()
    Class = classCombo.get()
    Stream = streamCombo.get()
    Email = Email_var.get()
    Password = passw_var.get()
    Role = roleCombo.get()
    userList = [UID, Name, Class, Stream, Email, Password, Role]
    b.updateUser(userList)
    messagebox.showinfo("Success", "Record is Updated Successfully")
    idEntry.config(state='enabled')
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    classCombo.current(0)
    streamCombo.current(0)
    emailEntry.delete(0, END)
    roleCombo.current(0)
    pwdEntry.delete(0, END)
    serEntry.focus_set()


def searchUser1():
    global idEntry
    global nameEntry
    global classCombo
    global streamCombo
    global emailEntry
    global pwdEntry
    global roleCombo

    userId = idSerVar.get()
    userInfo = b.searchUser(userId)
    if userInfo == 0:
        messagebox.showerror("Error", "No Such User")
    else:
        ID_var.set(userInfo[0])
        name_var.set(userInfo[1])
        Email_var.set(userInfo[4])
        passw_var.set(userInfo[5])

        idLabel = Label(serUserWin,
                        text='User ID',
                        font=('calibre', 10, 'bold'))
        idLabel.place(x=30, y=100)
        idEntry = Entry(serUserWin, textvariable=ID_var, state='disabled')
        idEntry.place(x=150, y=100)

        nameLabel = Label(serUserWin,
                          text='Name',
                          font=('calibre', 10, 'bold'))
        nameLabel.place(x=30, y=130)
        nameEntry = Entry(serUserWin, textvariable=name_var)
        nameEntry.place(x=150, y=130)

        classItems = ("11", "12")
        for i in range(len(classItems)):
            if classItems[i] == userInfo[2]:
                loc = i
        classLabel = Label(serUserWin,
                           text='Class',
                           font=('calibre', 10, 'bold'))
        classLabel.place(x=30, y=160)
        classCombo = Combobox(serUserWin)
        classCombo["values"] = classItems
        classCombo.place(x=150, y=160)
        classCombo.current(loc)

        streamItems = ("Bio-Maths", "Bio-IP", "Bio-Eco", "Maths-CS",
                       "Commerce-IP", "Commerce-Maths")
        for i in range(len(streamItems)):
            if streamItems[i] == userInfo[3]:
                loc = i
        streamLabel = Label(serUserWin,
                            text='Stream',
                            font=('calibre', 10, 'bold'))
        streamLabel.place(x=30, y=190)
        streamCombo = Combobox(serUserWin)
        streamCombo["values"] = streamItems
        streamCombo.place(x=150, y=190)
        streamCombo.current(loc)

        emailLabel = Label(serUserWin,
                           text='Email',
                           font=('calibre', 10, 'bold'))
        emailLabel.place(x=30, y=220)
        emailEntry = Entry(serUserWin, textvariable=Email_var)
        emailEntry.place(x=150, y=220)

        pwdLabel = Label(serUserWin,
                         text='Password',
                         font=('calibre', 10, 'bold'))
        pwdLabel.place(x=30, y=250)
        pwdEntry = Entry(serUserWin, textvariable=passw_var, show='*')
        pwdEntry.place(x=150, y=250)

        roleItems = ("Teacher", "Student")
        for i in range(len(roleItems)):
            if roleItems[i] == userInfo[6]:
                loc = i
        roleLabel = Label(serUserWin,
                          text='Role',
                          font=('calibre', 10, 'bold'))
        roleLabel.place(x=30, y=280)
        roleCombo = Combobox(serUserWin)
        roleCombo["values"] = roleItems
        roleCombo.place(x=150, y=280)
        roleCombo.current(loc)

        updateBtn = Button(serUserWin, text='Update', command=updateUser)
        updateBtn.place(x=40, y=310)
        deleteBtn = Button(serUserWin, text='Delete', command=deleteUser)
        deleteBtn.place(x=120, y=310)
        closeBtn = Button(serUserWin, text='Close', command=serUserWin.destroy)
        closeBtn.place(x=200, y=310)


def searchUser():
    global serUserWin
    global serEntry

    serUserWin = Toplevel()
    serUserWin.title("Search User")
    serUserWin.geometry(size)
    serUserWin.resizable(0, 0)

    serLabel = Label(serUserWin, text="User ID for Searching")
    serLabel.place(x=20, y=50)
    serEntry = Entry(serUserWin, textvariable=idSerVar)
    serEntry.place(x=150, y=50)
    serEntry.focus_set()
    serBtn1 = Button(serUserWin, text="Search", command=searchUser1)
    serBtn1.place(x=290, y=50)


def addUser1():
    UID = ID_var.get()
    Name = name_var.get()
    Class = class_combo.get()
    Stream = stream_combo.get()
    Email = Email_var.get()
    Password = passw_var.get()
    Role = role_combo.get()
    userList = [UID, Name, Class, Stream, Email, Password, Role]
    res = b.add_user(userList)
    if res == 0:
        messagebox.showerror("Error", "ID is Already Exist")
    else:
        messagebox.showinfo("Success", "Record is Added Successfully")
    ID_entry.delete(0, END)
    name_entry.delete(0, END)
    class_combo.current(0)
    stream_combo.current(0)
    email_entry.delete(0, END)
    role_combo.current(0)
    passw_entry.delete(0, END)
    ID_entry.focus_set()


def addUser():
    global ID_entry
    global name_entry
    global class_combo
    global stream_combo
    global email_entry
    global role_combo
    global passw_entry

    addUserWin = Toplevel()
    addUserWin.title("User Creation")
    addUserWin.geometry(size)
    addUserWin.resizable(0, 0)

    ID_label = Label(addUserWin,
                     text='User ID',
                     font=('calibre', 10, 'bold'),
                     width="20").pack()

    ID_entry = Entry(addUserWin,
                     textvariable=ID_var,
                     font=('calibre', 10, 'normal'))
    ID_entry.pack()

    name_label = Label(addUserWin,
                       text='Name',
                       font=('calibre', 10, 'bold'),
                       width="20").pack()

    name_entry = Entry(addUserWin,
                       textvariable=name_var,
                       font=('calibre', 10, 'normal'))
    name_entry.pack()

    Class_label = Label(addUserWin,
                        text='Class',
                        font=('calibre', 10, 'bold'),
                        width="20").pack()

    class_combo = Combobox(addUserWin)
    class_items = (
        "11",
        "12",
    )
    class_combo["values"] = class_items
    class_combo.pack()
    class_combo.current(0)

    Stream_label = Label(addUserWin,
                         text='Stream',
                         font=('calibre', 10, 'bold'),
                         width="20").pack()

    stream_combo = Combobox(addUserWin)
    stream_items = (
        "Bio-Maths",
        "Bio-IP",
        "Bio-Eco",
        "Maths-CS",
        "Commerce-IP",
        "Commerce-Maths",
    )
    stream_combo["values"] = stream_items
    stream_combo.pack()
    stream_combo.current(0)

    email_label = Label(addUserWin,
                        text='Email',
                        font=('calibre', 10, 'bold'),
                        width="20").pack()

    email_entry = Entry(addUserWin,
                        textvariable=Email_var,
                        font=('calibre', 10, 'normal'))
    email_entry.pack()

    passw_label = Label(addUserWin,
                        text='Password',
                        font=('calibre', 10, 'bold'),
                        width="20").pack()

    passw_entry = Entry(addUserWin,
                        textvariable=passw_var,
                        font=('calibre', 10, 'normal'),
                        show='*')
    passw_entry.pack()

    Role_label = Label(addUserWin,
                       text='Role',
                       font=('calibre', 10, 'bold'),
                       width="20").pack()

    role_combo = Combobox(addUserWin)
    items = (
        "Teacher",
        "Student",
    )
    role_combo["values"] = items
    role_combo.pack()
    role_combo.current(0)

    ub_btn = Button(addUserWin, text='Submit', command=addUser1,
                    width="20").pack()

    bk_btn = Button(addUserWin,
                    text="Back",
                    command=addUserWin.destroy,
                    width="20").pack()


def logout():
    ser_win.destroy()
    uname_entry.focus_set()


def adminMenu():
    global ser_win
    global ser_t1

    ser_win = Toplevel()
    ser_win.title("Admin Command Panel")
    ser_win.geometry("800x650")
    ser_win.resizable(0, 0)

    btn_add = Button(ser_win, text="Add User", command=addUser)
    btn_add.place(x=20, y=50)

    ser_b1 = Button(ser_win, text="Search User", command=searchUser)
    ser_b1.place(x=20, y=80)

    btn_logout = Button(ser_win, text="Logout", command=logout)
    btn_logout.place(x=650, y=10)


def login1():
    global res
    u = unm_var.get()
    p = pwd_var.get()
    if u == "admin" and p == "admin":
        uname_entry.delete(0, END)
        pwd_entry.delete(0, END)
        adminMenu()
    else:
        uname_entry.delete(0, END)
        pwd_entry.delete(0, END)
        res = b.checkUser(u, p)
        if res == 0:
            messagebox.showerror("Error", "Invalid Username or Password")
            uname_entry.focus_set()
        else:
            if res[6] == "Teacher":
                teacherMenu()
            else:
                studentMenu()


head_label1 = Label(loginWindow,
                    text="Course Management System",
                    font=("Arial", 25))
head_label1.place(x=200, y=10)

uname_label = Label(loginWindow, text="Username", font=("Arial", 10))
uname_label.place(x=300, y=200)
uname_entry = Entry(loginWindow, textvariable=unm_var)
uname_entry.place(x=380, y=200)
uname_entry.focus_set()
pwd_label = Label(loginWindow, text="Password", font=("Arial", 10))
pwd_label.place(x=300, y=240)
pwd_entry = Entry(loginWindow, textvariable=pwd_var, show="*")
pwd_entry.place(x=380, y=240)
login_button = Button(loginWindow, text="Login", command=login1)
login_button.place(x=360, y=280)

loginWindow.mainloop()

