"""Update set1 by adding items from set2, except common items
"""

a=set(map(int,input().split()))
b=set(map(int,input().split()))
a.symmetric_difference_update(b)
print(a)
