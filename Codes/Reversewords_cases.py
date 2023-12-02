"Program to Reverse Words and Swap Cases"

a=input()
b=a.split()
lst=[]
for i in b:
    c=i.swapcase()
    lst.append(c)
    
lst=lst[::-1]
f=" ".join(lst)
print(f)
    
