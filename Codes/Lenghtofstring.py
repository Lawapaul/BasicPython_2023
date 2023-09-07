def main():
    """Program to compare lenght of two string and display Yes, if the lenght is equal"""
    
    a=input("Enter String1: ")
    b=input("Enter String2: ")
    print("")
    print(main.__doc__)
    print("")
    print("String1: ",a)
    print("String2: ",b)
    
    if len(a)==len(b):
        print("Yes, Lenght is equal")
    else:
        print("No, Lenght is not equal")
        

main()