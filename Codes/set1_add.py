"""Exercise 4: Update the first set with items that don’t exist in the second set

    """

a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=set()
for i in a:
    if i not in b:
        c.add(i)

print(c)