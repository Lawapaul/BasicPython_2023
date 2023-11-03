import Operators
from Operators import *
def main():
    a=int(input("Enter Num 1: "))
    b=int(input("Enter Num 2: "))
    ch=int(input("1. ADD\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\nINPUT: "))
    if ch==1: 
        print("Addition is: ",Operators.main(a,b))
    elif ch==2:
        print("Subtraction is:",Operators.sub(a,b))
    elif ch==3:
        print("Multiplication is:",Operators.multiplication(a,b))
    elif ch==4:
        print("Division is:",Operators.division(a,b))
    else:
        print("ThankYou!")

main()
while True:
    chn=input("Do you wish to continue (y/n): ")
    if chn=="n" or chn=="N":
        print("Have a great Day!")
        break
    else:
        main()
