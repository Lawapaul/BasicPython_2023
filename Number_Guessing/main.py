
import random


a=input("\nEnter First and Middle Name(if any): ")
b=input("Enter Surname: ")
c=input("Enter Username: ")
print("-"*40)
print("\n               S T E L L A           ")
print()
print("-"*40)

def main(a,b,c):
    print()
    print()
    print("*","Welcome",a,b,"*")
    print("*","Username",c,"*")
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

    if inpu>c[0] and inpu<c[1]:
        if inpu==main:
            print("Congratulation!!!! Guessed in First Attempt")
        else:
            print("Wrong!!!! Try Again (3 Chances Left).")
            abc=int(input("Enter Number: "))
            if abc==main:
                print("Congratulation. You WIN!!!")
            elif abc>0:
                efg=int(input("Guessed Too High. Try again (2 Chances left): "))
                if efg==main:
                        print("Congratulations! You guessed right ^_^")
                elif efg>main:
                        chance_2=int(input("Guessed too high again (Last Chance): "))
                        if chance_2==main:
                            print("Congratulations!!! You guessed right ^_^")
                        else:
                            print("Failed. Better Luck next time.")
                            print("Answer was:",main)
            
                elif efg<main:
                        chance_2=int(input("Guessed Too low. Try again (Last Chance): "))
                        if chance_2==main:
                            print("Congratulations!!! You guessed Right ^_^")
                        else:
                            print("Failed. Better Luck Next time.")
                            print("Answer was:",main)
            elif abc<0:
                efg=int(input("Guessed Too Low. Try again (2 Chances left): "))
                if efg==main:
                    print("Congratulations! You guessed right ^_^")
                elif efg>main:
                    chance_2=int(input("Guessed Too high again (Last Chance): "))
                    if chance_2==main:
                        print("Congratulations!!! You guessed right ^_^")
                    else:
                        print("Failed. Better Luck next time.")
                        print("Answer was:",main)
            
                elif efg<main:
                    chance_2=int(input("Guessed Too low. Try again (Last Chance): "))
                    if chance_2==main:
                        print("Congratulations!!! You guessed Right ^_^")
                    else:
                        print("Failed. Better Luck Next time.")
                        print("Answer was:",main)
    else:
        print("Number out of Range!!")     
    
main(a,b,c)
while True:
    ch=input("Do you wish to continue (y/n): ")
    if ch=="n" or ch=="N":
        print("Thankyou. Have a great day ahead ^_^")
        print() 
        break
    else:
        main(a,b,c)


            

    
    
    
    
