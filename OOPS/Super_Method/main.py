class Student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def details(self):
        print(self.fname,self.lname)
class Graduation(Student):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year

    def Year(self):
        print(self.year)


s1 = Graduation("Harshit","Singh",2027)
s1.details()
s1.Year()