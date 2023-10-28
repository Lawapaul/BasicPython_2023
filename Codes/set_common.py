"""Exercise 7: Check if two sets have any elements in common. If yes, display the common elements"""

a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=a.intersection(b)
if len(c)>0:
    print(c)
else:
    print("none")