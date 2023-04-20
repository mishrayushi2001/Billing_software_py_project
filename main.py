from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
    # Image1
        img = Image.open("image/images1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg =ImageTk.PhotoImage(img)

        lb1_img =Label(self.root,image= self.photoimg)
        lb1_img.place(x=0,y=0,width =500,height = 130)

    #Image2
        img_1 = Image.open("image/images2.jpg")
        img_1 = img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1 =ImageTk.PhotoImage(img_1)

        lb1_img_1 =Label(self.root,image= self.photoimg_1)
        lb1_img_1.place(x=500,y=0,width =500,height = 130)

    #Image3
        img_2 = Image.open("image/images3.jpg")
        img_2 = img_2.resize((520,130),Image.ANTIALIAS)
        self.photoimg_2 =ImageTk.PhotoImage(img_2)

        lb1_img_2 =Label(self.root,image= self.photoimg_2)
        lb1_img_2.place(x=1000,y=0,width =520,height = 130)



        lbl_title =Label(self.root,text ="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        Main_Frame =Frame(self.root,bd=5,relief=GROOVE,bg ="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #customer LabelFrame
        Cust_Frame =LabelFrame(Main_Frame,text="Customer",font=("times new roman",35,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        self.lbl_mob = Label(Cust_Frame,text="Mobile No.",font=("times new room",12,"bold"),bg="White")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame,font=("times new roman",12,"bold"),width =24)
        self.entry_mob.grid(row=0, column=1)

        self.lblCustName = Label(Cust_Frame,font=("times new roman",12,"bold"),width =24)
        self.lblCustName.grid(row=1, column=1,sticky=W,padx=5,pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width =24)
        self.entry_mob.grid(row=1, column=1,stcky =W,pad=5,pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame,font=("times new roman",12,"bold"),width =24)
        self.entry_mob.grid(row=0, column=1)

        self.entry_mob = ttk.Entry(Cust_Frame,font=("times new roman",12,"bold"),width =24)
        self.entry_mob.grid(row=0, column=1)

if __name__ =='__main__':
    root =Tk()
    obj=Bill_App(root)
    root.mainloop()