"""
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
"""

a=int(input())
def check(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"

print(check(a))