def main():
    a=int(input("Enter Number: "))
    if abs(a)==a:
        print("Entered Number is Positive: ")
        
    else:
        y=a*(-1)
        print("Number Converted: ",y)

print(main())