"""This program helps waiter to provide family scheme to its members against
certain conditions

>>Starter should consists only:
            *Panner Tikka - P
            *Hara Bara Kabeb - H
            *Achari Tikka- A
            *Shammi Kabal - S
            *Fish Tikka - F
            
>>Main Course should consists only:
            *Laal Maas - L
            *Chicken Curry - C
            *Dal Tadka- D

>>Sweet Dish should consists only:
            *Cake - L
            *Black Forest Pastery - B

>>No of Family Members should not be more that 6.
>>Cost per person is Rs.1000.
>>Print their Total Bill if they pass all the conditions else display INVALID.
            
            

            


"""

import re
a=input("Enter Order: ")
b=a.split("-")
def main(a,b):
    cond1=r"PHASF"
    cond2=r"LCD"
    cond3=r"GH"
    match1=re.match(cond1,a)
    if match1:
        match2=re.match(cond2,a)
        if match2:
            match3=re.match(cond3,a)
            if match3:
                if int(b[-2])>6:
                    print("Invalid")
                else:
                    print(int(b[-2])*1000)
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")

main(a,b)