
str1=input("Enter First Heart Pulse: ")
str2=input("Enter Second Heart Pulse: ")
count=0
def main(str1,str2,count):
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            count+=1
    accuracy=((count)/len(str1))*100
    return f"{accuracy:.1f}"
print(main(str1,str2,count))