from tkinter import*
from tkinter import font
from PIL import ImageTk,ImageDraw
import mysql.connector as connector
from tkinter import ttk,messagebox

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #============background colour===============#
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        #===========Frames====================#
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)


        #============Title==================#
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        #==============Email=================#
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",18,"bold"),bg="lightgray")
        self.txt_email.place(x=250,y=190,width=350,height=35)

        #==============Password================#
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass=Entry(login_frame,font=("times new roman",18,"bold"),bg="lightgray")
        self.txt_pass.place(x=250,y=290,width=350,height=35)

        #=============Register button for new user================#
        btn_reg=Button(login_frame,text="Register new Account?",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=250,y=330)

        #=============Login=====================#
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)

    def register_window(self):
        #code to switch from current window to new window
        self.root.destroy()
        import register


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=connector.connect(host='localhost',port='3306',user='root',password='123456',database='retail')
                cur=con.cursor()
                cur.execute("select * from customer where email=%s and password=%s",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                else:
                    messagebox.showinfo("success","welcome",parent=self.root)
                    self.root.destroy()
                    import bill
                    
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

        

root=Tk()
obj=Login_window(root)
root.mainloop()