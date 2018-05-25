from sympy.geometry import Circle
from sympy.geometry import Point as _Point

class Point(object):
    def __init__(self, **kwargs):
        if 'x' in kwargs.keys():
            self.x, self.y = map(lambda key:kwargs[key], ['x','y'])
            self.xy2ri()
        else :
            self.real, self.imag = map(lambda key:kwargs[key], ['real','imag'])
            self.ri2xy()
        self.cal_circle()
    def xy2ri(self):
        x, y = self.x, self.y
        denominator = (1-x)**2 + y**2
        self.real = (1 - x**2 - y**2)/denominator
        self.imag = 2*y/denominator
    def ri2xy(self):
        r, i = self.real, self.imag
        denominator = (1+r)**2 + i**2
        self.x = (r**2 + i**2 -1)/denominator
        self.y = 2*i/denominator
    def cal_circle(self):
        self.center_real = (self.real/(1 + self.real), 0)
        self.radius_real = 1/(1 + self.real)
        if self.imag == 0:
            self.center_imag = (1, 100000)
            self.radius_imag= (100000)
        else :
            self.center_imag = (1, 1/self.imag)
            self.radius_imag = (1/abs(self.imag))
    def symmetry(self):
        P = Point(x = -self.x, y = -self.y)
        return P
    def rotation_90(self):
        P = Point(x = -self.y, y = self.x)
        return P
    def intersection_wi_assi(self):
        circ_assi = Circle(_Point(0,-0.5),0.5)
        circ_self = Circle( _Point(\
                self.center_real[0],\
                self.center_real[1]), \
                self.radius_real)
        point_intersection =  circ_self.intersection(circ_assi)[0]
        return Point(x = point_intersection[0], y = point_intersection[1])

if __name__ == "__main__":
    #point = Point(x=0.5, y=0.5)
    point = Point(real=2, imag=1)
#    circ_yl = Circle(Point(*cal_center(r)),cal_radius(r))
    print(point.x,point.y)
    print(point.real,point.imag)


