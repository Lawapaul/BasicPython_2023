
"""Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string

"""

a=input()
b=input()

def sum(a,b):
    if len(a)>len(b):
        return a
    elif len(a)<len(b):
        return b
    else:
        print(a)
        print(b)

print(sum(a,b))