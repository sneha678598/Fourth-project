from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600")
        self.root.title("QR Generator| Developed by Sneha")
        self.root.resizable(False,False)
        self.root.config(bg='#f4ede4')
        title = Label(self.root,text = "  QR Code Generator", font = ('times new roman',30,'bold'), width = 80, height=2, bg='#053246',
                      fg  = 'white',anchor='w')
        title.place(x=0,y=0,relwidth=1)
        
        #Employee deatils wimdow
        #===Variables=====
        self.var_Employee_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Department=StringVar()
        self.var_Designation=StringVar()
        
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE, bg='white')
        emp_Frame.place(x=50,y=130,width=550,height=450)
        
        l1 = Label(emp_Frame,text="Employee Details", font = ('goudy old style',20),height=1, bg='#043246',
                      fg='white')
        
        l1.place(x=0,y=0,relwidth=1)
        
        l2 = Label(emp_Frame,text="Employee_ID", font = ('times new roman',15,'bold'),height=1, bg='white',
                      fg  = 'black')
        l2.place(x=20,y=60)
        
        l3 = Label(emp_Frame,text="Name", font = ('times new roman',15,'bold'),height=1, bg='white',
                      fg  = 'black')
        l3.place(x=20,y=120)
        
        l4 = Label(emp_Frame,text="Department", font = ('times new roman',15,'bold'),height=1, bg='white',
                      fg  = 'black')
        l4.place(x=20,y=180)
        
        
        l5 = Label(emp_Frame,text="Designation", font = ('times new roman',15,'bold'),height=1, bg='white',
                      fg  = 'black')
        l5.place(x=20,y=240)
        
        #Entry
        
        e1 = Entry(emp_Frame,font =("times new roman",15),textvariable=self.var_Employee_ID, bg = 'light yellow')
        e1.place(x=250,y=60)
        
        e2 = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_Name, bg = 'light yellow')
        e2.place(x=250,y=120)
        
        e3 = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_Department, bg = 'light yellow')
        e3.place(x=250,y=180)
        
        e4 = Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_Designation, bg = 'light yellow')
        e4.place(x=250,y=240)
        
        #button
        
        b1 =Button(emp_Frame,text = ' Generate QR ', command=self.generate, font = ('times new roman',18,'bold'),height=1, bg='#2196f3',
                      fg  = 'white')
        b1.place(x =100 ,y=300,width=200,height=30)
        
        b2 =Button(emp_Frame,text = 'Clear', command=self.clear, font = ('times new roman',18,'bold'),height=1, bg='#607d8b',
                      fg  = 'white')
        b2.place(x =350,y=300,width=120,height=30)
        
        self.msg=''
        self.l1_msg=Label(emp_Frame,text=self.msg, font = ('times new roman',20),height=1, bg='white',
                      fg='green')
        self.l1_msg.place(x=0,y=370,relwidth=1)
        
        
        emp_Frame1=Frame(self.root,bd=2,relief=RIDGE, bg='white')
        emp_Frame1.place(x=750,y=130,width=300,height=440)
        
        l1 = Label(emp_Frame1,text="Employee QR Code", font = ('goudy old style',20),height=1, bg='#043246',
                      fg='white')
        l1.place(x=0,y=0,relwidth=1)
        
        self.l2_msg=Label(emp_Frame1,text='No Qr\nNot Available',font=('times new roman',15),bg='#3f51b5',
                         fg='white')
        self.l2_msg.place(x=55,y=150,width=180,height=180)
        
    def clear(self):
        self.var_Employee_ID.set('')
        self.var_Name.set('')
        self.var_Department.set('')
        self.var_Designation.set('')
        self.msg=''
        self.l1_msg.config(text=self.msg,fg='green')    
        self.l2_msg.config(image='')        
            
    def generate(self):
        if (self.var_Employee_ID.get()==''or self.var_Name.get()=='' or self.var_Department.get()=='' or
            self.var_Designation.get()==''):
            self.msg='Fill all blanks'
            self.l1_msg.config(text=self.msg)
        else:
            qr_data=(f'Employee_ID:{self.var_Employee_ID.get()}\nName:{self.var_Name.get()}\nDepartment:{self.var_Department.get()}\nDescription:{self.var_Designation.get()}')
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_QR\Emp_"+str(self.var_Employee_ID.get())+'.png')
            
            #=====QR code Image update===============
            self.im=ImageTk.PhotoImage(file="Employee_QR/Emp_"+str(self.var_Employee_ID.get())+'.png')
            self.l2_msg.config(image=self.im)
            self.msg='QR Generated Successfully!!!'
            self.l1_msg.config(text=self.msg,fg='green')    
                    
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
