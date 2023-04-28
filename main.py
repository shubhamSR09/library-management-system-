from distutils.util import execute
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import pymysql
class students:
    def __init__(self, root):
        self.root=root
        self.root.title("GABHA Student Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="GABHA Student Management System",bd=10,relief=GROOVE, font=("time new roman", 40, "bold"), bg="gold",fg="dark blue")
        title.pack(side=TOP , fill=X)

        #===============All Variables============================================================
        self.Roll_No_Var=StringVar()
        self.Name_Var = StringVar()
        self.Dob_Var=StringVar()
        self.Gender_Var=StringVar()
        self.Contact_Var=StringVar()
        self.Course_Var=StringVar()

        self.Searcch_by=StringVar()
        self.Search_text=StringVar()
        



        #===============Manager Fram============================================================
        manage_frame=Frame(self.root, bd=4,relief=RAISED, bg="sky blue")
        manage_frame.place(x=20,y=100, width=450,height=600)
        
        m_title=Label(manage_frame,text="Manage Students", bg="sky blue", fg="black" ,font=("time new roman", 25, "bold"))
        m_title.grid(row=0,columnspan=2, pady=20)

        lab_roll=Label(manage_frame,text="Roll No.", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_roll.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_roll=Entry(manage_frame,textvariable=self.Roll_No_Var,font=("time new roman", 15, "bold"),bd=2,relief=GROOVE)
        txt_roll.grid(row=1,column=1, pady=10,padx=20,sticky="w")

        lab_name=Label(manage_frame,text="Name", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_name.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        txt_name=Entry(manage_frame,textvariable=self.Name_Var,font=("time new roman", 15, "bold"),bd=2,relief=GROOVE)
        txt_name.grid(row=2,column=1, pady=10,padx=20,sticky="w")

        lab_dob=Label(manage_frame,text="D.O.B", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_dob.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        txt_dob=Entry(manage_frame,textvariable=self.Dob_Var,font=("time new roman", 15, "bold"),bd=2,relief=GROOVE)
        txt_dob.grid(row=3,column=1, pady=10,padx=20,sticky="w")

        lab_gender=Label(manage_frame,text="Gender", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_gender.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        combo_gender=ttk.Combobox(manage_frame,textvariable=self.Gender_Var,font=("time new roman", 15, "bold"),state="readonly")
        combo_gender['values']=('Male','Female','Other')
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #txt_gender=Entry(manage_frame,font=("time new roman", 15, "bold"),bd=5,relief=GROOVE)
        #txt_gender.grid(row=4,column=1, pady=10,padx=20,sticky="w")

        lab_contact=Label(manage_frame,text="Contact", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_contact.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        txt_contact=Entry(manage_frame,textvariable=self.Contact_Var,font=("time new roman", 15, "bold"),bd=2,relief=GROOVE)
        txt_contact.grid(row=5,column=1, pady=10,padx=20,sticky="w")

        lab_Course=Label(manage_frame,text="Course", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_Course.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        txt_Course=Entry(manage_frame,textvariable=self.Course_Var,font=("time new roman", 15, "bold"),bd=2,relief=GROOVE)
        txt_Course.grid(row=6,column=1, pady=10,padx=20,sticky="w")

        lab_add=Label(manage_frame,text="Address", bg="sky blue", fg="white" ,font=("time new roman", 20, "bold"))
        lab_add.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        self.txt_address=Text(manage_frame,width=30, height=4,font=("",10))
        self.txt_address.grid(row=7,column=1, pady=10,padx=20,sticky="w")


#===============Button Frame============================================================

        btn_frame=Frame(manage_frame, bd=0,relief=RAISED, bg="sky blue")
        btn_frame.place(x=10,y=520, width=420)   

        add_btn=Button(btn_frame,text='Add',font=("time new roman", 10, "bold"), width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(btn_frame,text='Update', font=("time new roman", 10, "bold"), width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(btn_frame,text='Delete', font=("time new roman", 10, "bold"), width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(btn_frame,text='Clear', font=("time new roman", 10, "bold"), width=10,command=self.Clear).grid(row=0,column=3,padx=10,pady=10) 


#===============Details Frame============================================================
        details_frame=Frame(self.root, bd=4,relief=RAISED, bg="pink")
        details_frame.place(x=500,y=100, width=800,height=600)

        lbl_search=Label(details_frame,text="Search By", bg="pink", fg="black" ,font=("time new roman", 15, "bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        combo_search=ttk.Combobox(details_frame, textvariable=self.Searcch_by,font=("time new roman", 10, "bold"),state="readonly")
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=15,pady=10)

        txt_search=Entry(details_frame,textvariable=self.Search_text ,font=("time new roman", 10, "bold"),bd=2,relief=GROOVE)
        txt_search.grid(row=0,column=2, pady=10,padx=20,sticky="w")

        search_btn=Button(details_frame, text='Search', font=("time new roman", 10, "bold"),width=10,pady=5,command=self.Search_data).grid(row=0,column=3,padx=10,pady=10)
        show_btn=Button(details_frame, text='Show All',font=("time new roman", 10, "bold"), width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10) 


#===============Table Frame============================================================
        table_frame=Frame(details_frame, bd=3,relief=RAISED, bg="pink")
        table_frame.place(x=10,y=70, width=760,height=520)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Roll No.","Name","D.O.B","Gender","Contact","Course","Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No.", text="Roll No.")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("D.O.B" ,text="D.O.B")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("Course" ,text="Course")
        self.student_table.heading("Address", text="Address")
        self.student_table['show']='headings'
        self.student_table.column('Roll No.', width=100)
        self.student_table.column('Name', width=100)
        self.student_table.column('D.O.B', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('Contact',width=100)
        self.student_table.column('Course', width=100)
        self.student_table.column('Address' ,width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):
        if self.Roll_No_Var.get()=="" or self.Name_Var.get()=="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=pymysql.connect(host="localhost",user='root',passwd='',database='gabha_stm')
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_Var.get(),
                                                                            self.Name_Var.get(),
                                                                            self.Dob_Var.get(),
                                                                            self.Gender_Var.get(),
                                                                            self.Contact_Var.get(),
                                                                            self.Course_Var.get(),
                                                                            self.txt_address.get('1.0',END)    
                                                                            ))
            con.commit()
            self.fetch_data()
            self.Clear()
            con.close()
            messagebox.showinfo("Success","Registration Completed Successfully!!")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user='root',passwd='',database='gabha_stm')
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()
        con.close()

    def Clear(self):
        if self.Roll_No_Var.get()=="" or self.Name_Var.get()=="":
            messagebox.showerror("Error","Data is not found for Clearance!!")
        else:
            self.Roll_No_Var.set("")
            self.Name_Var.set("")
            self.Dob_Var.set("")
            self.Gender_Var.set("")
            self.Contact_Var.set("")
            self.Course_Var.set("")
            self.txt_address.delete("1.0",END)
            #messagebox.showinfo("Clear","Student Data Cleaned Successfully!!")
    
    def get_cursor(self, gabha):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_Var.set(row[0])
        self.Name_Var.set(row[1])
        self.Dob_Var.set(row[2])
        self.Gender_Var.set(row[3])
        self.Contact_Var.set(row[4])
        self.Course_Var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
        

    def update_data(self):
        if self.Roll_No_Var.get()=="" or self.Name_Var.get()=="":
            messagebox.showerror("Error","Data is not found for Updations!!")
        else:
            con=pymysql.connect(host="localhost",user='root',passwd='',database='gabha_stm')
            cur=con.cursor()
            cur.execute("update  students set Name=%s,DOB=%s,Gender=%s,Contact=%s,Course=%s,Address=%s where Roll_No=%s",(
                                                                                            self.Name_Var.get(),
                                                                                            self.Dob_Var.get(),
                                                                                            self.Gender_Var.get(),
                                                                                            self.Contact_Var.get(),
                                                                                            self.Course_Var.get(),
                                                                                            self.txt_address.get('1.0',END),
                                                                                            self.Roll_No_Var.get()   
                                                                                            ))
            con.commit()
            con.close()
            self.fetch_data()
            self.Clear()
            messagebox.showinfo("Update","Student Data Updated Successfully!!")
    def delete_data(self):
        if self.Roll_No_Var.get()=="" or self.Name_Var.get()=="":
            messagebox.showerror("Error","Data is not found for deletion!!")
        else:
            con=pymysql.connect(host="localhost",user='root',passwd='',database='gabha_stm')
            cur=con.cursor()
            cur.execute("delete from students where Roll_No=%s",self.Roll_No_Var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.Clear()
            #messagebox.showinfo("Delete","Student Data Deleted Successfully!!")

    def Search_data(self):
        con=pymysql.connect(host="localhost",user='root',passwd='',database='gabha_stm')
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.Searcch_by.get())+" LIKE '%"+str(self.Search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()
        con.close()
        
    

    




        
root = Tk()
ob= students(root)
root.mainloop()