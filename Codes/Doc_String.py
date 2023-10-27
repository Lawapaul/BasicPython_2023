"""Question 24
Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document 
    online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function"""

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2:"))
def sum(a,b):
    
    '''This program is built by Harshit Singh Shekhawat
    
    It helps to Calculate sum of two numbers by entering input
    '''
    
    return a+b

print(sum.__doc__)
print(sum(a,b))