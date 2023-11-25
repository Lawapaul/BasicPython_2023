import re

str1=input()
str1_split=str1.split("-")
pattern="\d{2}"
find=re.findall(pattern,str1)
l1=["01","03","05","07","08","10","12"]
l2=["02","04","06","09","11"]
if find[0]>"31":
    print("Invalid")
elif find[1]>"12":
    print("Invalid")
elif find[0]<="31":
    if find[1] in l1:
        if str1_split[1]=="A":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Agra")
        elif str1_split[1]=="E":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Eroget")
        elif str1_split[1]=="I":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Indore")
        elif str1_split[1]=="O":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Ooty")
        elif str1_split[1]=="U":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"UP")
    else:
        print("Invalid")
elif find[0]<="30":
    if find[1] in l2:
        if str1_split[1]=="A":
            print("Delhi"+find[0]+"-"+find[1]+"-"+"Agra")
        elif str1_split[1]=="E":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Eroget")
        elif str1_split[1]=="I":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Indore")
        elif str1_split[1]=="O":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"Ooty")
        elif str1_split[1]=="U":
            print("Delhi"+"-"+find[0]+"-"+find[1]+"-"+"UP")
    else:
        print("Invalid")
else:
    print("Invalid")