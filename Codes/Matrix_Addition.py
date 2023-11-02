"""PS_MatCreateAdd
Sub-Task 1: Write a user defined function to create matrix with desired number 
            of rows and columns with elements filled with user input.

Sub-Task 2: Write a user defined function to add two matrices and display the 
            result"""
            
lst=[]
lst2=[]
a=int(input("Enter Number of Rows of Matrix 1: "))
b=int(input("Enter Number of Columns of Matrix 1: "))
for i in range(a):
    lst.append(int(input(f"Enter Row Element {i+1}: ")))
for j in range(b):
    lst2.append(int(input(f"Enter Column Element {j+1}: ")))

c=int(input("Enter Number of Rows of Matrix 2: "))
d=int(input("Enter Number of Columns of Matrix 2: "))
lst3=[]
lst4=[]
for i in range(c):
    lst3.append(int(input(f"Enter Row Element {i+1}: ")))
for j in range(d):
    lst4.append(int(input(f"Enter Column Element {j+1}: ")))

l=[]
def main(l,lst,lst3):
    for i in range(len(lst)):
        for j in range(len(lst3)):
            if i==j:
                l.append(lst[i]+lst3[j])
    return l
print(main(l,lst,lst3))

l1=[]
def main2(l1,lst2,lst4):
    for i in range(len(lst2)):
     for j in range(len(lst4)):
         if i==j:
             l1.append(lst2[i]+lst4[j])
    return l1
    
print(main2(l1,lst2,lst4))