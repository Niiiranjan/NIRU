class area:
    def __init__(self,breadth):
        self.breadth=breadth
class rectangle(area):
    def area_rectangle(self):
        print(self.len*self.breadth)
class circle(area):
    def area_circle(self):
        print(3.14*self.rad**2)
class square(area):
    def area_square(self):
        print(self.len**2)
r=rectangle(3)
r.len=int(input("Enter the length of the rectangle: "))
r.area_rectangle()
c=circle(0)
c.rad=int(input("Enter the radius of the circle: "))
c.area_circle()
s=square(0)
s.len=int(input("Enter the length of the square: "))
s.area_square()
