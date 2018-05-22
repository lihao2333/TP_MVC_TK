import base
from tkinter import Tk, Entry, Button, Label
from numpy import arange
from math import cos, acos
import matplotlib.lines as lines
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class View(base.BView):
    def __init__(self, figure):
        base.BView.__init__(self, figure)
        Label(self.root,text='Z0').grid(row=1,column=0)
        Label(self.root,text='ZL').grid(row=1,column=1)
        self.ipt_A = Entry(self.root)
        self.ipt_A.grid(row=2, column=0)
        self.ipt_B = Entry(self.root)
        self.ipt_B.grid(row=2, column=1)

class Model(base.BModel):
    def __init__(self):
        base.BModel.__init__(self)
        self.todraw = [
                self.draw_axis,
                self.draw_curve
                ]
        self.redraw()
    def draw_axis(self):
        line_x = lines.Line2D((-1,-1),(0,0))
        line_y = lines.Line2D((0,0),(-1,1))
        self.axes.add_line(line_x) 
        self.axes.add_line(line_y) 
        self.axes.set_xlim(-1,1)
        self.axes.set_ylim(-0,1)

    def draw_point(self,xy,s):
        self.axes.annotate(s=s,xy=xy)
        self.axes.scatter(xy[0],xy[1],s=20,color="red")
    def draw_circle(self, xy, redius):
        self.axes.add_patch(pCircle(xy=xy,radius= redius,alpha=0.5,linestyle='-.',edgecolor='green',facecolor='none'))
    def draw_arc(self,start,end,center,clkwise=False):
        if clkwise:c1,c2=c2,c1 
        c1 = complex(*start)-complex(*center)
        c2 = complex(*end)-complex(*center)
        t1 = cmath.phase(c1)*180/math.pi
        t2 = cmath.phase(c2)*180/math.pi
        if (t2-t1)%360>180:t1,t2=t2,t1
        radius = abs(c1)
        arc = Arc(center,2*radius, 2*radius, theta1 = t1, theta2 = t2)
        self.axes.add_patch(arc)
    def draw_line(self,start,end):
        line = lines.Line2D(*zip(start,end),linestyle="--",color='green',alpha = 0.5)
        self.axes.add_line(line) 
    
    
    def cal_center(self,r):
        return (r/(1+r),0)
    def cal_radius(self,r):
        return 1/(1+r)
    def cal_xy(self,r,i):
        x = (r**2 + i**2 -1)/float((1+r)**2 + i**2)
        y = (2*i)/float((1+r)**2 + i**2)
        return x,y
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

    def fun_next(self):
        self.model.state +=1
        self.model.redraw()
        self.view.redraw()
    def fun_back(self):
        self.model.state -=1
        self.model.redraw()
        self.view.redraw()
if __name__ == "__main__":
    control = Control()
    pass
