"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98"""

a=list(map(int,input("Enter Numbers with space: ").split()))
print(a)
print(tuple(a))