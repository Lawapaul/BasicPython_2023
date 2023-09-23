dict1={}
a=int(input("Enter lenght of dictionary: "))

def main():
 for i in range(a):
     key=input(f"Enter Name {i+1}: ")
     value=int(input(f"Enter Age {i+1}: "))
     dict1[key]=value
    

 for x,y in dict1.items():
    if y<18:
          print(x,"is not eligible for driving test!")
          
              
main()
        
while True:
    ch=input("Do you wish to continue(y/n)? ")
    if ch=='n' or ch=="N":
        print("Thankyou! Have a great day")
        break
    else:
        main()