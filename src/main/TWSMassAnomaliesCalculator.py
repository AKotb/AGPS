import Tkinter as tk
import os
import tkFileDialog
from subprocess import Popen, PIPE


class TWSMassAnomaliesCalculator(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.filtersdir = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources")
        self.init_window()

    def init_window(self):
        self.master.title("TWS Mass Anomalies Calculator")
        self.pack(fill=tk.BOTH, expand=1)

        RADIUSOPTIONS = [
            "0 km",
            "250 km",
            "500 km",
            "750 km",
            "990 km"
        ]
        rvariable = tk.StringVar(self)
        rvariable.set(RADIUSOPTIONS[0])

        rw = tk.OptionMenu(self, rvariable, *RADIUSOPTIONS)
        rw.place(x=300, y=45)

        FILTEROPTIONS = [
            "Gaussian",
            "Destripping"
        ]
        fvariable = tk.StringVar(self)
        fvariable.set(FILTEROPTIONS[0])

        fw = tk.OptionMenu(self, fvariable, *FILTEROPTIONS)
        fw.place(x=200, y=45)

        # Gaussian Radius
        gausssianradiuslbl = tk.Label(self.master, text="Choose Filter ")
        gausssianradiuslbl.place(x=20, y=50)


        # Formatted Data Directory
        inputgracedirlbl = tk.Label(self.master, text="Formatted GRACE Data Directory")
        inputgracedirlbl.place(x=20, y=100)

        self.inputgracedirtxtfield = tk.Text(self.master, height=1, width=45)
        self.inputgracedirtxtfield.place(x=200, y=100)

        inputgracedirbtn = tk.Button(self.master, text="Browse", command=self.selectgraceformatteddatadir)
        inputgracedirbtn.place(x=540, y=97)

        # Months to process File
        monthstoprocesslbl = tk.Label(self.master, text="Months to Process File")
        monthstoprocesslbl.place(x=20, y=150)

        self.monthstoprocesstxtfield = tk.Text(self.master, height=1, width=45)
        self.monthstoprocesstxtfield.place(x=200, y=150)

        monthstoprocessbtn = tk.Button(self.master, text="Browse", command=self.selectmonthstoprocessfile)
        monthstoprocessbtn.place(x=540, y=147)

        # Love Number File
        # lovenumberslbl = tk.Label(self.master, text="Love Numbers File")
        # lovenumberslbl.place(x=20, y=200)
        #
        # self.lovenumberstxtfield = tk.Text(self.master, height=1, width=45)
        # self.lovenumberstxtfield.place(x=200, y=200)
        #
        # lovenumbersbtn = tk.Button(self.master, text="Browse", command=self.selectlovenumbersdir)
        # lovenumbersbtn.place(x=540, y=197)


        self.startcalculatingtwsmassanomaliesbtn = tk.Button(self.master, text="Start",
                                                         command=self.calculatetwsmassanomalies)
        self.startcalculatingtwsmassanomaliesbtn.place(x=450, y=250)
        self.cancelbtn = tk.Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=400, y=250)

    def exit(self):
        self.master.destroy()

    def selectgraceformatteddatadir(self):
        self.formatteddatapath = tkFileDialog.askdirectory(initialdir="/", title="Select GRACE formatted Data Directory")
        self.inputgracedirtxtfield.delete(1.0, tk.END)
        self.inputgracedirtxtfield.insert(tk.END, self.formatteddatapath)

    def selectmonthstoprocessfile(self):
        self.monthstoprocessfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select Months to Process File")
        self.monthstoprocesstxtfield.delete(1.0, tk.END)
        self.monthstoprocesstxtfield.insert(tk.END, self.monthstoprocessfilepath)
        self.headmonthtoprocess, self.tailmonthtoprocess = os.path.split(self.monthstoprocessfilepath)

    # def selectlovenumbersdir(self):
    #     self.lovenumberfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select Love Number File")
    #     self.lovenumberstxtfield.delete(1.0, tk.END)
    #     self.lovenumberstxtfield.insert(tk.END, self.lovenumberfilepath)
    #     self.headlovenumber, self.taillovenumber = os.path.split(self.lovenumberfilepath)

    def calculatetwsmassanomalies(self):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\TWS_Mass_Anomalies_Calculation.bat")
        #p = Popen([batfilepath, self.formatteddatapath, self.filtersdir, self.formatteddatapath, "Calculating_TWS_mass_NDS_250km.exe", self.headmonthtoprocess, self.formatteddatapath, self.tailmonthtoprocess,  self.headlovenumber, self.formatteddatapath, self.taillovenumber, "Calculating_TWS_mass_NDS_250km.exe"], stdout=PIPE, stderr=PIPE)
        p = Popen([batfilepath, self.formatteddatapath, self.filtersdir, self.formatteddatapath, "Calculating_TWS_mass_NDS_250km.exe", self.headmonthtoprocess, self.formatteddatapath, self.tailmonthtoprocess, "Calculating_TWS_mass_NDS_250km.exe"], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()