"Program to convert a string into upper case"

a=input("Enter String: ")
b=a.split(" ")
def main(a,b):
    for i in range(len(b)):
        b[i]=b[i].upper()
    c=" ".join(b)
    return c
print(main(a,b))
