lst=[]

def main():
 for i in range(0,3):
     b=int(input(f"Enter Marks {i+1}: "))
     if b==0:
         print("Invalid Marks. Try Again")
         d=int(input("Enter Marks: "))
         lst.append(d)
     else:
         lst.append(b)
         
 c=sum(lst)/3
 if c>=98:
    print("Eligible for Scolarship!!")
 else:
    print("Not Eligible for Scolarship!!")
         
main()
    

    
while True:
    ch=input("Do you wish to Continue(y/n): ")
    if ch=='n' or ch=='N':
        print("Thankyou! Have a great day!")
        break
    else:
        main()
    
