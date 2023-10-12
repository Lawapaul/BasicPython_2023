a=input("Enter Blood Composition: ")
a=list(a)
dna=['G','A','U','T']
rna=['G','A','U','M']
flag1=True
flag2=True
for i in a:
    if i not in dna:
        flag1=False
    elif i not in rna:
        flag2=False

if flag1:
    print("DNA")
elif flag2:
    print("RNA")
else:
    print("None")
    

