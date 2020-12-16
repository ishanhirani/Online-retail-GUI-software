from tkinter import*
import math,random
from tkinter import messagebox
import mysql.connector as connector

class Bill_App:
     def __init__(self,root):
          self.root=root
          self.root.geometry("1350x700+0+0")
          self.root.title("Billing Software")
          bg_color="#7E3817"
          title=Label(self.root,text="Welcome",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
#=======================Variable===================
#=======================Cosmetics==================
          self.soap=IntVar()
          self.face_wash=IntVar()
          self.cream=IntVar()
          self.shampoo=IntVar()
#=======================Grocery=====================
          self.wheat=IntVar()
          self.rice=IntVar()
          self.oats=IntVar()
          self.sugar=IntVar()
#=======================Snacks======================
          self.lays=IntVar()
          self.frooti=IntVar()
          self.chocolate=IntVar()
          self.colddrink=IntVar()
#======================Total========================
          self.total_Cosmetics=StringVar()
          self.tota_Grocery=StringVar()         
          self.total_Snacks=StringVar()
#==================function for customer name===========
          self.c_bank=StringVar()
          self.c_account=StringVar()

          self.bill_no=StringVar()
          x=random.randint(1000,9999)
          self.bill_no.set(str(x))

          self.cphone=StringVar()
#==================Customer Detail Frame=================
          F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bank Details",font=("times new roman",12,"bold"),fg="gold",bg=bg_color)
          F1.place(x=0,y=80,relwidth=1)

          cname_lbl=Label(F1,text="Bank Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
          cname_txt=Entry(F1,width=15,textvariable=self.c_bank,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

          cphn_lbl=Label(F1,text="Account No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
          cname_txt=Entry(F1,width=20,textvariable=self.c_account,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

          cphone=Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
          cname_txt=Entry(F1,width=20,textvariable=self.cphone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

          #bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

# #===================Cosmetic Frame========================
          F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F2.place(x=5,y=180,width=325,height=380)

          soap_lbl=Label(F2,text="Soap",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
          soap_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          face_wash_lbl=Label(F2,text="Face Wash",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
          face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          cream_lbl=Label(F2,text="Cream",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
          cream_txt=Entry(F2,width=10,textvariable=self.cream,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          shampoo_lbl=Label(F2,text="Shampoo",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
          shampoo_txt=Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
# #====================Grocery Frame=======================================
          F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F3.place(x=340,y=180,width=325,height=380)

          g1_lbl=Label(F3,text="Wheat",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
          g1_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          g2_lbl=Label(F3,text="Rice",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
          g2_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          g3_lbl=Label(F3,text="Oats",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
          g3_txt=Entry(F3,width=10,textvariable=self.oats,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          g4_lbl=Label(F3,text="Sugar",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
          g4_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

# #===================Snacks Frame============================================
          F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Snacks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F4.place(x=670,y=180,width=325,height=380)

          c1_lbl=Label(F4,text="lays",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
          c1_txt=Entry(F4,width=10,textvariable=self.lays,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          c2_lbl=Label(F4,text="frooti",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
          c2_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          c3_lbl=Label(F4,text="chocolate",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
          c3_txt=Entry(F4,width=10,textvariable=self.chocolate,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)

          c4_lbl=Label(F4,text="colddrink",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
          c4_txt=Entry(F4,width=10,textvariable=self.colddrink,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

# #===========================Bill Area=========================================
          F5=Frame(self.root,bd=10,relief=GROOVE)
          F5.place(x=1010,y=180,width=350,height=380)
          bill_title=Label(F5,text="Bill Area",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
          scrol_y=Scrollbar(F5,orient=VERTICAL)
          self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
          scrol_y.pack(side=RIGHT,fill=Y)
          scrol_y.config(command=self.txtarea.yview)
          self.txtarea.pack(fill=BOTH,expand=1)

# #==========================Button Frame=======================================
          F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F6.place(x=0,y=560,relwidth=1,height=140)

          m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")
          m1_txt=Entry(F6,width=18,textvariable=self.total_Cosmetics,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

          m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="w")
          m2_txt=Entry(F6,width=18,textvariable=self.tota_Grocery,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

          m3_lbl=Label(F6,text="Total snacks Price",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="w")
          m3_txt=Entry(F6,width=18,textvariable=self.total_Snacks,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

          
          btn_F=Frame(F6,bd=7,relief=GROOVE)
          btn_F.place(x=450,width=820,height=105)

          total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=15,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=10)
          Gbill_btn=Button(btn_F,text="Generate bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=10)
          clear_btn=Button(btn_F,text="clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=10)
          Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=10)
          self.welcome_bill()

     def total(self):
          self.c_s_p=self.soap.get()*40
          self.c_fw_p=self.face_wash.get()*120
          self.c_c_p=self.cream.get()*60
          self.c_sh_p=self.shampoo.get()*180
          self.total_Cosmetic_price=(
                                        self.c_s_p+
                                        self.c_fw_p+
                                        self.c_c_p+
                                        self.c_sh_p
                                        )
          self.total_Cosmetics.set("Rs " + str(self.total_Cosmetic_price))
          

          self.g_w_p=self.wheat.get()*30
          self.g_r_p=self.rice.get()*60
          self.g_o_p=self.oats.get()*80
          self.g_s_p=self.sugar.get()*40
          self.tota_Grocery_price=(
                                        self.g_w_p+
                                        self.g_r_p+
                                        self.g_o_p+
                                        self.g_s_p
                                        )
          self.tota_Grocery.set("Rs " + str(self.tota_Grocery_price))

          self.s_l_p=self.lays.get()*40
          self.s_f_p=self.frooti.get()*120
          self.s_ch_p=self.chocolate.get()*60
          self.s_c_p=self.colddrink.get()*180
          self.total_Snacks_price=(
                                        self.s_l_p+
                                        self.s_f_p+
                                        self.s_ch_p+
                                        self.s_c_p
                                        )
          self.total_Snacks.set("Rs " + str(self.total_Snacks_price))

          self.Total_bill=self.total_Cosmetic_price+self.tota_Grocery_price+self.total_Snacks_price


     def welcome_bill(self):
          self.txtarea.delete('1.0',END)
          self.txtarea.insert(END,"\t  \tVISIT AGAIN \n")
          self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
          self.txtarea.insert(END,f"\n Bank Name : {self.c_bank.get()}")
          self.txtarea.insert(END,f"\n Account Number : {self.c_account.get()}")
          self.txtarea.insert(END,"\n######################################")
          self.txtarea.insert(END,"\t Product\t\tQTY\t\tprice")
          self.txtarea.insert(END,"\n######################################")

          
     def bill_area(self):
          if self.c_bank.get()=="" or self.c_account.get()=="":
               messagebox.showerror("Error","Enter details")

          elif self.total_Cosmetics.get()=="Rs 0" and self.tota_Grocery.get()=="Rs 0" and self.total_Snacks.get()=="Rs 0":
               messagebox.showerror("Error","No item purchased")

          else:
               self.welcome_bill()

               con=connector.connect(host='localhost',port='3306',user='root',password='123456',database='retail')
               cur=con.cursor()
               #=============costmatics details =================
               if self.soap.get()!=0:
                    self.txtarea.insert(END,f"\n Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
                    
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1001
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1001,0)
                                   )
                    

                    con.commit()

               if self.face_wash.get()!=0:
                    self.txtarea.insert(END,f"\n face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1002
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1002,0)
                                   )

                    con.commit()
                    

               if self.cream.get()!=0:
                    self.txtarea.insert(END,f"\n Cream\t\t{self.cream.get()}\t\t{self.c_c_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1003
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1003,0)
                                   )

                    con.commit()

               if self.shampoo.get()!=0:
                    self.txtarea.insert(END,f"\n Shampoo\t\t{self.shampoo.get()}\t\t{self.c_sh_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1004
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1004,0)
                                   )

                    con.commit()

               #========================grocery===================
               if self.wheat.get()!=0:
                    self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1005
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1005,0)
                                   )

                    con.commit()

               if self.rice.get()!=0:
                    self.txtarea.insert(END,f"\n rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1006
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1006,0)
                                   )

                    con.commit()

               if self.oats.get()!=0:
                    self.txtarea.insert(END,f"\n Oats\t\t{self.oats.get()}\t\t{self.g_o_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1007
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1007,0)
                                   )

                    con.commit()

               if self.sugar.get()!=0:
                    self.txtarea.insert(END,f"\n Suger\t\t{self.sugar.get()}\t\t{self.g_s_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1008
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1008,0)
                                   )

                    con.commit()

               #=============snacks details =================
               if self.lays.get()!=0:
                    self.txtarea.insert(END,f"\n Lays\t\t{self.lays.get()}\t\t{self.s_l_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1009
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1009,0)
                                   )

                    con.commit()

               if self.frooti.get()!=0:
                    self.txtarea.insert(END,f"\n frooti\t\t{self.frooti.get()}\t\t{self.s_f_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1010
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1010,0)
                                   )

                    con.commit()

               if self.chocolate.get()!=0:
                    self.txtarea.insert(END,f"\n Chocalate\t\t{self.chocolate.get()}\t\t{self.s_ch_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1011
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1011,0)
                                   )

                    con.commit()

               if self.colddrink.get()!=0:
                    self.txtarea.insert(END,f"\n Coldrink\t\t{self.colddrink.get()}\t\t{self.s_c_p}")
                    cur.execute("insert into pro_bill (billno,pid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    1012
                                    ))
               
                    con.commit()
                    cur.execute("update product set stock = stock - %s where pid = %s and stock > %s",
                                   (    
                                        self.soap.get(),
                                        1012,0)
                                   )

                    con.commit()

               self.txtarea.insert(END,"\n======================================")
               if self.total_Cosmetics.get()!="Rs 0":
                    self.txtarea.insert(END,f"\n Cosmetic Total\t\t\t{self.total_Cosmetics.get()}")
                    cur.execute("insert into sup_bill (billno,sid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    100
                                    ))
               
                    con.commit()
                    

               if self.tota_Grocery.get()!="Rs 0":
                    self.txtarea.insert(END,f"\n Grocery Total\t\t\t{self.tota_Grocery.get()}")
                    cur.execute("insert into sup_bill (billno,sid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    200
                                    ))
               
                    con.commit()

               if self.total_Snacks.get()!="Rs 0":
                    self.txtarea.insert(END,f"\n Snacks Total\t\t\t{self.total_Snacks.get()}")
                    cur.execute("insert into sup_bill (billno,sid) values(%s,%s)",
                                    (self.bill_no.get(),
                                    300
                                    ))
               
                    con.commit()

               
               self.txtarea.insert(END,"\n======================================")
               self.txtarea.insert(END,f"\n Total Bill: \t\t\t Rs. {self.Total_bill}")

               cur.execute("insert into bill (billno,total,c_phone) values(%s,%s,%s)",
                                    (self.bill_no.get(),
                                    self.Total_bill,
                                    self.cphone.get()
                                    ))

               cur.execute("insert into bank (acc_no,bankname,billno) values(%s,%s,%s)",
                                   (
                                        self.c_account.get(),
                                        self.c_bank.get(),
                                        self.bill_no.get()
                                        
                                   ))
               
               con.commit()
               con.close() 
               messagebox.showinfo("success","data stored successfully",parent=self.root)

               
               
               
               

               


    
     def clear_data(self):

          op=messagebox.askyesno("Clear","Do you really want to clear?")
          if op>0:
               self.soap.set(0)
               self.face_wash.set(0)
               self.cream.set(0)
               self.shampoo.set(0)

               self.wheat.set(0)
               self.rice.set(0)
               self.oats.set(0)
               self.sugar.set(0)

               self.lays.set(0)
               self.frooti.set(0)
               self.chocolate.set(0)
               self.colddrink.set(0)

               self.total_Cosmetics.set("")
               self.tota_Grocery.set("")         
               self.total_Snacks.set("")
          

               self.c_bank.set("")
               self.c_account.set("")

               self.bill_no.set("")
               x=random.randint(1000,9999)
               self.bill_no.set(str(x))

               self.cphone.set("")

               
               self.welcome_bill()

     def Exit_app(self):
          op=messagebox.askyesno("Exit","Do you really want to exit?")
          if op>0:
               self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
