"Given, an array of size n. Find an element that divides the array into two sub-arrays with equal sums."


a=int(input())
lst=[]
for i in range(a):
    lst.append(int(input()))
flag=False
count=0
count1=0
for i in lst:
    if i==0:
        count+=1
for i in range(len(lst)):
    if len(lst)==0 or lst[i]==0:
        flag==False
    elif sum(lst[0:i])==sum(lst[i+1:len(lst)]):
        count=i
        flag=True
        break
    else:
        flag=False

if flag==False:
    print("NO SUCH NUMBER")
else:
    print("Element",lst[count],"at Index",count)
    
