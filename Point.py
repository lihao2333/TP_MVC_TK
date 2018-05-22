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
        self.center_real = (1/(1 + self.real), 0)
        self.radius_real = 1/(1 + self.real)
        self.center_imag = (1, 1/self.imag)
        self.radius_imag = (1/abs(self.imag))
if __name__ == "__main__":
    point = Point(x=0.5, y=0.5)
    print(point.x,point.y)
    print(point.real,point.imag)


