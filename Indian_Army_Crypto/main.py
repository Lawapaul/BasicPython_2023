"""Indian Army wants to send their string in a cryptic form. Assume the text 
   has only lower case characters. No special characters or upper case. 
   Write a Python user-defined function that takes the text as argument and 
   returns a cryptic text.

 The cryptic text is generated as follows:

The cryptic text must replace for each character their respective numeric 
position must be replaced. For example '1' for 'a', '10' for 'j'.....
However, if the numeric position is greater than single digit (above j) then a 
'-' must be prepended before the replacing digit. If the numeric position is a 
single digit, then no '-' need to prepend '-'. However, if a single digit 
numeric position follows a double-digit position, then it must be prepended 
by '-'.

"""

lst=[]
for i in range(97,123):
    lst.append(chr(i))
a=input("Enter Element: ")
lst2=[]
for i in a:
    lst2.append(i)
def main(a,lst,lst2):
    lst3=[]
    for i in lst2:
        ef=lst.index(i)
        lst3.append(str(ef+1))
    for i in range(len(lst3)):
        if int(lst3[i])>9:
            lst3[i]="-"+str(lst3[i])
    c="".join(lst3)
    return c

print(main(a,lst,lst2))
    
    
    