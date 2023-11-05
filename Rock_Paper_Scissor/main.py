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
        main=random.randint(1,4)
        compu=""
        if main==3:
            compu="Rock"
        elif main==2:
            compu="Paper"
        elif main==1:
            compu="Scissor"
        inpu=input("\n1. Rock\n2. Paper\n3. Scissor\nEnter Your Choice: ")
        print(main)
        if compu.lower()==inpu.lower():
            print("Tie. Try Again!")
        elif compu=="Rock":
            if compu=="Rock" and inpu.lower=="paper":
                print("You Won. Congratulations!!!")    
                count+=1
            elif compu=="Rock" and inpu.lower=="scissor":
                print("You Lost. Try Again!")
                count1+=1
            else:
                print("Invalid Input.")
        elif compu=="Paper":
            if compu=="Paper" and inpu=="rock":
                print("You Loss. Better Luck Next Time!!!")
                count1+=1
            elif compu=="Paper" and inpu=="scissor":
                print("You won. Congratulations!!!")
                count+=1
            else:
                print("Invalid Input.")
        elif compu=="Scissor":
            if compu=="Scissor" and inpu=="rock":
                print("You Won. Congratulations!!!!")
                count=+1
            elif compu=="Scissor" and inpu=="paper":
                print("You loss. Better Luck next Time!!!")
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

                
            
