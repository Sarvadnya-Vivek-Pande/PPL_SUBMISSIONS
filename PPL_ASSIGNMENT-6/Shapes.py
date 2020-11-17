from math import*
import turtle
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(1)


class Shapes_2D(object):

    def __init__(self, first_dimension, second_dimension):
        self.first_dim = first_dimension
        self.second_dim = second_dimension
        print(f"2D Shape created with first dimension = {self.first_dim} and second dimension = {self.second_dim}")

    def __set__(self):
        print("Area and Perimeter Attributes declared")
        self.area = 0
        self.perimeter = 0

    def get_area(self):
        print(f"Area = {self.area}")

    def get_perimeter(self):
        print(f"Perimeter = {self.perimeter}")

    def draw(self):
        print("cannot draw a shape without knowing the shape")


class Regular_Polygon(Shapes_2D):
    def __init__(self, side_length, n):
        self.side_length=side_length
        self.no_of_sides=n
        print(f"Regular polygon created with Side length = {self.side_length} and Number of sides = {self.no_of_sides} ")

    def __set__(self):
        self.Exterior_angle=360/self.no_of_sides
        self.perimeter=self.side_length*self.no_of_sides
        self.area=0.25*(self.side_length**2)*self.no_of_sides/tan(pi/self.no_of_sides)
        print("Exterior angle, Area and Perimeter Attributes Declared")

    def get_exteriorangle(self):
        print(f"Exterior Angle = {self.Exterior_angle}")

    def draw(self):
        for i in range(self.no_of_sides):
            turtle.forward(self.side_length)
            turtle.left(self.Exterior_angle)


class Rectangle(Shapes_2D):

    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        print(f"Rectangle created with length = {self.length} and breadth = {self.breadth}")

    def __set__(self):
        print("Area and Perimeter Attributes declared")
        self.area = self.length * self.breadth
        self.perimeter = 2 * (self.length + self.breadth)

    def draw(self):
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.breadth)
            turtle.left(90)
        turtle.end_fill()


class Rhombus(Shapes_2D):
    def __init__(self, s_length, d1, d2):
        self.side_length=s_length
        self.d1=d1
        self.d2=d2
        print(f"Rhombus Created with side = {self.side_length} and diagonals {self.d1} and {self.d2}")
    def __set__(self):
        print("Area and perimeter attributes declared")
        self.perimeter=4*self.side_length
        self.area=0.5*self.d1*self.d2


class Ellipse(Shapes_2D):
    def __init__(self, a, b):
        self.a=a
        self.b=b
        print(f"Ellipse created with major axis = {self.a} and minor axis = {self.b}")
    def __set__(self):
        print("Area and Perimeter Attributes declared")
        self.area=pi*self.a*self.b
        self.perimeter=2*pi*sqrt((self.a*self.a+self.b*self.b)/2)


class Triangle(Shapes_2D):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        print(f"Triangle created with side lengths {self.s1}, {self.s2} and {self.s3}")
    def __set__(self):
        self.perimeter=self.s1+self.s2+self.s3
        self.area=sqrt((self.perimeter/2)*(self.perimeter/2-self.s1)*(self.perimeter/2-self.s2)*(self.perimeter/2-self.s3))
        print("Area and Perimeter attributes declared")


class Square(Rectangle, Rhombus, Regular_Polygon):
    def __init__(self, a):
        self.side_length=a
        print(f"Square created with side {self.side_length}")
    def __set__(self):
        print("Area and Perimeter attributes declared")
        self.area=self.side_length**2
        self.perimeter=4*self.side_length
    def draw(self):
        for i in range(4):
            turtle.forward(self.side_length)
            turtle.left(90)


class Circle(Ellipse):
    def __init__(self, r):
        self.a=self.b=r
        print(f"Circle created with radius = {self.a}")
    def draw(self):
        turtle.begin_fill()
        turtle.circle(self.a)
        turtle.end_fill()


class Octagon(Regular_Polygon):
    no_of_sides=8
    def __init__(self, s, n=8):
        self.side_length = s
        print(f"Octagon created Side length = {self.side_length}")


class Pentagon(Regular_Polygon):
    no_of_sides = 5
    def __init__(self, s, n=5):
        self.side_length = s
        print(f"Pentagon created Side length = {self.side_length}")


class Equilateral_Triangle(Regular_Polygon, Triangle):
    def __init__(self, side_length):
        self.side_length=side_length
        print(f"Equilateral Triangle created with side = {self.side_length}")
    def __set__(self):
        self.area=(sqrt(3)/4)*(self.side_length**2)
        self.perimeter=3*self.side_length
    def draw(self):
        self.no_of_sides=3
        self.Exterior_angle=120
        Regular_Polygon.draw(self)

# S1=Shapes_2D(30, 50)
# S1.__set__()
# S1.get_perimeter()
# S1.get_area()
# S1.draw()

# RG1=Regular_Polygon(30, 6)
# RG1.__set__()
# RG1.get_exteriorangle()
# RG1.get_perimeter()
# RG1.get_area()
# RG1.draw()


# R1=Rectangle(60, 80)
# R1.__set__()
# R1.get_perimeter()
# R1.get_area()
# R1.draw()

# O1=Octagon(48)
# O1.__set__()
# O1.get_exteriorangle()
# O1.get_perimeter()
# O1.get_area()
# O1.draw()

# P1=Pentagon(30)
# P1.__set__()
# P1.get_exteriorangle()
# P1.get_perimeter()
# P1.get_area()
# P1.draw()

# T1=Triangle(40, 9, 41)
# T1.__set__()
# T1.get_perimeter()
# T1.get_area()

# ET1=Equilateral_Triangle(100)
# ET1.__set__()
# ET1.get_perimeter()
# ET1.get_area()
# ET1.draw()

# Rh1=Rhombus(20, 30, 40)
# Rh1.__set__()
# Rh1.get_area()
# Rh1.get_perimeter()

# Sq=Square(100)
# Sq.__set__()
# Sq.get_area()
# Sq.get_perimeter()
# Sq.draw()

# El=Ellipse(42, 42)
# El.__set__()
# El.get_area()
# El.get_perimeter()

# c1=Circle(50)
# c1.__set__()
# c1.get_area()
# c1.get_perimeter()
# c1.draw()
