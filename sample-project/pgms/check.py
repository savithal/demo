'''class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self, other):
        return self.real+other.real, self.img+other.img

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def display(self):
        print(self.real,"+",self.img,"i")


c1=Complex(4,2)
c2=Complex(3,4)
c3=c1+c2
print((c3))'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        print (self.x,"+",self.y,"i")
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1=Point(4,2)
p2=Point(2,3)
p3=p1+p2
print(p3)


