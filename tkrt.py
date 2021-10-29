import time
import datetime
import tkinter as tk
from tkinter import *

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.timevar = tk.StringVar()  # Added.

        self.frames = {}
        for F in (MainPage, Page1, Help):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, columnspan=12,sticky="nsew")
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)
            frame.grid_columnconfigure(2, weight=1)
            frame.grid_columnconfigure(3, weight=1)
            frame.grid_columnconfigure(4, weight=1)
            frame.grid_columnconfigure(5, weight=1)
            frame.grid_columnconfigure(6, weight=1)
            frame.grid_columnconfigure(7, weight=1)
            frame.grid_columnconfigure(8, weight=1)
            frame.grid_columnconfigure(9, weight=1)
            frame.grid_columnconfigure(10, weight=1)
            frame.grid_columnconfigure(11, weight=1)

        # Synchronize with the computer's clock.
        snooze = (1000000 - datetime.datetime.now().microsecond) / 1000000.
        if snooze > 0:
            time.sleep(snooze)  # Sleep until next whole second.
        self.clock()  # Starts string variable update process.

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # Additional method added.
    def clock(self):
        self.timevar.set(datetime.datetime.now().strftime("Time: %H:%M:%S"))
        self.after(1000, self.clock)  # Update every second (1000 millsecs)


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # line 0
        label00 = tk.Label(self, text='00', height=2)
        label00.configure(relief='raised')
        label00.grid(row=0, column=0, sticky='nsew', columnspan=12)
        # line 1
        label10 = tk.Label(self, text='10')
        label10.configure(relief='raised')
        label10.grid(row=1, column=0, sticky='nsew')
        label11 = tk.Label(self, text='LOGO')
        label11.configure(relief='raised')
        label11.grid(row=1, column=1, sticky='nsew', columnspan=4, rowspan=2)
        label12 = tk.Label(self, text='12')
        label12.configure(relief='raised')
        label12.grid(row=1, column=5, sticky='nsew')
        label13 = tk.Label(self, text='TITLE')
        label13.configure(relief='raised')
        label13.grid(row=1, column=6, sticky='nsew', columnspan=5)
        label14 = tk.Label(self, text='14')
        label14.configure(relief='raised')
        label14.grid(row=1, column=11, sticky='nsew')
        # line 2
        label20 = tk.Label(self, text='20')
        label20.configure(relief='raised')
        label20.grid(row=2, column=0, sticky='nsew')
        label21 = tk.Label(self, text='21')
        label21.configure(relief='raised')
        label21.grid(row=2, column=5, sticky='nsew')
        label22 = tk.Label(self, text='Desc')
        label22.configure(relief='raised')
        label22.grid(row=2, column=6, sticky='nsew', columnspan=5)
        label23 = tk.Label(self, text='23')
        label23.configure(relief='raised')
        label23.grid(row=2, column=11, sticky='nsew')
        # line 3
        label30 = tk.Label(self, text='30', height=2)
        label30.configure(relief='raised')
        label30.grid(row=3, column=0, sticky='nsew', columnspan=12)
        #line 4
        label40 = tk.Label(self, text='40', width=10)
        label40.configure(relief='raised')
        label40.grid(row=4, column=0, sticky='nsew')
        label41 = tk.Label(self, text='STATUS', font=("Helvetica", 16), justify='center', fg="blue")
        label41.configure(relief='raised')
        label41.grid(row=4, column=1, columnspan=10)
        label42 = tk.Label(self, text='42', width=10)
        label42.configure(relief='raised')
        label42.grid(row=4, column=11, sticky='nsew')
        #line 5
        label50 = tk.Label(self, text='50', height=2)
        label50.configure(relief='raised')
        label50.grid(row=5, column=0, columnspan=12, sticky="nsew")
        #line 6
        label60 = tk.Label(self, text='60', height=2)
        label60.configure(relief='raised')
        label60.grid(row=6, column=0, sticky='nsew')
        buttonauto = tk.Button(self, text="PAGE1", font=("Helvetica", 16), justify='center', width=40, height=5,
                              command=lambda: controller.show_frame("Page1"))
        buttonauto.grid(row=6, column=1, columnspan=4)
        label61 = tk.Label(self, text='61', height=2)
        label61.configure(relief='raised')
        label61.grid(row=6, column=5, sticky='nsew')
        label62 = tk.Label(self, text='62', height=2)
        label62.configure(relief='raised')
        label62.grid(row=6, column=6, sticky='nsew')
        buttoncam = tk.Button(self, text="HELP",font=("Helvetica", 16), justify='center', width=40, height=5,
                              command=lambda: controller.show_frame("Help"))
        buttoncam.grid(row=6 , column=7, columnspan=4)
        label63 = tk.Label(self, text='63', height=2)
        label63.configure(relief='raised')
        label63.grid(row=6, column=11, sticky='nsew')
        # line 7
        label70 = tk.Label(self, text='70', height=2)
        label70.configure(relief='raised')
        label70.grid(row=7, column=0, sticky='nsew', columnspan=12)

        #line 13
        label13 = tk.Label(self, text='', height=2)
        label13.configure(relief='raised')
        label13.grid(row=13, column=0, columnspan=12, sticky="nsew")
        #line 14
        label14 = tk.Label(self, text='', width=10)
        label14.grid(row=14, column=0, sticky='w')
        buttonhlp = tk.Button(self, text="Help", width=20, height = 3,
                              command=lambda: controller.show_frame("Help"))
        buttonhlp.grid(row=14, column=1, columnspan=4)
        label14 = tk.Label(self, text='')
        label14.grid(row=14, column=5, columnspan=2)
        buttonquit = tk.Button(self, text="Quit", width=20, height = 3, command=close_window)
        buttonquit.grid(row=14, column=7, columnspan=4)
        label14 = tk.Label(self, text='', width=10)
        label14.grid(row=14, column=11, sticky='e')
        #line 15
        label15 = tk.Label(self, text='', height=5)
        label15.grid(row=15, column=0, columnspan=12, sticky="nsew")


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #line 0
#        label00 = tk.Label(self, text='PAGE1', height=2)
        label00 = tk.Label(self, textvariable=controller.timevar, height=2)
        label00.configure(relief='raised')
        label00.grid(row=13, column=0, columnspan=12, sticky="nsew")
        #line 1
        label10 = tk.Label(self, text='', width=10)
        label10.grid(row=14, column=0, sticky='w')
        buttonback = tk.Button(self, text="Back", width=20, height = 3,
                              command=lambda: controller.show_frame("MainPage"))
        buttonback.grid(row=14, column=1, columnspan=4)
        label10= tk.Label(self, text='')
        label10.grid(row=14, column=5, columnspan=2)
        buttonquit = tk.Button(self, text="Quit", width=20, height = 3, command=close_window)
        buttonquit.grid(row=14, column=7, columnspan=4)
        label10 = tk.Label(self, text='', width=10)
        label10.grid(row=14, column=11, sticky='e')
        #line 2
        label20 = tk.Label(self, text='', height=5)
        label20.grid(row=15, column=0, columnspan=12, sticky="nsew")

class Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #line 0
        label00 = tk.Label(self, text='HELP', height=2)
        label00.configure(relief='raised')
        label00.grid(row=13, column=0, columnspan=12, sticky="nsew")
        #line 1
        label10 = tk.Label(self, text='', width=10)
        label10.grid(row=14, column=0, sticky='w')
        buttonback = tk.Button(self, text="Back", width=20, height = 3,
                              command=lambda: controller.show_frame("MainPage"))
        buttonback.grid(row=14, column=1, columnspan=4)
        label10= tk.Label(self, text='')
        label10.grid(row=14, column=5, columnspan=2)
        buttonquit = tk.Button(self, text="Quit", width=20, height = 3, command=close_window)
        buttonquit.grid(row=14, column=7, columnspan=4)
        label10 = tk.Label(self, text='', width=10)
        label10.grid(row=14, column=11, sticky='e')
        #line 2
        label20 = tk.Label(self, text='', height=5)
        label20.grid(row=15, column=0, columnspan=12, sticky="nsew")


def close_window ():
    app.destroy()


if __name__ == "__main__":
    app = MainApp()

    app.overrideredirect(True)
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.focus_set()  # <-- move focus to this widget


    app.mainloop()