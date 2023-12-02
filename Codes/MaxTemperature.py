"""To Take Temperature input from the user until and unless he gives -1. At -1 stop taking input.
Display maximum temperature.
"""

lst=[]
while True:
    a=int(input())
    if a==-1:
        break
    lst.append(a)

print(lst)
print("Max Temperature: ",max(lst))