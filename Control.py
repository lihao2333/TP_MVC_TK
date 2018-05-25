import base
from Model import Model
from View import View
from tkinter import Tk, Entry, Button, Label
from numpy import arange
from math import cos, acos
import matplotlib.lines as lines
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Control(object):
    def __init__(self):
        self.model = Model()
        self.view = View(self.model.figure)
        self.view.redraw()
        self.bind()
        self.view.root.mainloop()
    def bind(self):
        self.view.btn_back.config(command=self.fun_back)
        self.view.btn_next.config(command=self.fun_next)
        self.view.zl_r.config(command=self.update_zl_r)
        self.view.zl_i.config(command=self.update_zl_i)

    def fun_next(self):
        self.model.state +=1
        self.redraw()
    def fun_back(self):
        self.model.state -=1
        self.redraw()
    def update_zl_r(self,value):
        self.model.zl_r = float(value)
        print(value)
        self.redraw()
    def update_zl_i(self,value):
        self.model.zl_i = float(value)
        print(value)
        self.redraw()
    def redraw(self):
        self.model.redraw()
        self.view.redraw()

if __name__ == "__main__":
    control = Control()
    pass
