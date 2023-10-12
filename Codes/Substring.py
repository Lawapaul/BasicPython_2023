#Write a program to print all the substring in the form of lexicographic order(sorted)
a=input("Enter String: ")
l=[]
for i in range(len(a)):
    for j in range(len(a)):
        l.append(a[i:j+1])

l.sort()
for i in l:
    print(i)

#or

a=input("Enter String: ")
l=[a[i:j:]for i in range(len(a)) for j in range(len(a)+1) if i<j]
l.sort()
for i in l:
    print(i)