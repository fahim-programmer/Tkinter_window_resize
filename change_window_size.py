# Shell Scripts

import tkinter
import threading
import time

class main_gui:
    def __init__(self):
        window_size = '400x600'
        self.root = tkinter.Tk()
        self.root.geometry(window_size)
        self.root.title('Grows')

        self.custom_password = tkinter.Entry(self.root)
        self.custom_password.configure(exportselection='true')
        _text_ = ''''''
        self.custom_password.delete('0', 'end')
        self.custom_password.insert('0', _text_)
        self.custom_password.place(x=10, y=10, width=170, height=30)

        # ````````````````````````````````````````````````````````````````
        custom_pass_button = tkinter.Button(self.root)
        custom_pass_button["bg"] = "#363636"
        #ft = tkFont.Font(family='Ariel', size=10)
        #custom_pass_button["font"] = ft
        custom_pass_button["fg"] = "#ffffff"
        custom_pass_button["justify"] = "center"
        custom_pass_button["text"] = "Change Size of Window"
        custom_pass_button["relief"] = "flat"
        custom_pass_button.place(x=10, y=50, width=170, height=30)
        custom_pass_button["command"] = self.function
        self.root.mainloop()

    def button(*args, **kwargs):
        button = tkinter.Button(self.root)
        custom_pass_button["bg"] = "#363636"
        #ft = tkFont.Font(family='Ariel', size=10)
        #custom_pass_button["font"] = ft
        custom_pass_button["fg"] = "#ffffff"
        custom_pass_button["justify"] = "center"
        custom_pass_button["text"] = "sample button"
        custom_pass_button["relief"] = "flat"
        custom_pass_button.place(x=10, y=50, width=170, height=30)
        custom_pass_button["command"] = self.function
        

    
    def threadmanager(self):
        thread1 = threading.Thread(target=self.function)
        thread1.start()

    def function(self):
        try:
            val = (self.custom_password.get())
            print(val)
            window_size = f"{str(val)}"
            self.root.geometry(window_size)
        except:
            print("Bad Command")

if __name__ == "__main__":
    main_gui()