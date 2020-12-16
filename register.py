from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector as connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#808080")

        #====Bg Image===#
        self.bg=ImageTk.PhotoImage(file="images/background.jpg")
        bg=Label(self.root,image=self.bg).pack()

        #====Register Frame===#
        frame1=Frame(self.root,bg="white")
        frame1.place(x=330,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=250,y=30)

        #====First row========#
        uname=Label(frame1,text="User Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_uname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_uname.place(x=50,y=130,width=250)

        gender=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.cmb_gender=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_gender['values']=("Select","Male","Female","Other")
        self.cmb_gender.place(x=370,y=130,width=250)
        self.cmb_gender.current(0)


        #=====Second row====#
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)


        #=====Third row===#
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=270,width=250)

        cpassword=Label(frame1,text="Conform Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=270,width=250)

        #=======fourth row====#
        btn_register=Button(frame1,text="Register Now ",font=("times new roman",13,"bold"),command=self.register_data,cursor="hand2",bg="green",fg="white").place(x=150,y=360)
        self.btn_login=Button(frame1,text="Login",font=("times new roman",13,"bold"),command=self.login_window,cursor="hand2",bg="green",fg="white")
        self.btn_login.place(x=370,y=360)

    def login_window(self):
        #code to switch from current window to new window
        self.root.destroy()
        import login

        
    def clear(self):
        self.txt_uname.delete(0,END)
        self.cmb_gender.current(0)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    #====fetch data to database=====#
    def register_data(self):
        if self.txt_uname.get()==""or self.cmb_gender.get()=="Select" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password does not match with Conform Password",parent=self.root)
        else:
            try:
                con=connector.connect(host='localhost',port='3306',user='root',password='123456',database='retail')
                cur=con.cursor()
                cur.execute("select * from customer where email =%s or phone=%s",(self.txt_email.get(),self.txt_contact.get()))
                row=cur.fetchone()
                #print(row)
                
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another contact number and Email",parent=self.root)

                else:
                    cur.execute("insert into customer (name,gender,phone,email,password) values(%s,%s,%s,%s,%s)",
                                    (self.txt_uname.get(),
                                    self.cmb_gender.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Register successful",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
root=Tk()
obj=Register(root)
root.mainloop()