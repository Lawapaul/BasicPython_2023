a=int(input("Enter Number of ID's you want to Enter: "))
dict1={}
for i in range(a):
    key=input("Enter ID: ")
    value=int(input("Enter Value: "))
    dict1[key]=value

lst=[]
b=int(input("No of customers who shopped: "))
for i in range(b):
    abc=input(f"Enter ID {i+1}: ")
    lst.append(abc)
    
women=[]
men=[]
#0 - indicates Men
#1 - indicates Women
for i,j in dict1.items():
    if j==0:
        men.append(i)
    elif j==1:
        women.append(i)
lst2=[]
lst3=[]
for i in lst:
    if i in men:
        lst2.append(i)
    elif i in women:
        lst3.append(i)

a=set(lst2)
b=set(lst3)
union=a.union(b)
lt=set(dict1)
diff=set(lst).difference(union)
print("Women ID:",b)
print("Male ID",a)
print("Neither Women Nor Men:",diff)

