"""
Question:
Define a function which can generate and print a list where the values are square of numbers 
between 1 and 20 (both included).

 """
 
def list():
    lst=[]
    for i in range(1,20+1):
        lst.append(i**2)
    return lst

print(list())