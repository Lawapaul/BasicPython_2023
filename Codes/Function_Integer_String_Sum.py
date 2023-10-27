"""
    Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
"""

a=input()
b=input()
def sum(a,b):
    return int(a)+int(b)

print(sum(a,b))