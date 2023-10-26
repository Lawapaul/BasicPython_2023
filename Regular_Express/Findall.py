import re
a="bat cat rat mat dad "
b=r'.at'
match=re.findall(b,a)
print(match)

a="98ABCD cdef efhb 892gbdh"
b=r'\d'
match=re.match(b,a)
if match:
    print("True")
else:
    print("False")

