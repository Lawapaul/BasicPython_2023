class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r
    
c1 = Circle(5)
print(c1.area()," ",c1.perimeter())