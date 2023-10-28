"""Exercise 3: Get Only unique items from two sets"""

a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(sorted(a.union(b)))