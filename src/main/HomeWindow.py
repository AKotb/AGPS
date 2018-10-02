import Tkinter as tk
import sys
import tkMessageBox

from src.main.MonthIndexFrame import MonthIndexFrame
from src.main.TemporalMeanFrame import TemporalMeanFrame


class HomeWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("AGPS Home")
        self.pack(fill=tk.BOTH, expand=1)

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        processingmenu = tk.Menu(menubar, tearoff=0)
        processingmenu.add_command(label="Month Index", command=self.monthindex)
        processingmenu.add_command(label="Temporal Mean", command=self.temporalmean)
        menubar.add_cascade(label="Processing", menu=processingmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

    def exit(self):
        exit()

    def open(self):
        print ("Open Menu Item Pressed!")

    def about(self):
        tkMessageBox.showinfo("AGPS",
                              "Automated GRACE Processing System."
                              "AGPS Version 0.1")

    def monthindex(self):
        root = tk.Tk()
        root.geometry("600x250")
        app = MonthIndexFrame(root)
        root.mainloop()

    def temporalmean(self):
        root = tk.Tk()
        root.geometry("600x250")
        app = TemporalMeanFrame(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x20+50+50")
    root.overrideredirect(0)
    root.config(bg="blue")
    app = HomeWindow(root)
    root.mainloop()

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook
