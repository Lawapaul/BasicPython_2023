"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""

a=input()
count=0
for i in range(0,4):
    b=a+(a*i)
    count+=int(b)
    
print(count)