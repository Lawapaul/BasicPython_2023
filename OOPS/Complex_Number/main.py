
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def display(self):
        print(self.real,"+",self.imag,"i")

    def addition(self,obj_2):
        return Complex(self.real + obj_2.real,self.imag + obj_2.imag)

def main():
    obj_1 = Complex(3,2)
    obj_2 = Complex(4,3)
    obj_1.display()
    obj_2.display()
    obj_3 = obj_1.addition(obj_2)
    obj_3.display()

main()