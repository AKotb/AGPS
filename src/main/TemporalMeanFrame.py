import os
import tkFileDialog
import Tkinter as tk
import gzip

import xlsxwriter


class TemporalMeanFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Temporal Mean Calculation")
        self.pack(fill=tk.BOTH, expand=1)

        inputgracedirlbl = tk.Label(self.master, text="Raw Data Directory")
        inputgracedirlbl.place(x=20, y=50)

        self.inputgracedirtxtfield = tk.Text(self.master, height=1, width=50)
        self.inputgracedirtxtfield.place(x=130, y=50)

        inputgracedirbtn = tk.Button(self.master, text="Browse", command=self.selectgracerawdatadir)
        inputgracedirbtn.place(x=540, y=47)

        self.startcalculatingtemporalmeanbtn = tk.Button(self.master, text="Calculate Temporal Mean",
                                                         command=self.calculatetemporalmean)
        self.startcalculatingtemporalmeanbtn.place(x=450, y=200)
        self.cancelbtn = tk.Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=400, y=200)

        self.opentemporalmeanbtn = tk.Button(self.master, text="Open Temporal Mean", command=self.opentemporalmean)
        self.opentemporalmeanbtn.place(x=50, y=200)
        self.opentemporalmeanbtn.config(state="disabled")

    def exit(self):
        self.master.destroy()

    def selectgracerawdatadir(self):
        self.inputfilespath = tkFileDialog.askdirectory(initialdir="/", title="Select GRACE Raw Data Directory")
        self.files = os.listdir(self.inputfilespath)
        nooffiles = "No of Files= " + str(len(self.files))
        self.nooffileslbl = tk.Label(self.master, text=nooffiles)
        self.nooffileslbl.place(x=20, y=100)

    def calculatetemporalmean(self):
        self.cancelbtn.config(state="disabled")
        self.startcalculatingtemporalmeanbtn.config(state="disabled")
        workbook = xlsxwriter.Workbook(self.inputfilespath + '/' + 'GRACE Raw Data.xlsx')
        worksheet = workbook.add_worksheet()
        # Header
        #worksheet.write(0, 0, 'Coefficient')
        #worksheet.write(0, 1, 'Degree')
        worksheet.write(0, 2, 'Order')
        for x in self.files:
            if ".gz" in x:
                try:
                    filename = x.split('.')[0]  # File Name without extension
                    with gzip.open(self.inputfilespath+'/'+x, 'rb') as f:
                        file_content = f.read()
                    o = open(self.inputfilespath+'/'+filename+'.txt', 'w')
                    o.write(file_content)
                    o.close()
                except Exception as e:
                    print(e)
                    print "Could not read " + x
                    continue
            else:
                print("File " + x + " is not a .gz file")
                continue
        self.opentemporalmeanbtn.config(state="active")
        self.cancelbtn.config(state="active")

    def opentemporalmean(self):
        os.chdir(self.inputfilespath)
        os.system('start excel.exe "%s\\MonthIndex.xlsx"' % (self.inputfilespath,))
