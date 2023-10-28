"""Exercise 6: Return a set of elements present in Set A or B, but not both"""
a=set(map(int,input().split()))
b=set(map(int,input().split()))

a.symmetric_difference_update(b)
print(a)
