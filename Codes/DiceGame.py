import random
print("Welcome to Dice Game!")
print()

def main():
    a=input("Press (y/n) to roll Dice 1: ")
    if a=='y' or a=='Y':
        b=input("Press (y/n) to roll Dice 2: ")
        if b=='y' or b=='Y':
            
            c=random.randint(1,6)
            print("Number appeared on Dice1: ",c)
            d=random.randint(1,6)
            print("Number Appeared on Dice2: ",d)
            if c>d:
                m=str(c)+str(d)
                print("Highest Number: ",int(m))
                
            elif c<d:
                m=str(d)+str(c)
                print("Higest Number: ",int(m))
            
            elif c==d:
                print("Foul Disqualified!!!")
                
               
            while True:
                ch=input("Do you wish to continue(y/n): ")
                if ch=='n' or ch=='N':
                    print("Thankyou! Have a great day :)) ")
                    break
                else:
                    main()
                    break
                    
                
                    
            
        
        else:
            print("Thankyou! Have a great day :)) ")
        
    else:
        print("ThankYou! Have a Great Day :)) ")
        
main()

