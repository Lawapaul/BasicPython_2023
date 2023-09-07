
#Program to take input in list and print double of the elements added in reverse order

def list():
    l=[]
    a=int(input("Enter Range of List: "))
    for x in range(0,a):
        b=int(input("Enter Elements of list: "))
        l.append(b)
        
    for x in range(0,a):
        l[x]=l[x]*2
        
    print("Output:",l[::-1])
    
list()