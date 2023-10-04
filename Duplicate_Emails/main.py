a=int(input("Enter Range: "))
lst=[]
for i in range(a):
    b=int(input(f"Enter Email-ID {i+1}: "))
    lst.append(b)

lst1=[]
lst2=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
    else:
        lst2.append(i)

print("Cleaned Inbox with Email-ID's:",lst1)
print("Duplicate Email ID's:",lst2)
print("Total duplicate Entries found: ",len(lst2))
print("="*40)
for i in lst1:
    if i in lst2:
        print("Count of Email-ID",i,"is",lst2.count(i))
print("="*40)

