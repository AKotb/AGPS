import os
import tkFileDialog
import Tkinter as tk


class MonthIndexFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Month Index")
        self.pack(fill=tk.BOTH, expand=1)

        inputgracedirlbl = tk.Label(self.master, text="Raw Data Directory")
        inputgracedirlbl.place(x=20, y=50)
        self.inputgracedirtxtfield = tk.Text(self.master, height=1, width=50)
        self.inputgracedirtxtfield.place(x=130, y=50)
        inputgracedirbtn = tk.Button(self.master, text="Browse", command=self.selectgracerawdatadir)
        inputgracedirbtn.place(x=520, y=50)

        self.startgeneratingmonthindexbtn = tk.Button(self.master, text="Generate Month Index", command=self.generatemonthindex)
        self.startgeneratingmonthindexbtn.place(x=480, y=200)
        self.cancelbtn = tk.Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=520, y=200)

    def exit(self):
        self.master.destroy()

    def selectgracerawdatadir(self):
        inputfilespath = tkFileDialog.askdirectory(initialdir="/", title="Select GRACE Raw Data Directory")
        print ("GRACE Raw Data Directory: " + inputfilespath);
        self.nooffileslbl = tk.Label(self.master, text="No of Files: %s File" % inputfilespath)
        self.nooffileslbl.place(x=20, y=100)

    def generatemonthindex(self):
        self.cancelbtn.place_forget()
        self.startgeneratingmonthindexbtn.place_forget()