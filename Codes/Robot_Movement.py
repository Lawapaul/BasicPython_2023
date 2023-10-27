"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
 """

import math
lst=[]
while True:
    a=input()
    b=a.split(" ")
    if a=="Break" or a=="break":
        break
    lst.append(b)

print(lst)    
lst2=[]
lst3=[]
lst4=[]
lst5=[]
for i in range(len(lst)):
    if lst[i][0]=="UP":
        c=int(lst[i][1])
        lst2.append(c)
    elif lst[i][0]=="DOWN":
        c=int(lst[i][1])
        lst3.append(c)
    if lst[i][0]=="RIGHT":
        c=int(lst[i][1])
        lst4.append(c)
    elif lst[i][0]=="LEFT":
        c=int(lst[i][1])
        lst5.append(c)
        
total=abs(sum(lst2)-sum(lst3))
total1=abs(sum(lst5)-sum(lst4))
formula=(total*total)+(total1*total1)
print(f"Distance from position: {math.sqrt(formula):.2f}")