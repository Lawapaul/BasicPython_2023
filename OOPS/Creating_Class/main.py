
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        return sum(self.marks)/3
    
def main():
    s1 = Student("Harshit",[99,94,95])
    print(s1.avg())

main()
