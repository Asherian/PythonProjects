""""
Your script will need to use Python 3 and the Tkinter module.
Your script will need to re-create an exact copy of a GUI from the supplied image at the bottom of this page.
"""
import tkinter
from tkinter import *
import os

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(500,200))
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')
        
        self.varSource = StringVar()
        self.varDestination = StringVar()
        
        
        self.btnBrowOne = Button(self.master, text="Browse Source", width=14, height=1,command=self.browSource)
        self.btnBrowOne.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowOne = Button(self.master, text="Browse Destination", width=14, height=1,command=self.browDestination)
        self.btnBrowOne.grid(row=1, column=0, padx=(30,0), pady=(30,0))
        

        self.txtSource = Entry(self.master,text=self.varSource, font=("Helvetica",16), fg='black', bg='white')
        self.txtSource.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)

        self.txtDestination = Entry(self.master,text=self.varDestination, font=("Helvetica",16), fg='black', bg='white')
        self.txtDestination.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)

        self.btnCheck = Button(self.master, text="Check for files", width=12, height=2,command=self.Check)
        self.btnCheck.grid(row=2, column=0, padx=(30,0), pady=(20,0))

        self.btnMove = Button(self.master, text="Move Files", width=12, height=2, command=self.Move)
        self.btnMove.grid(row=2, column=1, padx=(30,0), pady=(20,0))


        self.btnClose = Button(self.master, text="Close Program", width=12, height=2,command=self.Close)
        self.btnClose.grid(row=2, column=2, padx=(0,0), pady=(0,0),sticky=SE)





    def Close(self):
        self.master.destroy()
        
    def browSource(self):
       sn=self.varSource.get()
       

    def browDestination(self):
        dn=self.varDestination.get()

    def Check(self):
        path=os.listdir()
        fName=os.listdir(path='C:\\TechAcademy\\Python\\Projects\\')
        fPath='C:\\TechAcademy\\Python\\Projects\\'
        for filename in os.listdir(path='C:\\TechAcademy\\Python\\Projects\\'):
            if filename.endswith('.txt'):
                print(filename)
                paths=os.path.join(fPath, filename)
                print(os.path.getmtime(paths))
                continue
            else:
                continue

    def Move(self):
        c=complicated

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

