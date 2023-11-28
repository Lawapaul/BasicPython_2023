"DNA CHECK"

a=input("Enter String 1: ")
b=input("Enter String 2: ")
count=0
for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
if count>=3:
    print("Mutuation")
else:
    print("Same")