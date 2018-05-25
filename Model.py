import base
import Point
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
                self.do_zl,
                self.do_yl, 
                self.do_a, 
                self.do_b, 
                self.do_o
                ]
        self.total_state = len(self.todo)
        self.redraw()
        self.cal = Tools.Calculator()

    def do_predraw(self):
        self.draw_axis()
        self.draw_circle((0.5,0), 0.5, edgecolor='black')
        self.draw_circle((0, -0.5), 0.5, edgecolor='black')
    def do_zl(self):
        self.P_zl = Point.Point(real=self.zl_r, imag=self.zl_i)
        print("xxxx")
        self.draw_point_(self.P_zl, "zl")
        self.draw_smith(self.P_zl)
    def do_yl(self):
        self.P_yl = self.P_zl.symmetry()
        self.draw_point_(self.P_yl, "yl")
        self.draw_line_(self.P_zl, self.P_yl)
        self.draw_smith(self.P_yl)
    def do_a(self):
        self.P_a = self.P_yl.intersection_wi_assi()
        self.draw_point_(self.P_a,"A")
        self.draw_arc_(self.P_yl, self.P_a, self.P_yl.center_real)
    def do_b(self):
        self.P_b = self.P_a.rotation_90()
        self.draw_point_(self.P_b,"B")
        self.draw_arc_(self.P_a, self.P_b, (0,0))
    def do_o(self):
        self.P_o = Point.Point(x=0, y=0)
        self.draw_point_(self.P_o,"O")
        self.draw_arc_(self.P_b, self.P_o, self.P_b.center_real)

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
    def draw_point_(self,P, s):
        self.draw_point((P.x, P.y),s)
    def draw_line(self,start,end):
        line = lines.Line2D(*zip(start,end),linestyle="--",color='green',alpha = 0.5)
        self.axes.add_line(line) 
    def draw_line_(self, start, end):
        line = lines.Line2D((start.x, end.x),(start.y, end.y),linestyle="--",color='green',alpha = 0.5)
        self.axes.add_line(line) 
    
    def draw_circle(self, xy, redius,edgecolor='green'):
        self.axes.add_patch(pCircle(xy=xy,radius= redius,alpha=0.5,linestyle='-.',edgecolor=edgecolor,facecolor='none'))
    def draw_smith(self,P):
        self.draw_circle(P.center_real, P.radius_real, 'blue')
        self.draw_circle(P.center_imag, P.radius_imag, 'pink')
        pass
    def draw_reflect(self, P):
        _ = sqrt(P.x**2+P.y**2)
        self.draw_circle((0,0), _, 'yellow')
        pass

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
    def draw_arc_(self, P1, P2,center,  clkwise=False):
        self.draw_arc((P1.x,P1.y), (P2.x, P2.y),center, clkwise )
        pass
