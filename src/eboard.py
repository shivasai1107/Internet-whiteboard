from Tkinter import *
import urllib2
import tkMessageBox
from Databaser import *
import MySQLdb
import time
import threading
import random
import string
import pycurl
from StringIO import StringIO
import json


class myThread(threading.Thread):
    def __init__(self, threadID, name, dowhat):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.usrobj = userobject
        self.dowhat = dowhat

    def run(self):
        global lock_flag, reg_flag
        while (1):
            try:

                if (self.dowhat == "REGISTER"):
                    reg_thread(self.name)
                    reg_flag = "FALSE"

                elif (self.dowhat == "RETRIEVE"):
                    Ret(self.name)
                    LOCKSTATUS = userobject.checkLock(logus)
                    if (LOCKSTATUS == "TRUE"):
                        lock_flag = "TRUE"
                    else:
                        lock_flag = "FALSE"

                else:
                    pass


            except:

                pass
            time.sleep(0.01)

    def stop(self):
        self._is_running = False


def reg_thread(threadName):
    global threadflag, reg_flag, regus, regpass, regmail, thread_ID, thread2
    if (reg_flag == "TRUE"):

        if (threadflag == "STOP"):
            thread2.stop()

        try:
            userobject.sendMail(regmail, regus, regpass)
            threadflag = "STOP"
            try:
                thread2.stop()
                thread_ID = thread_ID + 1
                thread2 = myThread(thread_ID, "TH", "REGISTER")
            except:
                pass
        except:
            pass


def Ret(threadName):
    global threadflag
    global UL, i, len_old, AL

    if (threadflag == "STOP"):
        thread1.stop()

    dataobject.UPDATE()
    try:
        db = MySQLdb.connect(passwd=dataobject.DB_Password, db=dataobject.DB_DBName, host=dataobject.DB_IP,
                             port=dataobject.DB_PORT, user=dataobject.DB_UserName)
        cursor = db.cursor()
    except:
        tkMessageBox.showinfo("Error", "Error9: Couldn't establish connection to server")
    sql = "SELECT MODIFICATION FROM %s" % dataobject.DB_SESSION_Table
    cursor.execute(sql)
    result = cursor.fetchall()
    result = list(result)
    len_new = len(result)
    j = 0
    for h in range(0, len_new):
        if (h >= len_old):
            ex = result[h][0]
            ey = ex[-10:]
            ey = ey.strip()
            exec ex
            AL.append('')
            try:
                j = int(ey)
                i = j

            except:
                pass

    len_old = len_new
    db.close()


class Toolmgmt():
    def __init__(self):
        global canvas
        global canvas_name
        self.can = canvas
        self.can_name = canvas_name

    def updateCanvas(self):
        self.can = canvas
        self.can_name = canvas_name

    def Nothing(self, master):
        pass

    def Unbind(self):
        self.can.bind('<Button-1>', self.Nothing)
        self.can.bind('<B1-Motion>', self.Nothing)
        self.can.bind('<ButtonRelease-1>', self.Nothing)

        self.can.bind("<Leave>", CheckMod)
        self.can.bind("<Enter>", CheckMod)

    def getClick(self, event):
        global x1, y1, lock_flag
        if (lock_flag == "FALSE"):
            x1, y1 = event.x, event.y

    def pencilDraw(self, event):
        global x1, y1, L1, thck, i, lock_flag
        if (lock_flag == "FALSE"):
            string = 'AL[%d]=%s.create_line((%d, %d, %d, %d),fill="%s",width=%d);#          %s' % (
            i + 1, self.can_name, x1, y1, event.x, event.y, clr, thck, i + 1)
            x1, y1 = event.x, event.y
            self.inserter(string)

    def Clear(self):
        global thck, thckera, clr, clrfill, lock_flag, i
        if (lock_flag == "FALSE"):
            string = 'AL[%d]= %s.delete(ALL);#          %s' % (i + 1, self.can_name, i + 1)
            self.inserter(string)
            thck = 1
            thckera = 10
            clr = "black"
            clrfill = "white"

    def Pencil(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            canvas.bind('<Button-1>', self.getClick)
            canvas.bind('<B1-Motion>', self.pencilDraw)

    def Eraser(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            canvas.bind('<Button-1>', self.getClick)
            canvas.bind("<B1-Motion>", self.eraseStuff)

    def eraseStuff(self, event):

        global x2, y2, L1, i, lock_flag

        if (lock_flag == "FALSE"):
            x1, y1 = event.x, event.y
            string = 'AL[%d]=%s.create_rectangle(%d, %d, %d, %d,outline="white",fill="white");#          %d' % (
            i + 1, self.can_name, event.x - thckera, event.y - thckera, event.x + thckera, event.y + thckera, i + 1)
            self.inserter(string)

    def font1(self):
        global fnt
        fnt = "Helvetica"

    def font2(self):
        global fnt
        fnt = "SimSun"

    def font3(self):
        global fnt
        fnt = "Times"

    def font4(self):
        global fnt
        fnt = "Stencil"

    def font5(self):
        global fnt
        fnt = "Magneto"

    def font6(self):
        global fnt
        fnt = "French Script MT"

    def size1(self):
        global rndfont
        rndfont = 16

    def size2(self):
        global rndfont
        rndfont = 20

    def size3(self):
        global rndfont
        rndfont = 24

    def size4(self):
        global rndfont
        rndfont = 28

    def size5(self):
        global rndfont
        rndfont = 32

    def size6(self):
        global rndfont
        rndfont = 36

    def bold(self):
        global bold
        bold = 'bold'

    def normal(self):
        global bold
        bold = 'normal'

    def italic(self):
        global slant
        slant = 'italic'

    def roman(self):
        global slant
        slant = 'roman'

    def redclr(self):
        global clr
        clr = "red"

    def greenclr(self):
        global clr
        clr = "green"

    def blueclr(self):
        global clr
        clr = "blue"

    def blackclr(self):
        global clr
        clr = "black"

    def redclrf(self):
        global clrfill
        clrfill = "red"

    def greenclrf(self):
        global clrfill
        clrfill = "green"

    def blueclrf(self):
        global clrfill
        clrfill = "blue"

    def blackclrf(self):
        global clrfill
        clrfill = "black"

    def thck1(self):
        global thck, thckera
        thck = 1
        thckera = 10

    def thck3(self):
        global thck, thckera
        thck = 3
        thckera = 15

    def thck5(self):
        global thck, thckera
        thck = 5
        thckera = 20

    def Line(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            self.can.bind("<Button-1>", self.getClick)
            self.can.bind("<ButtonRelease-1>", self.drawLine)

    def drawLine(self, event):
        global x1, y1, i

        string = 'AL[%d]=%s.create_line((%d, %d, %d, %d),fill="%s",width=%d); #          %s' % (
            i + 1, self.can_name, x1, y1, event.x, event.y, clr, thck, i + 1)
        self.inserter(string)

    def Oval(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            canvas.bind('<Button-1>', self.ovalStart)
            canvas.bind('<ButtonRelease-1>', self.ovalEnd)

    def ovalStart(self, event):
        global xc1, yc1, thck
        xc1, yc1 = event.x, event.y

    def ovalEnd(self, event):

        global xc1, yc1, clr, clrfill, thck, i

        string = 'AL[%d]=%s.create_oval((%d, %d, %d, %d),outline= "%s",fill="%s",width=%d); #          %s' % (
        i + 1, self.can_name, xc1, yc1, event.x, event.y, clr, clrfill, thck, i + 1)
        self.inserter(string)

    def rect(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            canvas.bind('<Button-1>', self.rectStart)
            canvas.bind('<ButtonRelease-1>', self.rectEnd)

    def rectStart(self, event):
        global xq1, yq1, thck
        xq1, yq1 = event.x, event.y

    def rectEnd(self, event):
        global xq1, yq1, xq2, yq2, clr, clrfill, i
        xq2, yq2 = event.x, event.y

        string = 'AL[%d]=%s.create_rectangle((%d, %d, %d, %d),outline= "%s",fill="%s",width=%d); #          %s' % (
        i + 1, self.can_name,
        xq1, yq1, xq2, yq2, clr, clrfill, thck, i + 1)
        self.inserter(string)

    def newClick(self, event):
        global x1
        global y1, i

        string = 'AL[%d]=%s.create_line((%d, %d, %d, %d),fill="%s",width=%d);#          %s' % (
            i + 1, self.can_name, x1, y1, event.x, event.y, clr, thck, i + 1)
        self.inserter(string)
        x1 = event.x
        y1 = event.y

    def polylineend(self, event):
        self.Unbind()

    def drawpolyline(self, event):
        global x1, y1, i

        x2, y2 = event.x, event.y
        string = 'AL[%d]=%s.create_line((%d, %d, %d, %d),fill="%s",width=%d);#          %s' % (
            i + 1, self.can_name, x1, y1, event.x, event.y, clr, thck, i + 1)

        self.inserter(string)
        self.Unbind()
        x1 = event.x
        y1 = event.y
        self.can.bind("<Button-1>", self.newClick)
        self.can.bind("<Button-3>", self.polylineend)

    def Polyline(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            self.can.bind("<Button-1>", self.getClick)
            self.can.bind("<ButtonRelease-1>", self.drawpolyline)
            self.can.bind("<Button-3>", self.polylineend)

    def Arrow(self):
        global lock_flag
        self.Unbind()
        if (lock_flag == "FALSE"):
            canvas.bind('<Button-1>', self.getClick)
            canvas.bind('<ButtonRelease-1>', self.arrowdraw)

    def arrowdraw(self, event):
        global x1, y1, clr, thck, i

        string = 'AL[%d]=%s.create_line((%d, %d, %d, %d), arrow = "last", fill="%s",width=%d);#          %s' % (
            i + 1, self.can_name, x1, y1, event.x, event.y, clr, thck, i + 1)
        self.inserter(string)

    def Text_input(self):
        global lock_flag
        global enter
        self.Unbind()
        if (lock_flag == "FALSE"):
            frame_text.pack(side=TOP)
            enter.grid(row=0,column=1,sticky=(N,E,W,S))
            button10.grid(row=2,column=0,sticky=(N,E,W,S))
            button11.grid(row=2,column=1,sticky=(N,E,W,S))
            button12.grid(row=2,column=2,sticky=(N,E,W,S))
            button13.grid(row=2,column=3,sticky=(N,E,W,S))
            self.can.bind("<Button-1>", self.Text)
            self.can.bind("<Button-3>", self.textend)

    def textend(self, event):
        global enter
        enter.delete(0, END)
        enter.grid_remove()

        button10.grid_remove()
        button11.grid_remove()
        button12.grid_remove()
        button13.grid_remove()

    def Text(self, event):
        global x_1, y_1, clr, i
        global enter
        x_1, y_1 = event.x, event.y
        s = enter.get()
        string = 'AL[%d]=%s.create_text(%d, %d,text="%s",font=("%s",%d,"%s","%s"));#          %s' % (
        i + 1, self.can_name, x_1, y_1, s, fnt, rndfont, bold, slant, i + 1)
        self.inserter(string)

    def Undo(self):
        global lock_flag, i
        if (lock_flag == "FALSE"):
            ender = 0
            starter = 0
            string = "canvas1.delete(AL[%d])" % (i)
            exec string

            self.inserter(string)
            if (i > 1):
                i -= 1

    def get_modifications(self):
        global commands, len_commands, x
        try:
            db = MySQLdb.connect(passwd=dataobject.DB_Password, db=dataobject.DB_DBName, host=dataobject.DB_IP,
                                 port=dataobject.DB_PORT, user=dataobject.DB_UserName)
        except:
            tkMessageBox.showinfo("Error", "Error: Couldn't establish connection to server")
        cursor = db.cursor()
        sql = "SELECT MODIFICATION,USER,TIME_STAMP FROM %s" % (dataobject.DB_SESSION_Table)
        cursor.execute(sql)
        commands = cursor.fetchall()
        commands = list(commands)
        len_commands = len(commands)
        x = 0

    def reload_event(self):
        global p
        self.Unbind()
        self.can.delete(ALL)
        self.get_modifications()
        self.can.bind("<Button-1>", self.reload_click)
        p = 0

    def reload_click(self, event):
        global commands, len_commands, x, p
        if (p > 0):
            self.can.delete("h")
            self.can.delete("o")
        while (x < len_commands):
            ex = commands[x][0]
            us = commands[x][1]
            ts = commands[x][2]
            a = self.can.create_text(55, 15, text=us, tag="h")
            b = self.can.create_text(55, 35, text=ts, tag="o")
            p = 1
            exec ex
            x = x + 1
            break;

    def reload_automatic(self):
        global commands, len_commands
        self.can.delete(ALL)
        self.get_modifications()
        for x in range(0, len_commands):
            ex = commands[x][0]
            exec ex
            root.update()
            time.sleep(1)

    def Timestamp(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp

    def inserter(self, string):
        global logus, timestamp, canvas_name
        try:
            db = MySQLdb.connect(passwd=dataobject.DB_Password, db=dataobject.DB_DBName, host=dataobject.DB_IP,
                                 port=dataobject.DB_PORT, user=dataobject.DB_UserName)
            cursor = db.cursor()
        except:
            tkMessageBox.showinfo("Error", "Error: Couldn't establish connection to server")
        try:
            sql = "SELECT MODIFICATION FROM %s" % dataobject.DB_SESSION_Table
            cursor.execute(sql)
            serial = cursor.fetchall()
            serial = list(serial)
            serial = len(serial)
            try:
                timestamp = self.Timestamp()
                sql = "INSERT INTO %s(SNO,SHEET_NO,MODIFICATION,USER,TIME_STAMP) VALUES ('%d','%s','%s','%s','%s')" % (
                    dataobject.DB_SESSION_Table, serial + 1, canvas_name[-1:], string, logus, timestamp)
                cursor.execute(sql)
                db.commit()
                db.close()
            except:
                tkMessageBox.showinfo("Error", "Error: Connection interupted")
        except:
            tkMessageBox.showinfo("Error", "Error: Connection interupted")


class Sheetmgmt():
    def __init__(self, canvas):
        self.can = canvas

    def Show(self):
        self.can.grid(row=0, column=0, columnspan=9, sticky=(N, E, S, W))

    def Hide(self):
        self.can.grid_remove()


class Usermgmt():
    def login(self):
        global V
        V = 4
        frame1.grid_remove()
        frame3.grid_remove()
        frame2.grid(columnspan=10, padx=450, pady=50, row=0, column=0, sticky=(N, E, S, W))
        Labellogin = Label(frame2, text="    LOGIN", font=('Broadway', 30), bg='light blue')
        Labellogin.grid(pady=50, row=0, column=1, sticky=(N, E, W, S))
        Labellogin = Label(frame2, text="PAGE", font=('Broadway', 30), bg='light blue')
        Labellogin.grid(row=0, column=2, sticky=(N, E, W, S))
        Labeluser_log = Label(frame2, text="User Name", font=(5), bg='light blue')
        Labeluser_log.grid(row=1, column=1, sticky=(N, E, S, W))
        user_log.grid(row=1, column=2, sticky=(N, E, S, W))
        Labelpass_log = Label(frame2, text="Password", font=(5), bg='light blue')
        Labelpass_log.grid(row=2, column=1, sticky=(N, E, S, W))
        pass_log.grid(row=2, column=2, sticky=(N, E, S, W))
        OK_log.grid(pady=10, row=3, column=1, sticky=(E))
        Back_log.grid(row=3, column=2, sticky=(W))
        V = 4

    def register(self):
        global status, V
        frame1.grid_remove()
        frame2.grid_remove()
        frame4.grid_remove()
        frame5.grid_remove()
        frame3.grid(padx=400, pady=200, row=0, column=0, sticky=(N, E, S, W))
        Labelregister = Label(frame3, text="REGISTER", font=('Broadway', 30), bg='light blue')
        Labelregister.grid(pady=20, row=0, column=1, sticky=(N, E, W, S))
        Labelpage = Label(frame3, text=" PAGE ", font=('Broadway', 30), bg='light blue')
        Labelpage.grid(row=0, column=2, sticky=(N, E, W, S))
        Labeluser_reg = Label(frame3, text="User Name", font=(20), bg='light blue')
        Labeluser_reg.grid(row=1, column=1, sticky=(N, E, S, W))
        user_reg.grid(row=1, column=2, sticky=(N, E, S, W))
        Labelemail_reg = Label(frame3, text=" Email ID", font=(20), bg='light blue')
        Labelemail_reg.grid(row=2, column=1, sticky=(N, E, S, W))
        email_reg.grid(row=2, column=2, sticky=(N, E, S, W))
        OK_reg.grid(pady=10, row=3, column=1, sticky=(E))
        Back_reg.grid(row=3, column=2, sticky=(W))

    def Bac(self):
        global V
        user_log.delete(0, END)
        pass_log.delete(0, END)
        user_reg.delete(0, END)
        email_reg.delete(0, END)
        frame2.grid_remove()
        frame3.grid_remove()
        frame1.grid_remove()

        if (V == 1):
            frame4.grid(row=0, column=0)
            frame5.grid_remove()
        if (V == 0):
            frame5.grid(row=0, column=0)
            frame4.grid_remove()

        if (V == 3):
            on_closing()

        if (V == 4):
            frame2.grid_remove()
            frame1.grid(row=0, column=0)

    def Ok_log(self):
        global logus, thread1, threadflag, checker
        logus = user_log.get()
        logpass = pass_log.get()
        
        if all([logus == "Admin", logpass == "Admin"]):
            frame1.grid_remove()
            frame2.grid_remove()
            frame3.grid_remove()
            frame5.grid_remove()
            frame4.grid(row=0, column=0)


        else:

            try:
                dataobject.UPDATE()
                try:
                    db = MySQLdb.connect(passwd=dataobject.DB_Password, db=dataobject.DB_DBName, host=dataobject.DB_IP,
                                         port=dataobject.DB_PORT, user=dataobject.DB_UserName)
                except:
                    tkMessageBox.showinfo("Error", "Error: Couldn't establish connection to server")
                dataobject.PUSH_LOGGEDIN(logus)
            except:
                tkMessageBox.showinfo("Error", "Error: Couldn't Push Login status")

            str1 = '%s/lens.php?tn=%s&un=%s&pc=%s' % (dataobject.DB_IP, dataobject.DB_Table, logus, logpass)
            html = "default"
            try:
                html = toSSLornottoSSL(str1, checker)
                
            except:
                tkMessageBox.showinfo("Error", "Error: lost connection to server")

            if (html == 200):
                tkMessageBox.showinfo("Login", "Login success")
                type_user = dataobject.POP_USER_TYPE(logus)

                if (type_user == 'Employee'):
                    frame1.grid_remove()
                    frame2.grid_remove()
                    frame3.grid_remove()
                    frame4.grid_remove()
                    frame5.grid(row=0, column=0)

                elif (type_user == "Customer"):
                    frame1.grid_remove()
                    frame2.grid_remove()
                    frame3.grid_remove()
                    frame5.grid_remove()
                    frame4.grid_remove()
                    mainframe.grid(row=0, column=0, sticky=(N, E, S, W))
                    root.config(menu=menu1)

                    threadflag = "RUN"
                    thread1.start()
            else:
                tkMessageBox.showinfo("Error", "Error: LOGIN FAILURE!")
            db.close()

    def Ok_reg(self):
        global reg_flag, regus, regpass, regmail, checker, thread_ID, thread2
        reg_flag = "TRUE"
        reg_status = 0
        dataobject.UPDATE()
        try:
            db = MySQLdb.connect(passwd=dataobject.DB_Password, db=dataobject.DB_DBName, host=dataobject.DB_IP,
                                 port=dataobject.DB_PORT, user=dataobject.DB_UserName)
        except:
            tkMessageBox.showinfo("Error", "Error: Couldn't establish connection to server")
        regus = user_reg.get()
        regpass = "%s%d%s" % (regus[0:2], int(random.random() * 100), random.choice(string.ascii_lowercase))
        regmail = email_reg.get()
        try:
            threadflag = "RUN"
            thread2.start()
        except:
            pass
        str2 = '%s/pin.php?tn=%s&un=%s&pc=%s&ut=%s' % (dataobject.DB_IP, dataobject.DB_Table, regus, regpass, status)

        try:
            html = toSSLornottoSSL(str2, "NO")
            tkMessageBox.showinfo("status", "Resgistration Success")
        except:
            tkMessageBox.showinfo("status", "Resgistration failed")
        try:
            db.close()
        except:
            pass

    def logout(self):
        global logus, threadflag, V
        mainframe.grid_remove()
        frame2.grid_remove()
        frame3.grid_remove()
        frame4.grid_remove()
        frame5.grid_remove()
        frame1.grid(row=0, column=0)
        if (logus != "Admin"):
            dataobject.PUSH_UNMODERATOR(logus)
            dataobject.PUSH_LOGGEDOUT(logus)
        root.config(menu="")
        V = 3
        threadflag = "STOP"

    def locker(self):
        global logus
        x = dataobject.POP_USER()
        for users in range(0, len(x)):
            if (x[users] != logus):
                dataobject.PUSH_LOCK(x[users])

    def unlocker(self):
        global logus
        x = dataobject.POP_USER()
        for users in range(0, len(x)):
            if (x[users] != logus):
                dataobject.PUSH_UNLOCK(x[users])

    def checkLock(self, user):
        x = dataobject.POP_LOCK()
        for mod_num in range(0, len(x)):
            if (x[mod_num] == user):
                toolobj.Unbind()
                return "TRUE"
        return "FALSE"

    def CheckModerator(self, user):
        try:
            x = dataobject.POP_MODERATOR()
        except:
            pass
        for mod_num in range(0, len(x)):
            if (x[mod_num] == user):
                button15.pack(side=RIGHT)
                button15b.pack(side=LEFT)
                return "TRUE"
        button15.pack_forget()
        button15b.pack_forget()

        return "FALSE"

    def modselection(self):
        global X, frame_mod, mainframe, dataobject, v, y
        try:
            root.configure(background='white')
            str1 = 'http://193.11.187.1/session.php'
            response = urllib2.urlopen(str1)
            html = response.read()
            jsondata = json.loads(html)
            html = jsondata["data"]
            X = ""
            radio = []
            v = IntVar()
            r = html
            length = len(r)
            frame_mod.grid(row=0, column=1)
            for hi in range(0, length):
                radio.append('')
                radio[hi] = Radiobutton(frame_mod, text=r[hi], bg='white', variable=v, value=hi)
                radio[hi].pack()
            button17.pack()
        except:
            tkMessageBox.showinfo("Error", "Error: Couldn't establish connection to the server")

    def mod_ok(self):
        global X, frame_mod, dataobject, mainframe, v, y
        root.configure(background='light blue')
        r = dataobject.POP_USER()
        length = len(r)
        for i in range(0, length):
            if (v.get() == i):
                X = r[i]
                dataobject.PUSH_MODERATOR(X)
            else:
                X = r[i]
                dataobject.PUSH_UNMODERATOR(X)
        y = 0
        frame_mod.grid_remove()

    def sendMail(self, toaddr, regus, regpass):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        fromaddr = "d.ibrahim12@yahoo.com"
        message = " Eboard login details \n username = %s \n password = %s \n validity period = 3 days (259200 seconds)" % (
        regus, regpass)

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "userdetails"

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('plus.smtp.mail.yahoo.com', 25)
        server.starttls()
        server.login(fromaddr, "faquir")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()


def ChangeIP():
    global entry_1, label_1, button_ok
    button_IPConfig.destroy()
    label_1 = Label(frame4, text="Enter IP")
    entry_1 = Entry(frame4)
    label_1.pack()
    entry_1.pack()
    button_ok = Button(frame4, text="ok", command=OK)
    button_ok.pack(side=TOP)


def Setup():
    dataobject.UPDATE()
    try:
        db = MySQLdb.connect(passwd=dataobject.DB_Password, db=dataobject.DB_DBName, host=dataobject.DB_IP,
                             port=dataobject.DB_PORT, user=dataobject.DB_UserName)
    except:
        tkMessageBox.showinfo("Error", "Error1: message cannot be diaplayed")
    try:
        dataobject.CREATE_TABLE()
    except:
        tkMessageBox.showinfo("Error", "Table already exists")
    try:
        dataobject.CREATE_SESSION_TABLE()
    except:
        tkMessageBox.showinfo("Error", "Table already exists")
    button_SETUP.destroy()


def OK():
    global entry_1, label_1, entry_1
    str = entry_1.get()
    fo = open("eboard.cnf", "wb")
    fo.write(str)
    fo.close()
    entry_1.delete(0, END)
    entry_1.pack_forget()
    label_1.pack_forget()
    button_ok.pack_forget()


def show1():
    global canvas
    global canvas_name, page_name
    canvas = canvas1  # DON'T REMOVE, WILL BE USED IN Toolmgmt CLASS
    canvas_name = "canvas1"
    toolobj.updateCanvas()
    page2.Hide()
    page3.Hide()
    page1.Show()
    page_name = "page1"


def show2():
    global canvas
    global canvas_name, page_name
    canvas = canvas2
    canvas_name = "canvas2"
    toolobj.updateCanvas()

    page1.Hide()
    page3.Hide()
    page2.Show()
    page_name = "page2"


def show3():
    global canvas
    global canvas_name, page_name
    canvas = canvas3
    canvas_name = "canvas3"
    toolobj.updateCanvas()
    page1.Hide()
    page2.Hide()
    page3.Show()
    page_name = "page3"


def toSSLornottoSSL(thelink, checker):
    if (checker == "YES"):
        buffer = StringIO()
        cobj = pycurl.Curl()
        sslstr = 'https://%s' % thelink
        cobj.setopt(cobj.URL, sslstr)
        cobj.setopt(pycurl.SSL_VERIFYPEER, 0)
        cobj.setopt(pycurl.SSL_VERIFYHOST, 0)
        cobj.perform()
        html = cobj.getinfo(pycurl.HTTP_CODE)
        return html

    else:
        str1 = 'http://%s' % thelink
        response = urllib2.urlopen(str1)
        html = response.read()
        jsondata = json.loads(html)
        html = jsondata['status']
        return html
        


def on_closing():
    global logus, threadflag, thread1
    threadflag = "STOP"
    try:
        if (logus != "Admin"):
            dataobject.PUSH_UNMODERATOR(logus)
            dataobject.PUSH_LOGGEDOUT(logus)
    except:
        tkMessageBox.showinfo("error", "Couldn't push logout status")
    try:
        thread1.stop()
        thread2.stop()
    except:
        tkMessageBox.showinfo("error", "couldn't stop background thread")
    root.destroy()


def CheckMod(event):
    global y
    MODSTATUS = userobject.CheckModerator(logus)

    if (MODSTATUS == "TRUE"):
        if (y == 0):
            tkMessageBox.showinfo("Moderator", "Moderator privileges are invoked")
            y = 1
        button14.pack(side=BOTTOM)
        button15.pack(side=RIGHT)
        button16.pack(side=BOTTOM)

    else:
        button14.pack_forget()
        button15.pack_forget()
        button16.pack_forget()
        button17.pack_forget()
        frame_mod.pack_forget()
        # rightside.grid_remove()


def debugging():
    global checker
    if (checker == "YES"):
        checker = "NO"
    else:
        checker = "YES"


def start_session():
    global threadflag, logus, dataobject, y
    try:
        string = "canvas1.delete(ALL)"
        toolobj.inserter(string)
        string = "canvas2.delete(ALL)"
        toolobj.inserter(string)
        string = "canvas3.delete(ALL)"
        toolobj.inserter(string)

        try:
            frame1.grid_remove()
            frame2.grid_remove()
            frame3.grid_remove()
            frame5.grid_remove()
            frame4.grid_remove()
            mainframe.grid(row=0, column=0, sticky=(N, E, S, W))
            root.config(menu=menu1)
            threadflag = "RUN"
            dataobject.PUSH_MODERATOR(logus)
            thread1.start()
        except:
            tkMessageBox.showinfo("Moderator", "unable to start thread")
    except:
        tkMessageBox.showinfo("Moderator", "unable to intialize session")
    tkMessageBox.showinfo("Moderator", "Moderator privileges are invoked")
    y = 1


clr = "black"
clrfill = "white"
thck = 1
thckera = 10
fnt = "Helvetica"
rndfont = 16
bold = 'normal'
slant = 'roman'
AL = []
thread_ID = 2
i = 0
V = 3
y = 0
AL.append('#')
AL.append('#')
len_old = 0
threadflag = "RUN"
MODSTATUS = "FALSE"
LOCKSTATUS = "FALSE"
reg_flag = "FALSE"
checker = "NO"

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.protocol("WM_DELETE_WINDOW", on_closing)
mainframe = Frame(root)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

canvas1 = Canvas(mainframe, bg='white')
canvas2 = Canvas(mainframe, bg='white')
canvas3 = Canvas(mainframe, bg='white')

page1 = Sheetmgmt(canvas1)
page2 = Sheetmgmt(canvas2)
page3 = Sheetmgmt(canvas3)
page_name = "page1"
canvas = canvas1
canvas.bind("<Enter>", CheckMod)
canvas.bind("<Leave>", CheckMod)
canvas_name = "canvas1"
lock_flag = "FALSE"



page1.Show()
toolobj = Toolmgmt()
dataobject = Databaser()
userobject = Usermgmt()

thread1 = myThread(1, "TH", "RETRIEVE")
thread2 = myThread(2, "TH", "REGISTER")

frame1 = Frame(root, bg='light blue')
labeleboard = Label(frame1, text="EBOARD", font=('Broadway', 50), bg='light blue')
labelhome = Label(frame1, text="HOME PAGE", font=('Broadway', 50), bg='light blue')
frame1.grid(row=0, column=0, sticky=(N, E, S, W))
labeleboard.grid(row=0, column=1)
labelhome.grid(row=1, column=1)
frame2 = Frame(root, bg='light blue')
frame3 = Frame(root, bg='light blue')
frame4 = Frame(root, bg='light blue')
frame5 = Frame(root, bg='light blue')
frame_mod = Frame(root, bg='white')
frame_text=Frame(root,bg='white')
enter = Entry(frame_text,bg="grey")

login = Button(frame1, text="LOGIN", command=userobject.login, height=2, width=9, bg='white', font=(20))
login.grid(padx=550, pady=300, row=2, column=1, sticky=(N, E, S, W))


def employee():
    global status, V
    V = 1
    status = "Employee"
    userobject.register()


def customeremp():
    global status, V
    V = 0
    status = "Customer"
    userobject.register()


def customeradm():
    global status, V
    V = 1
    status = "Customer"
    userobject.register()


OK_log = Button(frame2, text='OK', bg='white', command=userobject.Ok_log, width=10)
OK_reg = Button(frame3, text='OK', bg='white', command=userobject.Ok_reg, width=10)
Back_log = Button(frame2, text='Back', bg='white', command=userobject.Bac, width=10)
Back_reg = Button(frame3, text='Back', bg='white', command=userobject.Bac, width=10)
logout_admin = Button(frame4, text='logout', bg='white', command=userobject.logout)
logout_employee = Button(frame5, text='logout', bg='white', command=userobject.logout)
user_log = Entry(frame2, bd=5)
pass_log = Entry(frame2, bd=5, show="*")
user_reg = Entry(frame3, bd=5)
email_reg = Entry(frame3, bd=5)

button0 = Button(mainframe, text="Clear", command=toolobj.Clear)
button0.grid(row=1, column=0, sticky=(N, E, S))
button1 = Button(mainframe, text="Pencil", command=toolobj.Pencil)
button1.grid(row=1, column=1, sticky=(N, E, S))
button2 = Button(mainframe, text="Eraser", command=toolobj.Eraser)
button2.grid(row=1, column=2, sticky=(N, E, S))
button4 = Button(mainframe, text="Circle/Oval", command=toolobj.Oval)
button4.grid(row=1, column=3, sticky=(N, E, S))
button5 = Button(mainframe, text="Rectangle/Square", command=toolobj.rect)
button5.grid(row=1, column=4, sticky=(N, E, S))
button6 = Button(mainframe, text="Polyline", command=toolobj.Polyline)
button6.grid(row=1, column=5, sticky=(N, E, S))
button7 = Button(mainframe, text="Line", command=toolobj.Line)
button7.grid(row=1, column=6, sticky=(N, E, S))
button8 = Button(mainframe, text="Arrow", command=toolobj.Arrow)
button8.grid(row=1, column=7, sticky=(N, E, S))
button9 = Button(mainframe, text="Text", command=toolobj.Text_input)
button9.grid(row=1, column=8, sticky=(N, E, S))
var = StringVar()
button10 = Radiobutton(frame_text, text="Bold Text", variable=var, value=1, command=toolobj.bold)
button11 = Radiobutton(frame_text, text="Normal Text", variable=var, value=2, command=toolobj.normal)
v = StringVar()
button12 = Radiobutton(frame_text, text="Italic", variable=v, value=1, command=toolobj.italic)
button13 = Radiobutton(frame_text, text="Roman", variable=v, value=2, command=toolobj.roman)
button14 = Button(mainframe, text="UNDO", bg='light blue', command=toolobj.Undo)
button15 = Button(mainframe, text="LOCK", bg='light blue', command=userobject.locker)
button15b = Button(mainframe, text="UNLOCK", bg='light blue', command=userobject.unlocker)
button16 = Button(mainframe, text='CHANGE MODERATOR', bg='light blue', command=userobject.modselection)
button17 = Button(frame_mod, text='OK', bg='white', command=userobject.mod_ok)

Adminlabel = Label(frame4, text="ADMIN PAGE", font=('Broadway', 40), bg='light blue')
Adminlabel.pack(pady=100, side=TOP)
button_IPConfig = Button(frame4, text="CHANGE IP", bg='white', command=ChangeIP)
button_SETUP = Button(frame4, text="SETUP", bg='white', command=Setup)
button_SETUP.pack(side=TOP, pady=10)
button_create_employee = Button(frame4, text="CREATE EMPLOYEE", bg='white', command=employee)
button_create_employee.pack(side=TOP, pady=10)
button_create_custadmin = Button(frame4, text="CREATE CUSTOMER", bg='white', command=customeradm)
button_create_custadmin.pack(side=TOP, pady=10)
logout_admin.pack(side=TOP, pady=10)
EMPLOYEElabel = Label(frame5, text="EMPLOYEE   PAGE", font=('Broadway', 30), bg='light blue')
EMPLOYEElabel.pack(pady=100, side=TOP)
button_start_session = Button(frame5, text="START SESSION", command=start_session, bg='white')
button_start_session.pack(pady=30, side=TOP)
button_create_customer = Button(frame5, text="CREATE CUSTOMER", command=customeremp, bg='white')
button_create_customer.pack(side=TOP)
button_IPConfig.pack(side=TOP, pady=10)
logout_employee.pack(pady=50, side=TOP)

button_toSSLornottoSSL = Button(frame4, text="DEBUG", command=debugging)

button_toSSLornottoSSL.pack(side=TOP, pady=10)

menu1 = Menu(mainframe)
Submenu = Menu(menu1)
menu1.add_cascade(label="Colors", menu=Submenu)
Submenu.add_command(label="RED", command=toolobj.redclr)
Submenu.add_command(label="BLUE", command=toolobj.blueclr)
Submenu.add_command(label="GREEN", command=toolobj.greenclr)
Submenu.add_command(label="BLACK", command=toolobj.blackclr)

editm = Menu(menu1)
menu1.add_cascade(label="Thickness", menu=editm)
editm.add_command(label="Thickness 1", command=toolobj.thck1)
editm.add_command(label="Thickness 3", command=toolobj.thck3)
editm.add_command(label="Thickness 5", command=toolobj.thck5)

thmen = Menu(menu1)
menu1.add_cascade(label="Fill Color", menu=thmen)
thmen.add_command(label="Red", command=toolobj.redclrf)
thmen.add_command(label="Blue", command=toolobj.blueclrf)
thmen.add_command(label="Green", command=toolobj.greenclrf)
thmen.add_command(label="Black", command=toolobj.blackclrf)

sheetMenu = Menu(menu1)
menu1.add_cascade(label="Sheets", menu=sheetMenu)
sheetMenu.add_command(label="Sheet 1", command=show1)
sheetMenu.add_command(label="Sheet 2", command=show2)
sheetMenu.add_command(label="Sheet 3", command=show3)

fonts = Menu(menu1)
menu1.add_cascade(label="Text Font", menu=fonts)
fonts.add_command(label="Helvetica", command=toolobj.font1)
fonts.add_command(label="SimSun", command=toolobj.font2)
fonts.add_command(label="Times", command=toolobj.font3)
fonts.add_command(label="Stencil", command=toolobj.font4)
fonts.add_command(label="Magneto", command=toolobj.font5)
fonts.add_command(label="French Script MT", command=toolobj.font6)

fontsize = Menu(menu1)
menu1.add_cascade(label="Text Font Size", menu=fontsize)
fontsize.add_command(label="16", command=toolobj.size1)
fontsize.add_command(label="20", command=toolobj.size2)
fontsize.add_command(label="24", command=toolobj.size3)
fontsize.add_command(label="28", command=toolobj.size4)
fontsize.add_command(label="32", command=toolobj.size5)
fontsize.add_command(label="36", command=toolobj.size6)

usmen = Menu(menu1)
menu1.add_cascade(label="User", menu=usmen)
usmen.add_command(label="logout", command=userobject.logout)

rel_opt = Menu(menu1)
menu1.add_cascade(label="Reload Options", menu=rel_opt)
rel_opt.add_command(label="On Click", command=toolobj.reload_event)
rel_opt.add_command(label="Playback", command=toolobj.reload_automatic)

root.configure(background='light blue')
root.geometry("1200x650")
root.mainloop()
