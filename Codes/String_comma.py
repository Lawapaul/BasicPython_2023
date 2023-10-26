"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

a=input("Enter Words: ")
b=a.split(",")
lst=[]
for i in range(len(b)):
    lst.append(b[i])

lst.sort()
print(",".join(lst))