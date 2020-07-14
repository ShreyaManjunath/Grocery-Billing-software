from tkinter import*
import math,random,os
from tkinter import messagebox
#43C6DB
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color ="#43C6DB"
        title =Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #####################variables########

        #############cosmeticd################
        self.soap =IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.gell =IntVar()
        self.loshan=IntVar()
        self.spray =IntVar()

        ######################grocery###############
        self.rice=IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.daal= IntVar()
        self.tea = IntVar()

        ##########################cooldrink#############3
        self.maza = IntVar()
        self.mirinda = IntVar()
        self.pepsi = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.frooti = IntVar()

        ###################3Total product prices#############
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cool_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax= StringVar()
        self.cool_drink_tax = StringVar()

        ##################customer############
        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()


        ######################customer details#########3
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Detail",font=("times new roman",15,"bold"),fg="yellow",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt =Entry(F1,width=18,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1, text="Phone No:", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=18,textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        cbill_lbl = Label(F1, text="Bill No:", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=18,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn= Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=5)


        ####################costemitcs frame###########3

        F2 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="yellow",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl =Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt =Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid( row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Face_w_lb1 = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_s_lb1 = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hair_g_lb1 = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lb1 = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=10,textvariable=self.loshan, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

####################Grocerics frame###########3

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="yellow",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl =Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt =Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid( row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        g6_lb1 = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        g3_lb1 = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        g4_lb1 = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g5_lb1 = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ####################Cool drink###########3

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg="yellow", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        c2_lbl = Label(F4, text="Mirinda", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.mirinda, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lb1 = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.pepsi, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lb1 = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lb1 = Label(F4, text="Thumbs", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lb1 = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        ################Bill area########3
        F5 =Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=530, height=380)
        bill_title = Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y =Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        ############Button frame#########
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="yellow", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=240)

        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="purple",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=20,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="purple",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=20, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cooldrink Price", bg=bg_color, fg="purple",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=20, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cool_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)


        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="purple",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=20, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="purple",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=20, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cooldrinks Tax", bg=bg_color, fg="purple",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=20, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cool_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=760,height=200)

        total_btn =Button(btn_F,command=self.total,text="Total",bg="gray",fg="white",bd=5,pady=15,width=13,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=50)
        gbill_btn = Button(btn_F,command=self.bill_area, text="Generate Bill", bg="gray", fg="white", bd=5, pady=15, width=14,font="arial 15 bold").grid(row=0, column=1, padx=5, pady=50)
        clear_btn = Button(btn_F,command=self.clear_data, text="Clear", bg="gray", fg="white", bd=5, pady=15, width=13,font="arial 15 bold").grid(row=0, column=2, padx=5, pady=50)
        Exit_btn = Button(btn_F,command=self.Exit_app, text="Exit", bg="gray", fg="white", bd=5, pady=15, width=13,font="arial 15 bold").grid(row=0, column=3, padx=5, pady=50)

        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p = self.face_cream.get()* 120
        self.c_fw_p = self.face_wash.get()* 60
        self.c_hs_p = self.spray.get()* 180
        self.c_hg_p = self.gell.get()* 140
        self.c_bl_p = self.loshan.get()* 180



        self.total_cosmetic_price=float(
                                self.c_s_p+
                                self.c_fc_p+
                                self.c_fw_p+
                                self.c_hs_p+
                                self.c_hg_p+
                                self.c_bl_p

                                    )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*180
        self.g_f_p = self.food_oil.get() * 90
        self.g_s_p = self.sugar.get() * 180
        self.g_w_p = self.wheat.get() * 50
        self.g_t_p = self.tea.get() * 30
        self.g_d_p = self.daal.get() * 150


        self.total_grocery_price = float(
                                    self.g_r_p+
                                    self.g_f_p +
                                    self.g_s_p +
                                    self.g_w_p +
                                    self.g_t_p +
                                    self.g_d_p
        )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.03),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_m_p=self.maza.get()*80
        self.d_mi_p = self.mirinda.get()*80
        self.d_p_p = self.pepsi.get()*70
        self.d_l_p = self.limca.get()*50
        self.d_th_p = self.thumbsup.get()*50
        self.d_f_p = self.frooti.get()*40

        self.total_cooldrinks_price = float(
            self.d_m_p+
            self.d_mi_p +
            self.d_p_p +
            self.d_l_p +
            self.d_th_p +
            self.d_f_p
        )

        self.cool_drink_price.set("Rs. "+str(self.total_cooldrinks_price))
        self.d_tax = round((self.total_cooldrinks_price*0.08),2)
        self.cool_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                        self.total_grocery_price+
                        self.total_cooldrinks_price+
                        self.c_tax+self.g_tax+self.d_tax
                              )


    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t\t  Welcome To SuperMarket ")
        self.txtarea.insert(END,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txtarea.insert(END,f"\n  Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n  Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n  Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n#############################################################")
        self.txtarea.insert(END, f"\n Products\t\t\tQTY\t\t\tPrice")
        self.txtarea.insert(END, f"\n#############################################################")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror('Error', 'Customer details are must')
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cool_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product perchased")
        else:
            self.welcome_bill()

            ################cosmetics#############
            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t\t{self.soap.get()}\t\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END, f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\n Fash Wash\t\t\t{self.face_wash.get()}\t\t\t{self.c_fw_p}")

            if self.spray.get()!=0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t\t{self.spray.get()}\t\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t\t{self.gell.get()}\t\t\t{self.c_hg_p}")

            if self.loshan.get()!=0:
                self.txtarea.insert(END, f"\n Body Loshan\t\t\t{self.loshan.get()}\t\t\t{self.c_bl_p}")

                ################grocery#################
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice \t\t\t{self.rice.get()}\t\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil \t\t\t{self.food_oil.get()}\t\t\t{self.g_f_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar \t\t\t{self.sugar.get()}\t\t\t{self.g_s_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat \t\t\t{self.wheat.get()}\t\t\t{self.g_w_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea Powder \t\t\t{self.tea.get()}\t\t\t{self.g_t_p}")

            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal \t\t\t{self.daal.get()}\t\t\t{self.g_d_p}")

                ###############cool drinks#########
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza \t\t\t{self.maza.get()}\t\t\t{self.d_m_p}")
            if self.mirinda.get() != 0:
                self.txtarea.insert(END, f"\n Mirinda \t\t\t{self.mirinda.get()}\t\t\t{self.d_mi_p}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(END, f"\n Pepsi \t\t\t{self.pepsi.get()}\t\t\t{self.d_p_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca \t\t\t{self.limca.get()}\t\t\t{self.d_l_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\nThumbsUp \t\t\t{self.thumbsup.get()}\t\t\t{self.d_th_p}")

            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti \t\t\t{self.frooti.get()}\t\t\t{self.d_f_p}")

            self.txtarea.insert(END,f"\n-------------------------------------------------------------")
            if self.cosmetic_tax.get() !="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get() !="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t\t\t\t{self.grocery_tax.get()}")

            if self.cool_drink_tax.get() !="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cooldrinks Tax\t\t\t\t\t\t{self.cool_drink_tax.get()}")
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t\t\t\t{self.Total_bill}")
            self.txtarea.insert(END, f"\n-------------------------------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op > 0:

            self.bill_data = self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no.: {self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present ="no"

        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Erroe","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("Clear", "Do you want to clear data")
        if op>0:
            #####################variables########

            #############cosmeticd################
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            self.spray.set(0)

            ######################grocery###############
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.daal.set(0)
            self.tea.set(0)

            ##########################cooldrink#############3
            self.maza.set(0)
            self.mirinda.set(0)
            self.pepsi.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.frooti.set(0)

            ###################3Total product prices#############
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cool_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cool_drink_tax.set("")

            ##################customer############
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you reallu want to Exit")
        if op>0:
            self.root.destroy()





root =Tk()
obj = Bill_App(root)
root.mainloop()



