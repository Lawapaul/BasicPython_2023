"Program to Display the Sum of Primary and Secondary Diagonal elements of a Matrix"

a=int(input("Enter Number of Rows: "))
b=int(input("Enter Number of Columns: "))
lst=[]
for i in range(a):
    l=[]
    for j in range(b):
        l.append(int(input()))
    lst.append(l)

print("Matrix Created: ")
for i in lst:
    print(*i)

print()
count=0
for i in range(len(lst[0])):
    count+=lst[i][i]
print("Sum of Primary Diagonal:",count)
lst2=[]
count1=0
for i in lst:
    lst2.append(list(reversed(i)))
for k in range(len(lst2[0])):
    count1+=lst2[k][k]
print("Sum of Secondary Diagonal:",count)
