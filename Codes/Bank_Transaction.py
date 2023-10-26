"""Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
 """
 
count=0
count1=0
lst=[]
while True:
     a=input("Enter (break/Break) to stop: ")
     lst.append(a)
     if a=="Break" or a=="break":
         break

lst.pop(len(lst)-1)
for i in lst:
    c=i.split(" ")
    if c[0]=="D" or c[0]=="d":
        count+=int(c[1])
    elif c[0]=="W" or c[0]=="W":
        count1+=int(c[1])

print("Total Deposit:",count)
print("Total Withdrawl:",count1)
print("Net Amount:",count-count1)