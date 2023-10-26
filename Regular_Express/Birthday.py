"""Kevin is the HR Manger of a Company. He designed a birthday e-card with a customizable date in it. 
He normally mails that card after filling the correct date. He was finding it difficult to check if 
the date was in correct format. Write a Python code to help him check the validity of the given date 
and expand and print the greeting message if valid using regular expression. 
If the date is invalid print as 'invalid'.

 Regular expression must perform the following:

H3112

First character must be H only (Expanded as Happy birthday)

Next 2 characters is the date (Date has 2 digits. Ex: 09 or 11 or 23 or 30 or 31 Date can have first

digit 0 or 1 or 2 or 3 only. If first digit is 3 then second digit can be 0 or 1 only)

Next 2 characters is month (Month has 2 digits. Ex: 07 or 10 or 11 or 12 Month can have first

digit 0 or 1 only. If first digit is 1 then second digit is 0 or 1 or 2 only)

Assume that the year is only for 2023

Also ensure that the correct number of days is specified based on month. For example: if month

is 12 day can be 30 or 31. If month is 04 then 31 day is not possible. If month is 02 and 2021 is

not a leap year upto 28 days is only possible. (Need not use regular expression) If there is a

mismatch print as INVALID.

If the code is correct expand as follows:

Happy birthday31-12-2023
    """
    
import re
a=input()
c=re.findall("\d{2}",a)
d=["01","03","05","07","08","10","12"]
if a[0]!="H":
    print("Invalid Input")
    
elif int(c[1])>12:
    print("Invalid Output")

elif int(c[0])>30:
    if int(c[0])>31:
        print("Invalid Input")
    elif int(c[0])>30 and c[1] not in d:
        print("Invalid Input")
    else:
        print("Happy Birthday",str(c[0])+"-"+str(c[1])+"-"+"2023")
else:
    print("Happy Birthday",str(c[0])+"-"+str(c[1])+"-"+"2023")