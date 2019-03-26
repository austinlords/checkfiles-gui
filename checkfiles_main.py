from tkinter import *

import checkfiles_gui
import checkfiles_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(475,180)

        checkfiles_func.center_window(self,500,200)
        self.master.title('Check files')
        self.master.configure(bg='#eee')
        self.master.protocol('WM_DELETE_WINDOW', lambda:
                             checkfiles_func.ask_quit(self))
        
        checkfiles_gui.load_gui(self)



if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
