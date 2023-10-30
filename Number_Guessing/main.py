
import random


a=input("\nEnter your Name: ")
b=input("Enter your Surname: ")
print("-"*50)
print("\n               D I C E    G A M E          ")
print()
print("-"*50)


print()
print()
print("*","Welcome",a,b,"*")
print()
c=list(map(int,input("Enter range in format ( Lower Number (space) Highest Number ): ").split()))
print("Range:",c[0],"-",c[1])
ch=input("Do you wish to Re-Enter(y/n) : ")
if ch=='y':
    d=list(map(int,input("Enter range in format ( Lower Number (space) Highest Number ): ").split()))    
    print("Range:",d[0],"-",d[1])
    c=d

main=random.randint(c[0],c[1])   
print()
print("Random Number Generating......")
print("Random Number Generated!!!")
print()
inpu=int(input("Enter Number: "))
    

    
    
    
    
