import math

print("")
print("")

print("      B A S I C    C A L C U L A T O R      ")

print("")
print("")

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("")
print("")


def main(a,b):
    
    print("1. Addtion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Trignometric Functions")
    print("6. Exit")
    print()
    
    c = int(input("Enter Choice: "))
    print()

    if c==1:
      print("Sum of",a,"and",b,"is: ",a+b)

    elif c==2:
      print("Sub of",a,"and",b,"is: ",a-b)
    
    elif c==3:
      print("Multiplication of",a,"and",b,"is: ",a*b)
    
    elif c==4:
      print("Division of",a,"and",b,"is: ",a/b)
      
    elif c==6:
        print("Thankyou, Have a great Day :))")
    
    elif c==5:
      print("**********TRIGONOMETRIC CALCULATOR**********")
      x=math.pi
      print("1. sin \n2. cos \n3. tan \n4. cosec \n5. sec \n6. cot")
      c=int(input("Enter the value of c : "))
      print("\nNumerator value is:",a)
      print("Denominator is:",b)
      
      if c==1:
          sin=math.sin(a*x/b)
          print(format(sin,'.2f'))
      elif c==2:
        cos=math.cos(a*x/b)
        print(format(cos,'.2f'))
    
      elif c==3:
        tan=math.tan(a*x/b)
        print(format(tan,'.2f'))
      elif c==4:
         cosec=math.cosec(a*x/b)
         print(format(cosec,'.2f'))
      elif c==5:
         sec=math.sec(a*x/b)
         print(format(sec,'.2f'))
      elif c==6:
        cot=math.cot(a*x/b)
        print(format(cot,'.2f'))
      else:
        print("Invalid Option: ")

print(main(a,b))
print()

while True:
    x=input("Do you wish to continue (y/n): ")
    if x=='n' or x=='N':
        print("Thankyou, Have a great day :)) ")
        break
    else:
     op=input("Do you wish to change Numbers (y/n): ")
    
     if op=='n' or op=='N':
         print(main(a,b))
        
     elif op=='y' or 'Y':
         z=int(input("Enter number: "))
         v=int(input("Enter Second Number: "))
         print(main(z,v))
        
     elif x=='n' or x=='N':
         print("Thankyou, Have a great day :)) ")
         break
    
     elif x=='y' or x=="Y":
         print(main(a,b))
        
