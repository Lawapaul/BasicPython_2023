"""Find the number of occurrences of a lower case and upper case characters
in a string"""

a=input()
count=0
count1=0
for i in a:
    if i.islower():
        count+=1
    elif i.isupper():
        count1+=1
    

print(count,count1)