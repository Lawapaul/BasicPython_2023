lst=[]
a=int(input("Enter Number of Rows: "))
b=int(input("Enter Number of Columns: "))

for i in range(a):
    c=list(map(int,input(f"Enter Row{i+1}: ").split()))
    if len(c)<b:
        print("Out of Index. Please Try again: ")
        d=list(map(int,input("Enter List again: ").split()))
        lst.append(d)
    else: 
     lst.append(c)

print("Matrix: ")
for i in range(a):
    for j in range(b):
        print(lst[i][j],end=" ")
    print()

print("Transposed Matrix: ")
for i in range(a):
    for j in range(b):
        print(lst[j][i],end=" ")
    print()


