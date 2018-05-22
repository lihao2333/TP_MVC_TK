import math
class Calculator(object):
    def center(self,r):#r:rediaus
        return (r/(1+r),0)
    def radius(self,r):#r:real
        return 1/(1+r)
    def mod(self,x,y):
        return math.sqrt(x**2+y**2)
    def ri2xy(self,r,i):
        x = (r**2 + i**2 -1)/float((1+r)**2 + i**2)
        y = (2*i)/float((1+r)**2 + i**2)
        return x,y
