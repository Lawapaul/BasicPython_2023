# Match - It matches a character in string and return output
import re

a=r'Hello was Harshit Singh Shekhawat'
b="H|harshit"

match=re.match(b,a)
if match:
    print("Successful")
else:
    print("Unsuccessful")