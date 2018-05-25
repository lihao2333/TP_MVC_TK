import base
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class View(base.BView):
    def __init__(self, figure):
        base.BView.__init__(self, figure)
        Label(self.root,text='Zl_Real').grid(row=1,column=0)
        Label(self.root,text='Zl_Image').grid(row=1,column=1)
        self.zl_r = Scale(self.root, from_=0.0, to=5.0 , resolution=0.1,orient=HORIZONTAL)  
        self.zl_i = Scale(self.root, from_=-5.0, to=5.0, resolution=0.1,orient=HORIZONTAL)  
        self.zl_r.set(2)
        self.zl_i.set(20)
        self.zl_r.grid(row = 1, column=0)
        self.zl_i.grid(row = 1, column=1)

