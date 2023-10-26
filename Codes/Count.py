"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""

a=input()
count=0
coun1=0
for i in a:
    if i.isalpha():
        count+=1
    elif i.isdigit():
        coun1+=1

print("LETTERTS:",count)
print("DIGITS:",coun1)