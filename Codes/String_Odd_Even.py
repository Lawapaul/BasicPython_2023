"""Program to print sum of count and Index of a substring in string"""

a=input("Enter String1: ")
b=input("Enter Character: ")
count=0
def main(a,b,count):
    for i in a:
      if i==b:
            count+=1

    lst=[]
    for i in range(len(a)):
        if a[i]==b:
            lst.append(i)
    d=sum(lst)
    if count==0:
        return "No"
    elif count%2==0 and d%2==0:
        return "EVEN-EVEN"
    elif count%2!=0 and d%2==0:
        return "ODD-EVEN"
    elif count%2!=0 and d%2!=0:
        return "ODD-ODD"
    elif count%2==0 and d%2!=0:
        return "EVEN-ODD"
    elif b not in a:
        return "No"
    
print("Ans:",main(a,b,count))

        