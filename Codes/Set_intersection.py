"""
Exercise 2: Return a new set of identical items from two sets
"""

a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(a.intersection(b))
