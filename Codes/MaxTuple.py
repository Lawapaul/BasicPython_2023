#Program to take input in tuple and find maximum element in it

a=int(input("Enter Range of tuple: "))
tup=()

for x in range(0,a):
    a=int(input("Enter Elements: "))
    tup=tup+(a,)
    
print("Tuple: ",tup)
print("Maximum Element: ",max(tup))
