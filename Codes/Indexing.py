
"""
2. A list of N integers with non-zero values is passed as the input to the program.
The program must print another list of size N where value at each index will
be the sum of all the values in the input list except the value at that index in the input list.
"""

lst=list(map(int,input("Enter list: ").split()))
lst1=[]
sum=sum(lst)
for i in range(len(lst)):
    c=sum-lst[i]
    lst1.append(c)

print(lst1)
