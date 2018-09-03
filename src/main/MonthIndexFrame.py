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
        inputgracedirbtn.place(x=550, y=50)

        self.startgeneratingmonthindexbtn = tk.Button(self.master, text="Generate Month Index", command=self.generatemonthindex)
        self.startgeneratingmonthindexbtn.place(x=450, y=200)
        self.cancelbtn = tk.Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=400, y=200)

    def exit(self):
        self.master.destroy()

    def selectgracerawdatadir(self):
        inputfilespath = tkFileDialog.askdirectory(initialdir="/", title="Select GRACE Raw Data Directory")
        print ("GRACE Raw Data Directory: " + inputfilespath);

        self.nooffileslbl = tk.Label(self.master, text='Status ...')
        self.nooffileslbl.place(x=20, y=100)

        files = os.listdir(inputfilespath)
        index = 0
        for x in files:
            if ".gz" in x:
                index = index + 1
                print ("%s] %s" % (index,x))
                try:

                    '''print "Opening " + x
                    f = gzip.GzipFile(x, "r")
                    print "Reading " + x
                    data = f.readlines()[7:]  # read from the line no 7.. you should later add the coeff. (0,0) values
                    for entry in data:
                        tmp = entry.split(' ')
                        m = []
                        for n in tmp:
                            if n != '':
                                m.append(n)
                        if str(m[1]) + "," + str(m[2]) in output:
                            cur = output[str(m[0]) + "," + str(m[1]) + "," + str(m[2])]
                            output[str(m[0]) + "," + str(m[1]) + "," + str(m[2])] = [cur[0] + float(m[3]),
                                                                                     cur[1] + float(m[4]),
                                                                                     cur[2] + 1]
                        else:
                            output[str(m[0]) + "," + str(m[1]) + "," + str(m[2])] = [float(m[3]),
                                                                                     float(m[4]),
                                                                                     1]

                    print "Closing " + x
                    f.close()'''
                except:
                    print "Could not open " + x
                    continue


    def generatemonthindex(self):

        self.cancelbtn.place_forget()
        self.startgeneratingmonthindexbtn.place_forget()