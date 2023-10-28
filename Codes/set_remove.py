"""
    Exercise 5: Remove items from the set at once
    """
a=set()
b=set(map(int,input().split()))
c=int(input())
for i in range(c):
    d=int(input())
    a.add(d)

b.difference_update(a)
print(b)