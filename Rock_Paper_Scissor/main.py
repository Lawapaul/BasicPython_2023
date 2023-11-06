import random

name=input("\nEnter Username: ")
print()
print("-"*50)
print("                  W E L C O M E            ")
print("-"*50)
print()
print("*","Hello",name,"*")

def main():
    a=int(input("How many Chances you want to play: "))
    count=0
    count1=0
    for i in range(a):
        main=random.randint(1,3)
        compu=""
        if main==3:
            compu="rock"
        elif main==2:
            compu="paper"
        elif main==1:
            compu="scissor"
        inpu=input("\nRock\nPaper\nScissor\nEnter Your Choice: ")
        if compu=="rock":
            if compu=="rock" and inpu.lower=="paper":
                print("You Won. Congratulations!!!")    
                count+=1
            elif compu=="rock" and inpu.lower=="scissor":
                print("You Lost. Try Again!")
                count1+=1
            elif compu=="rock" and inpu.lower()=="rock":
                print("Tie. Try Again")
            else:
                print("Invalid Input. Try again!")
        elif compu=="paper":
            if compu=="paper" and inpu.lower()=="rock":
                print("You Loss. Better Luck Next Time!!!")
                count1+=1
            elif compu=="paper" and inpu.lower()=="scissor":
                print("You won. Congratulations!!!")
                count+=1
            elif compu=="paper" and inpu.lower()=="paper":
                print("Tie. Try again!")
            else:
                print("Invalid Input. Try again!")
        elif compu=="scissor":
            if compu=="scissor" and inpu.lower()=="rock":
                print("You Won. Congratulations!!!!")
                count=+1
            elif compu=="scissor" and inpu.lower()=="paper":
                print("You loss. Better Luck next Time!!!")
            elif compu=="scissor" and inpu.lower()=="scissor":
                print("Tie. Try again!")
            else:
                print("Invalid Input. Try Again!")
    if a>1:            
        if count==count1:
            print("\nMatch Tied. Well played!!!")
        elif count>count1:
            print("\nUser Won. Congratulations!!!!")
        elif count1>count:
            print("\nComputer Won. Better luck next Time!!!")
    

main()
while True:
    ch=input("Do you wish to coninue (y/n): ")
    if ch=='n' or ch=="N":
        print("\nThankyou. Have a great day ^_^")
        print()
        break
    else:
        main()

                
            
