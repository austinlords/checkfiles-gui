from tkinter import *
from tkinter import messagebox
import os


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(475,180)

        center_window(self,500,200)
        self.master.title('Check files')
        self.master.configure(bg='#eee')
        self.master.protocol('WM_DELETE_WINDOW', lambda: ask_quit(self))
        
        load_gui(self)

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def load_gui(self):
    # Browse empty fields
    self.txt_browse1 = Entry(self.master,text='',width=52)
    self.txt_browse1.grid(row=0,column=1,padx=(30,0),pady=(30,0),sticky=NE)
    self.txt_browse2 = Entry(self.master,text='', width=52)
    self.txt_browse2.grid(row=1,column=1,padx=(30,0),pady=(10,0),sticky=NE)

    # Buttons
    self.btn_browse1 = Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(30,10),sticky=NW)
    self.btn_browse2 = Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(10,10),sticky=NW)

    self.btn_checkfiles = Button(self.master,width=12,height=2,text='Check \
for files...')
    self.btn_checkfiles.grid(row=2,column=0,padx=(20,0),pady=(10,0),sticky=NW)
    self.btn_close = Button(self.master,width=12,height=2,text='Close \
Program', command=lambda: ask_quit(self))
    self.btn_close.grid(row=2,column=1,padx=(30,0),pady=(10,0),sticky=NE)


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
