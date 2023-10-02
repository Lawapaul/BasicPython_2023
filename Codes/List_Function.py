
h=list(map(int,input("Enter list with space: ").split()))

def main():
    print("1. Insert\n2. Print\n3. Append\n4. Remove\n5. Sort\n6. Pop\n7. Reverse\n8. Exit")
    inpu=int(input("Enter Choice: "))
    if inpu==1:
        a=int(input("Enter Index Value: "))
        b=int(input("Enter Number: "))
        h.insert(a,b)
        print("New list: ",h)
    
    elif inpu==2:
        print(h)
    elif inpu==3:
        a=int(input("Enter Number to append: "))
        h.append(a)
        
    elif inpu==4:
        a=int(input("Enter element to remove: "))
        h.remove(a)
        print(h)
    elif inpu==5:
        h.sort()
        print(h)
    elif inpu==6:
        h.pop()
        print(h)
    elif inpu==7:
        h.sort(reverse=True)
        print(h)
    
    else:
        print("Have a great day! Thankyou.")
        
main()

while True:
    ch=input("Do you wish to continue(y/n): ")
    if ch=='n' or 'N':
        print("Thankyou! Have a great day.")
        break
    else:
        main()