"""The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. 
    It's simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter 
    with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced 
    by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently
    used it to communicate with his officials.
"""

a=input()
b=int(input("Enter Space: "))
lst2=[]
for i in a:
    c=ord(i)+b
    if c>90 and c<97:
        d=abs(90-c)
        lst2.append(chr(64+d))
    elif c>122:
        d=abs(122-c)
        lst2.append(chr(96+d))
    else:
        lst2.append(chr(c))
lst2="".join(lst2)
print(lst2)