""""
Your script will need to use Python 3 and the Tkinter module.
Your script will need to re-create an exact copy of a GUI from the supplied image at the bottom of this page.
"""
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import os


class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(500,200))
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')

    

        #Browse Buttons
        
        self.btnBrowOne = Button(self.master, text="Browse Source", width=14, height=1,command=self.browSource)
        self.btnBrowOne.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowOne = Button(self.master, text="Browse Destination", width=14, height=1,command=self.browDestination)
        self.btnBrowOne.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        #Folder destination/Entry fields
        
        self.txtSource = Entry(self.master,text='', font=("Helvetica",16), fg='black', bg='white')
        self.txtSource.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)

        self.txtDestination = Entry(self.master,text='', font=("Helvetica",16), fg='black', bg='white')
        self.txtDestination.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)


        #Operation buttons, Check and Close
        
        self.btnCheck = Button(self.master, text="Check for files", width=12, height=2,command=self.Check)
        self.btnCheck.grid(row=2, column=0, padx=(30,0), pady=(20,0))

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2,command=self.Close)
        self.btnClose.grid(row=2, column=2, padx=(0,0), pady=(0,0),sticky=SE)





    def Close(self):
        self.master.destroy()
   
    def browSource(self):
        self.varFolder=tk.filedialog.askdirectory()
        self.txtSource.insert(0,self.varFolder)
        
       

    def browDestination(self):
        self.varDestFold=tk.filedialog.askdirectory()
        self.txtDestination.insert(0,self.varDestFold)
        
#Once we can get the folder to load then we'll worry about printing it in screen instead of console
    def Check(self):
        path=self.varSource.get()


        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                print(filename)
                paths=os.path.join(fPath, filename)
                print(os.path.getmtime(paths))
                continue
            else:
                continue

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

