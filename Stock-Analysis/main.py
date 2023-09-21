

print("\n W E L C O M E       T 0     D A T A B A S E ")
print("="*50)


b=int(input("Enter Number of Entries you want to store: "))
dict1={}
for x in range(b):
    key=input(f"Enter Name of Item {x+1}: ")
    value=int(input(f"Enter Quantity of Item {x+1}: "))
    dict1[key]=value
    
print("Items Added Successfully.....")
    


print()

def Add():
    a=input("Enter Name of Item: ")
    c=int(input("Enter Quantity: "))
    dict2={}
    dict2[a]=c
    dict1.update(dict2)
    print(dict1.items())
    
    
def Delete():
    d=input("Enter Name: ")
    dict1.pop(d)
    print("Updated Invertory Successfully.....")
    print(dict1)

def Update():
    print("\n1. Sold\n2. Return")
    mh=int(input("Enter Choice: "))
    if mh==1:
        g=input("Enter Name: ")
        h=int(input("Enter Number of Quantites Sold: "))
        dict1[g]=dict1[g]-h
        print("Successfully Updated....",)
        print(dict1)
        
    elif mh==2:
        g=input("Enter Name: ")
        h=int(input("Enter Number of Quantites Returned: "))
        dict1[g]=dict1[g]+h
       
        print("Successfully Updated....")
        print(dict1)
    


def main():
 for x,y in dict1.items():
  if y<=5:
    print("\n ALERT!   LOW   STOCK  OF ",x.upper())
    
 print("\n1. Add\n2. Delete\n3. Update")
 ch=int(input("Enter Choice: "))
 if ch==1:
     Add()
 elif ch==2:
     Delete()
 elif ch==3:
     Update()
 elif ch==4:
    print("ThankYou! Have a Great day!")
    
main()


while True:
    mn=input("Do you wish to continue(y/n): ")
    if mn=='n' or mn=="N":
        print("Thankyou! Have a Great day")
        break
    else:
        main()

