from tkinter import *

import checkfiles_func
import checkfiles_main

def load_gui(self):
    # Browse empty fields
    self.txt_browse1 = Entry(self.master,text='',width=52)
    self.txt_browse1.grid(row=0,column=1,padx=(30,0),pady=(30,0),sticky=NE)
    self.txt_browse2 = Entry(self.master,text='', width=52)
    self.txt_browse2.grid(row=1,column=1,padx=(30,0),pady=(10,0),sticky=NE)

    # Buttons
    self.btn_browse1 = Button(self.master,width=12,height=1,text='Browse...',
                              command=lambda:checkfiles_func.browse1(self))
    self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(30,10),sticky=NW)
    self.btn_browse2 = Button(self.master,width=12,height=1,text='Browse...',
                              command=lambda:checkfiles_func.browse2(self))
    self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(10,10),sticky=NW)

    # 'Check Files' button commented out, no functionality yet
    '''
    self.btn_checkfiles = Button(self.master,width=12,height=2,text='Check \
for files...')
    self.btn_checkfiles.grid(row=2,column=0,padx=(20,0),pady=(10,0),sticky=NW)
    '''

    
    self.btn_close = Button(self.master,width=12,height=2,text='Close \
Program', command=lambda: checkfiles_func.ask_quit(self))
    self.btn_close.grid(row=2,column=1,padx=(30,0),pady=(10,0),sticky=NE)


if __name__ == '__main__':
    print('Please run this program from the checkfiles_main.py file')
