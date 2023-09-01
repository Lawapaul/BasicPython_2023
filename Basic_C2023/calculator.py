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
      
    elif c==5:
        print("Thankyou, Have a great Day :))")
      
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
        
