
print("\nW E L C O M E       T O      P H O N E B O O K")
print("="*50)
print()


dict1={}
def code():
 a=int(input("Enter number of contacts you want to enter: "))
 
 for x in range(a):
     key=input(f"Enter Name {x+1}: ")
     value=int(input(f"Enter Phone Number {x+1}: "))
     x=key.lower()
     dict1[x]=value
    
code()

print("Contacts Added Successfully.......")

print()
print("="*50)

def main():
 m=input("Enter Name to find its contact: ")
 n=m.lower()
 print("Phone number of",m.capitalize(),"is:",dict1[n])
 
main()

while True:
    ch=input("Do you wish to continue(y/n): ")
    if ch=='y':
        main()
    else:
        print("Thankyou! Have a great day")
        break
    

