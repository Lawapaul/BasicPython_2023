"Programme to Extract Toll free number from a big database"

import re
a=input()
pattern=r"\b[111|222|333|444|555|666|777|888|999]{3}[-]+[111|222|333|444|555|666|777|888|999]{3}[-]+[111|222|333|444|555|666|777|888|999]{3}\b"
d=re.findall(pattern,a)
lst=["111","222","333","444","555","666","777","888","999"]
lst2=[]
for i in d:
    e=i.split("-")
    for j in e:
        if j in lst:
            lst2.append(i)
lst3=[]
for i in lst2:
    if i not in lst3:
        lst3.append(i)
print(lst3)

            
   


