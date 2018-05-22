#!/usr/bin/env python3
#-*-coding:utf-8  -*-
import numpy as np  
import cmath
from tkinter import *  
import matplotlib  
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
from matplotlib.figure import Figure  
from sympy.geometry import Circle,Point
from matplotlib.patches import Circle as pCircle,Arc
from time import sleep
import math

import matplotlib.lines as lines
  
def drawPic():  
    z0 = complex(value_z0.get())
    zl = complex(value_zl.get())
    z=zl/z0
    y=1/z
    d = float(value_d.get())
    delay_time = float(value_time.get())

   #清空图像，以使得前后两次绘制的图像不会重叠  
    drawPic.f.clf()  
    drawPic.a=drawPic.f.add_subplot(111)  
             

    #坐标系
    draw_axis(drawPic.a)

    #Cal:zl Draw:zl,yl
    r,i = z.real, z.imag
    xz,yz = cal_xy(r,i)
    draw_point(drawPic.a,(xz,yz),"Z_L")
    drawPic.canvas.draw()   
    sleep(delay_time)
    r,i = y.real, y.imag
    x,y = cal_xy(r,i)
    draw_point(drawPic.a,(x,y),"Y_L")
    draw_line(drawPic.a,(xz,yz),(x,y))
    drawPic.canvas.draw()   
    sleep(delay_time)


    #Cal:yl的电导圆,辅助圆,左交点 Draw:yl->A
    draw_circle(drawPic.a,cal_center(r),cal_radius(r))
    draw_circle(drawPic.a,(0,-0.5),0.5)
    circ_assi = Circle(Point(0,-0.5),0.5)
    circ_yl = Circle(Point(*cal_center(r)),cal_radius(r))
    point_xx = circ_yl.intersection(circ_assi)[0]
    xa = point_xx.x
    ya = point_xx.y
    drawPic.a.annotate(s="A",xy=(xa,ya))
    drawPic.a.scatter([xa],[ya],s=20,color="red")
    ca = complex(xa,ya) - complex(*cal_center(r))
    c = complex(x,y) - complex(*cal_center(r))
    draw_arc(drawPic.a,(x,y),(xa,ya),cal_center(r))
    drawPic.canvas.draw()   
    sleep(delay_time)
    

    #Cal:B Draw:B,单位电导圆
    xb,yb = -ya,xa
    draw_point(drawPic.a,(xb,yb),"B")
    draw_circle(drawPic.a,(0.5,0),0.5)
    draw_circle(drawPic.a,(0,0),math.sqrt(xb**2+yb**2))
    draw_arc(drawPic.a,(xa,ya),(xb,yb),(0,0))
    drawPic.canvas.draw()   
    sleep(delay_time)

#    r = math.sqrt(xb**2+yb**2)
#    drawPic.a.add_patch(Arc((0,0),2*r,2*r,theta1=0,theta2=90))
    x0,y0 = 0,0
    draw_point(drawPic.a,(x0,y0),"O")
    draw_arc(drawPic.a,(xb,yb),(x0,y0),(0.5,0))
    drawPic.canvas.draw()   
    sleep(delay_time)


    #绘制这些随机点的散点图，颜色随机选取  
    drawPic.a.set_title('Double junction matcher')  
    drawPic.canvas.draw() 
def draw_axis(ax):
    line_x = lines.Line2D((-1,1),(0,0))
    line_y = lines.Line2D((0,0),(-1,1))
    ax.add_line(line_x) 
    ax.add_line(line_y) 
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
def draw_point(ax,xy,s):
    ax.annotate(s=s,xy=xy)
    ax.scatter(xy[0],xy[1],s=20,color="red")
def draw_circle(ax, xy, redius):
    ax.add_patch(pCircle(xy=xy,radius= redius,alpha=0.5,linestyle='-.',edgecolor='green',facecolor='none'))
def draw_arc(ax,start,end,center,clkwise=False):
    if clkwise:c1,c2=c2,c1 
    c1 = complex(*start)-complex(*center)
    c2 = complex(*end)-complex(*center)
    t1 = cmath.phase(c1)*180/math.pi
    t2 = cmath.phase(c2)*180/math.pi
    if (t2-t1)%360>180:t1,t2=t2,t1
    radius = abs(c1)
    arc = Arc(center,2*radius, 2*radius, theta1 = t1, theta2 = t2)
    ax.add_patch(arc)
def draw_line(ax,start,end):
    line = lines.Line2D(*zip(start,end),linestyle="--",color='green',alpha = 0.5)
    ax.add_line(line) 


def cal_center(r):
    return (r/(1+r),0)
def cal_radius(r):
    return 1/(1+r)
def cal_xy(r,i):
    x = (r**2 + i**2 -1)/float((1+r)**2 + i**2)
    y = (2*i)/float((1+r)**2 + i**2)
    return x,y

if __name__ == '__main__':      
      
    matplotlib.use('TkAgg')  
    root = Tk()    
    root.title("Double junction matcher")
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局  
    drawPic.f = Figure(figsize=(6.5,6.5), dpi=100)  
  
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)   
    drawPic.canvas.draw()   
    drawPic.canvas.get_tk_widget().grid(row=0,column=0, rowspan=3)      
      
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数  
    Label(root,text='Z0').grid(row=0,column=1)  
    value_z0=Entry(root)  
    value_z0.grid(row=0,column=2)  
    value_z0.insert(0,'50+0j')  

    Label(root,text='ZL').grid(row=1,column=1)  
    value_zl=Entry(root)  
    value_zl.grid(row=1,column=2)  
    value_zl.insert(0,'70+30j')  

    Label(root,text='d').grid(row=2,column=1)  
    value_d=Entry(root)  
    value_d.grid(row=2,column=2)  
    value_d.insert(0,'0.5')  

    Label(root,text='delay_time').grid(row=3,column=1)  
    value_time=Entry(root)  
    value_time.grid(row=3,column=2)  
    value_time.insert(0,'1')  

    Button(root,text='OK',command=drawPic).grid(row=4,column=1,columnspan=2)  
         
    #启动事件循环  
    root.mainloop() 
