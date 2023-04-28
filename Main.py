from  tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import pymysql
import datetime




class GabhaLibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("GABHA Library Management System")
        self.root.geometry("1550x800+0+0")

#=======================================Variable======================================
        self.member_var=StringVar()
        self.prnn_var=StringVar()
        self.title_var=StringVar()
        self.firstName_var=StringVar()
        self.LastName_var=StringVar()
        self.Address1_var=StringVar()
        self.Address2_var=StringVar()
        self.Postid_var=StringVar()
        self.Mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.days_var=StringVar()
        self.latereturn_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()



        lbltitle=Label(self.root,text="GABHA Library Sanagement System",bg="#CACAFF",fg="#5C5C5C",bd=20,relief=RIDGE,font=("time new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame1=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='#CACAFF')
        frame1.place(x=0,y=130,width=1530,height=400)


#=======================================DataLeft======================================
        DataFrameLeft=LabelFrame(frame1,text="Library Membership Information ",bg="#CACAFF",fg="#45458B",bd=12,relief=RIDGE,font=("time new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=850,height=350)

        lblMember=Label(DataFrameLeft,text="Member Type",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W) 

        comMember=ttk.Combobox(DataFrameLeft, font=("time new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember['value']=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPNR_No=Label(DataFrameLeft,text="PNR No.",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblPNR_No.grid(row=1,column=0,sticky=W)
        txtPNR_No=Entry(DataFrameLeft,bg="white",font=("time new roman",12,"bold"),textvariable=self.prnn_var,width=29)
        txtPNR_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,text="ID No:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.title_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirst=Label(DataFrameLeft,text="FirstName:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblFirst.grid(row=3,column=0,sticky=W)
        txtFirst=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.firstName_var,width=29)
        txtFirst.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,text="LastName:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.LastName_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,text="Address1:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.Address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,text="Address2:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.Address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,text="PostCode:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.Postid_var,width=29)
        txtPostCode.grid(row=7,column=1)


        lblMobile=Label(DataFrameLeft,text="Mobile:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.Mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,text="Book ID:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,text="Book Title:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,text="Auther Name:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,text="Date Borrowed:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,text="Date Deu:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.days_var,width=29)
        lblDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,text="Late Return Fine:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        lblLateReturnFine=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.latereturn_var,width=29)
        lblLateReturnFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameLeft,text="Date Over Due:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        lblDateOverdate=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        lblDateOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,text="Acrual Price:",bg="#CACAFF",fg="#383838",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        lblActualPrice=Entry(DataFrameLeft,bg="white",font=("time new roman",13,"bold"),textvariable=self.finalprice_var,width=29)
        lblActualPrice.grid(row=8,column=3)
        

        


        


#=======================================DataRight======================================

        DataFrameRight=LabelFrame(frame1,text="Book Details",bg="#CACAFF",fg="#45458B",bd=12,relief=RIDGE,font=("time new roman",12,"bold"))
        DataFrameRight.place(x=880,y=5,width=420,height=350)

        self.txtBox=Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head firt Book','Learn Python','Python Programming','Secrete Rehshy','Python CookBook','Into to Machine Leaning ',
                 'Machine teco','My Python ','Head-First Python','Invent','Think Python',
                 'Effective Computation in Physics','Learn Python','Teach Your Kids to Code',
                 'Python Tricks','Fluent Python','Effective Python','Python Cookbook','Get Coding'
            
        ]

        def SelectBook(event=""):
                value=str(listBox.get(listBox.curselection()))
                x=value
                if (x=="Head firt Book"):
                        self.bookid_var.set("BKID5454")
                        self.booktitle_var.set("Python Mannual")
                        self.auther_var.set("Paul Barry")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.days_var.set(15)
                        self.latereturn_var.set("Rs.70")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs.788")


                elif (x=="Learn Python"):
                        self.bookid_var.set("BKID5457")
                        self.booktitle_var.set("Python Mannual")
                        self.auther_var.set("Paul Barry")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.days_var.set(15)
                        self.latereturn_var.set("Rs.70")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs.788")

                elif (x=="Python Programming"):
                        self.bookid_var.set("BKID5457")
                        self.booktitle_var.set("Python Mannual")
                        self.auther_var.set("Paul Barry")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.days_var.set(15)
                        self.latereturn_var.set("Rs.70")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs.788")

                elif (x=="Secrete Rehshy"):
                        self.bookid_var.set("BKID5457")
                        self.booktitle_var.set("Python Mannual")
                        self.auther_var.set("Paul Barry")

                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.days_var.set(15)
                        self.latereturn_var.set("Rs.70")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs.788")

        listBox=Listbox(DataFrameRight,fg="#383838",font=("arial",12,"bold"),width=12,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
#=======================================Button Frame======================================


        frameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='#CACAFF')
        frameButton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(frameButton,text="Add Data",command=self.add_data,font=("arial",12,"bold"),width=20,bg="#CDCDB7",fg="#424242")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(frameButton,command=self.Showdata,text="Show Data",font=("arial",12,"bold"),width=20,bg="#CDCDB7",fg="#424242")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(frameButton,command=self.update_data,text="Update",font=("arial",12,"bold"),width=20,bg="#CDCDB7",fg="#424242")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(frameButton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=20,bg="#CDCDB7",fg="#424242")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(frameButton,command=self.Reset,text="Reset",font=("arial",12,"bold"),width=23,bg="#CDCDB7",fg="#424242")
        btnReset.grid(row=0,column=4)

        btnExit=Button(frameButton,command=self.Exit,text="Exit",font=("arial",12,"bold"),width=23,bg="#CDCDB7",fg="#424242")
        btnExit.grid(row=0,column=5)
        
#=======================================Function Information======================================


        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='#CACAFF')
        frameDetails.place(x=0,y=600,width=1530,height=135)

        Table_frame=Frame(self.root,bd=12,relief=RIDGE,padx=20 ,bg="#CACAFF")
        Table_frame.place(x=0,y=590,width=1460,height=130)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstName","LastName","Address1","Address2","Postid",
                                                            "Mobile","bookid","booktitle","auther","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Ttile")
        self.library_table.heading("firstName",text="First Name")
        self.library_table.heading("LastName",text="Last Name")
        self.library_table.heading("Address1",text="Address1")
        self.library_table.heading("Address2",text="Address2")
        self.library_table.heading("Postid",text="Post ID")
        self.library_table.heading("Mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Deu")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="Late Retrun fine")
        self.library_table.heading("dateoverdue",text="Date Over Deu")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("Postid",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        con=pymysql.connect(host="localhost",user='root',passwd='',database='librarygabha')
        cur=con.cursor()
        cur.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.member_var.get(),
                                                                                                        self.prnn_var.get(),
                                                                                                        self.title_var.get(),
                                                                                                        self.firstName_var.get(),
                                                                                                        self.LastName_var.get(),
                                                                                                        self.Address1_var.get(),
                                                                                                        self.Address1_var.get(),
                                                                                                        self.Postid_var.get(),
                                                                                                        self.Mobile_var.get(),
                                                                                                        self.bookid_var.get(),
                                                                                                        self.booktitle_var.get(),
                                                                                                        self.auther_var.get(),
                                                                                                        self.dateborrowed_var.get(),
                                                                                                        self.datedue_var.get(),
                                                                                                        self.days_var.get(),
                                                                                                        self.latereturn_var.get(),
                                                                                                        self.dateoverdue_var.get(),
                                                                                                        self.finalprice_var.get()
                                                                                                        ))
        con.commit()
        con.close()
        self.Reset()
        messagebox.showinfo("Success","Member has been insert  Successfully!!")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user='root',passwd='',database='librarygabha')
        cur=con.cursor()
        cur.execute("select * from library")
        rows=cur.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert('',END,values=row)
                con.commit()
        con.close()

    def get_cursor(self, gabha):
        cursor_row=self.library_table.focus()
        contents=self.library_table.item(cursor_row)
        row=contents['values']
        self.member_var.set(row[0])
        self.prnn_var.set(row[1])
        self.title_var.set(row[2])
        self.firstName_var.set(row[3])
        self.LastName_var.set(row[4])
        self.Address1_var.set(row[5])
        self.Address2_var.set(row[6])
        self.Postid_var.set(row[7])
        self.Mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.days_var.set(row[14])
        self.latereturn_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])




    def update_data(self):
        con=pymysql.connect(host="localhost",user='root',passwd='',database='librarygabha')
        cur=con.cursor()
        cur.execute("update library set membertype=%s,title=%s,firstName=%s,LastName=%s,Address1=%s,Address2=%s,Postid=%s,Mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed%s,datedue=%s,days=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s, where prnno=%s,",(
                                                                                                                                                                                                                                                                        self.member_var.get(),
                                                                                                                                                                                                                                                                        self.title_var.get(),
                                                                                                                                                                                                                                                                        self.firstName_var.get(),
                                                                                                                                                                                                                                                                        self.LastName_var.get(),
                                                                                                                                                                                                                                                                        self.Address1_var.get(),
                                                                                                                                                                                                                                                                        self.Address1_var.get(),
                                                                                                                                                                                                                                                                        self.Postid_var.get(),
                                                                                                                                                                                                                                                                        self.Mobile_var.get(),
                                                                                                                                                                                                                                                                        self.bookid_var.get(),
                                                                                                                                                                                                                                                                        self.booktitle_var.get(),
                                                                                                                                                                                                                                                                        self.auther_var.get(),
                                                                                                                                                                                                                                                                        self.dateborrowed_var.get(),
                                                                                                                                                                                                                                                                        self.datedue_var.get(),
                                                                                                                                                                                                                                                                        self.days_var.get(),
                                                                                                                                                                                                                                                                        self.latereturn_var.get(),
                                                                                                                                                                                                                                                                        self.dateoverdue_var.get(),
                                                                                                                                                                                                                                                                        self.finalprice_var.get(),
                                                                                                                                                                                                                                                                        self.prnn_var.get(),
                                                                                                                                                                                                                                                                        ))
                                                                                                                                                                                                                                                                                                                                                                
        con.commit()
        self.fetch_data()
        self.Reset()
        con.close()
        messagebox.showinfo("Update","Student Data Updated Successfully!!")


    def Showdata(self):
        self.txtBox.insert(END,"Member Type   \t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No.   \t\t"+self.prnn_var.get()+"\n")
        self.txtBox.insert(END,"Title   \t\t"+self.title_var.get()+"\n")
        self.txtBox.insert(END,"First Name   \t\t"+self.firstName_var.get()+"\n")
        self.txtBox.insert(END,"Last Name   \t\t"+self.LastName_var.get()+"\n")
        self.txtBox.insert(END,"Address1    \t\t"+self.Address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2    \t\t"+self.Address2_var.get()+"\n")
        self.txtBox.insert(END,"Postid    \t\t"+self.Postid_var.get()+"\n")
        self.txtBox.insert(END,"Book id    \t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title    \t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Auther    \t\t"+self.auther_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed   \t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due   \t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Days    \t\t"+self.days_var.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine   \t\t"+self.latereturn_var.get()+"\n")
        self.txtBox.insert(END,"Date Over Due\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Final Price   \t\t"+self.finalprice_var.get()+"\n")

        self.Reset()

    def Reset(self):
        self.member_var.set("")
        self.prnn_var.set("")
        self.title_var.set("")
        self.firstName_var.set("")
        self.LastName_var.set("")
        self.Address1_var.set("")
        self.Address2_var.set("")
        self.Postid_var.set("")
        self.Mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.days_var.set("")
        self.latereturn_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")

    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Gabha Library Management System","Do You Want Exit")
        if Exit>0:
            self.root.destroy()
            return     


    def delete(self):
        if self.prnn_var.get()=="" or self.title_var.get()=="":
             messagebox.showerror("Error","First select the Member")
        else:
             con=pymysql.connect(host="localhost",user='root',passwd='',database='librarygabha')
             cur=con.cursor()
             cur.execute("delete from library where prnno=%s",self.prnn_var.get())

             con.commit()
             self.fetch_data()
             self.Reset()
             con.close()

             messagebox.showinfo("Success","Member has been Deleted")
             
             
              

if __name__ == "__main__":
    root=Tk()
    obj=GabhaLibraryManagementSystem(root)
    root.mainloop()
