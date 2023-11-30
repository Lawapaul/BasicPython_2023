from getpass import getpass

a=input("\nEnter First and Middle Name(if any): ")
b=input("Enter Surname: ")
c=input("Enter Player 1 Name: ")
d=input("Enter Player 2 Name: ")
print("-"*50)
print("\n               M A S T E R M I N D             ")
print()
print("-"*50)

def main(a,b,c,d):
    print()
    print()
    print("*","Welcome",a,b,"*")
    print()
    count=0
    person1=getpass("Enter Number: ")
    print("Number Encoded:",len(person1)*"*")
    while True:
        person2=input("Player 1 Guess: ")
        if person2==person1:
            print()
            print("You Guessed Right. Player 2 Chance")
            break
        else:
            count+=1
            encoded=[]
            for i in range(len(person1)):
                encoded.append("*")
            lst1=[]
            for i in person2:
                lst1.append(i)
            for i in range(len(person1)):
                if person2[i]==person1[i]:
                    encoded[i]=person1[i]
            final_encoded="".join(encoded)
            print("Decoded Message:",final_encoded)
            continue
    print()

    perso=getpass("Next player enter Number: ")
    print("Number Encoded:",len(perso)*"*")
    count1=0
    while True:
        person2=input("Player 2 Guess: ")
        if person2==perso:
            print()
            print("Chance Over!!!!")
            print("Results are........")
            break
        else:
            encoded=[]
            for i in range(len(perso)):
                encoded.append("*")
            lst1=[]
            for i in person2:
                lst1.append(i)
            for i in range(len(person1)):
                if person2[i]==perso[i]:
                    encoded[i]=perso[i]
            final_encoded="".join(encoded)
            print("Decoded Message:",final_encoded)
            count1+=1
            continue
    print()
    if count>count1:
        print(d,"is the Mastermind!!!!!")
    elif count<count1:
        print(c,"Player 1 is the Mastermind!!!!!")
    elif count==count1:
        print("Match Tied. Better Luck Next Time!!!")
        
    
main(a,b,c,d)

while True:
    ch=input("Do you wish to continue (y/n): ")
    if ch=='n' or ch=="N":
        print("Thankyou! Have a great day :) ")
        break
    else:
        main(a,b,c,d)
        