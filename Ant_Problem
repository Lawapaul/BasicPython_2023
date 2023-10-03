#This program calculates time taken by Ant to bring its food back to the nest by crossing a mountain.

lst=[]
n=int(input("Enter Range of Distance: "))
m=int(input("Enter Range of Speed: "))
for i in range(n):
    a=int(input(f"Enter Distance {i+1}: "))
    lst.append(a)



lst2=[]
for x in range(m):
    a=int(input(f"Enter Speed {x+1}: "))
    lst2.append(a)

lst.append(lst[0])


Total_Distance=sum(lst)

count=0
for i in range(len(lst)):
    for j in range(len(lst2)-1):
        if i==j:
         time=lst[i]/lst2[j]
         count+=time
 

hss=lst2[len(lst2)-1]
c=lst[0]/hss
total_time=(2*count)-lst[0]/lst2[0]
print("No of minutes:",total_time + c)
kh=(total_time + c)//60
hk=(total_time + c)%60
print(kh,"hours and",hk,"minutes.")



   