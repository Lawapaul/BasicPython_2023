#Program to check wheather two numbers are Anagram or not

a=input("Enter String 1: ")
b=input("Enter String 2: ")
l1=[]
l2=[]
for i in a:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        l1.append(i)
for i in b:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        l2.append(i)

c="".join(sorted(l1))
d="".join(sorted(l2))
if c==d:
    print("Yes")
else:
    print("No")