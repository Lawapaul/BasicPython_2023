n=int(input("Enter Range: "))
def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0:
            if i%5==0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%3!=0 and i%5==0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(n)