import base


from sympy.geometry import Circle,Point
from matplotlib.patches import Circle as pCircle,Arc
import Tools
from tkinter import Tk, Entry, Button, Label
from numpy import arange
import cmath, math
import matplotlib.lines as lines
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Model(base.BModel):
    def __init__(self):
        base.BModel.__init__(self)
        ##content
        self.zl_r = 2 
        self.zl_i = 0 
        ##todo
        self.todo = [
                self.do_predraw,
                self.do_point_ZL,
                self.do_move_YL,
                self.do_circle_A, 
                self.do_circle_assistant, 
                self.do_move_A,
                self.do_circle_unit, 
                self.do_circle_B,
                self.do_move_B, 
                self.do_move_O
                ]
        self.total_state = len(self.todo)
        self.redraw()
        self.cal = Tools.Calculator()

    def do_predraw(self):
        self.zl = complex(self.zl_r, self.zl_i)
        self.figure.clf()
        self.axes = self.figure.add_subplot(111)
        self.draw_axis()
    def do_point_ZL(self):
        self.zl_x, self.zl_y = self.cal.ri2xy(self.zl_r, self.zl_i)
        self.draw_point((self.zl_x, self.zl_y), "Z_L")
        self.zl_radius = self.cal.radius(self.zl_r)
        self.zl_center=self.cal.center(self.zl_radius)
        self.draw_circle(self.zl_center, self.zl_radius)
        
    def do_move_YL(self):
        self.yl = 1/self.zl
        self.yl_r, self.yl_i = self.yl.real, self.yl.imag
        self.yl_x, self.yl_y = self.cal.ri2xy(self.yl_r, self.yl_i)
        self.draw_line((self.zl_x, self.zl_y) , (self.yl_x, self.yl_y))
        self.draw_point((self.yl_x, self.yl_y), "Y_L")
    def do_circle_A(self):
        self.A_center =  self.cal.center(self.yl_r)
        self.A_radius = self.cal.radius(self.yl_r)
        self.draw_circle(self.A_center, self.A_radius)
    def do_circle_assistant(self):
        self.assi_center =(0,-0.5)
        self.assi_radius = 0.5
        self.draw_circle(self.assi_center, self.assi_radius,'black')
    def do_move_A(self):
        assi_circle = Circle(Point(*self.assi_center), self.assi_radius)
        A_circle = Circle(Point(*self.A_center), self.A_radius)
        A_point = A_circle.intersection(assi_circle)[0]
        self.A_x = A_point.x
        self.A_y = A_point.y
        self.draw_point((self.A_x, self.A_y),"A")
        self.draw_arc((self.yl_x,self.yl_y),(self.A_x,self.A_y),self.cal.center(self.yl_r))
    def do_circle_unit(self):
        self.A_radius = self.cal.mod(self.A_x, self.A_y)
        self.draw_circle((0,0),self.A_radius)
    def do_circle_B(self):
        self.B_radius = 0.5
        self.B_center = (0.5,0)
        self.draw_circle(self.B_center, self.B_radius,'black')
    def do_move_B(self):
        self.B_x, self.B_y = -self.A_y, self.A_x
        self.draw_arc((self.A_x, self.A_y), (self.B_x, self.B_y), (0,0))
        self.draw_point((self.B_x, self.B_y), "B")
    def do_move_O(self):
        self.draw_arc((self.B_x, self.B_y), (0,0), self.B_center)
        self.draw_point((0,0), "O")

    def draw_axis(self):
        line_x = lines.Line2D((-1,1),(0,0))
        line_y = lines.Line2D((0,0),(-1,1))
        self.axes.add_line(line_x) 
        self.axes.add_line(line_y) 
        self.axes.set_xlim(-1,1)
        self.axes.set_ylim(-1,1)


    def draw_point(self,xy,s):
        self.axes.annotate(s=s,xy=xy)
        self.axes.scatter(xy[0],xy[1],s=20,color="red")
    def draw_circle(self, xy, redius,edgecolor='green'):
        self.axes.add_patch(pCircle(xy=xy,radius= redius,alpha=0.5,linestyle='-.',edgecolor=edgecolor,facecolor='none'))
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
    
    
