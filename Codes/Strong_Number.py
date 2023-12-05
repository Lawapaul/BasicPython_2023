#Python Program to Check if a number is a strong number or not

a=input()
lst=[]
for i in a:
    lst.append(int(i))
count=0
for i in range(len(a)):
    factorial=1
    for j in range(1,int(lst[i])+1):
        factorial=factorial*j
    count+=factorial
if count==int(a):
    print("Strong Number: ")
else:
    print("No Strong Number")