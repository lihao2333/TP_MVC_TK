from tkinter import Tk, Entry, Button, Label
from numpy import arange
from math import cos, acos
import matplotlib.lines as lines
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class BView(object):
    def __init__(self, figure):
        self.root = Tk()
        self.canvas = FigureCanvasTkAgg(figure, master = self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=9)
        self.btn_back = Button(self.root, text="Back")
        self.btn_back.grid(row=1, column=4)
        self.btn_ok = Button(self.root, text="OK")
        self.btn_ok.grid(row=1,column=5)
        self.btn_next = Button(self.root, text="Next")
        self.btn_next.grid(row=1, column=6)
    def redraw(self):
        self.canvas.draw()
class BModel(object):
    def __init__(self):
        self.figure = Figure(figsize=(7.5,6.5), dpi=100)
        self.axes = self.figure.add_subplot(111)
        self.state = 0
        self.todo =[]
    def redraw(self):

        cnt_state = len(self.todo)
        if self.state==-1 :self.state+=1
        if self.state==len(self.todo): self.state-=1
        self.figure.clf()
        self.axes = self.figure.add_subplot(111)
        for No, do in enumerate(self.todo):
            do()
            if No == self.state: return




