
def main():
    return "Hello World"

while True:
    a=input("Enter Username: ")
    if a=="admin":
        b=input("Enter Passcode: ")
        if b=="test":
            
            
            print(main())
            break
            
        
        else:
            print("Wrong Passcode")  
            print("\nDo you wish to continue (y/n): ") 
            voi=input()
            if voi=='n' or voi=='N':
              print("Thankyou!,Have a great day :) ") 
              break
            else:
              continue
             
        
            
            
            
    else:
        print("Wrong Username: ") 
       
        print("\nDo you wish to continue (y/n): ") 
        a=input()
        if a=='n' or a=='N':
            print("Thankyou!,Have a great day :) ") 
            break
        else:
            continue
        
          
    
            
            
            
        
        