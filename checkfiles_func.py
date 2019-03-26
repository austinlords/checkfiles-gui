from tkinter import *
from tkinter import messagebox, filedialog
import os

import checkfiles_gui
import checkfiles_main


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

def browse1(self):
    abspath = filedialog.askdirectory()
    print(abspath)
    paste_path1(self, abspath)

def paste_path1(self, path):
    self.txt_browse1.delete(0,END)
    self.txt_browse1.insert(0, path)

def browse2(self):
    abspath = filedialog.askdirectory()
    print(abspath)
    paste_path2(self, abspath)

def paste_path2(self, path):
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(0, path)
    

if __name__ == '__main__':
    print('Please run this program from the checkfiles_main.py file')

