"""Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n."""

a=int(input("Enter Range: "))
for i in range(0,a+1):
    if i%7==0:
        print(i)