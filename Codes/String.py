"""Program to take a string in a input from user. Take another input from a user which consists new
letter and desired index position. Update the new letter at the desired index position and print the
output.
"""

a=input()
b=list(map(str,input().split()))
c=int(b[0])
d=str(b[1])
f=list(a)
f[c]=d
print("".join(f))


