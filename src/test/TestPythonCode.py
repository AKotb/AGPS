from Tkinter import *

OPTIONS = [
    "0 km",
    "250 km",
    "500 km",
    "750 km",
    "990 km"
]

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0])

w = apply(OptionMenu, (master, variable) + tuple(OPTIONS))
w.pack()

mainloop()