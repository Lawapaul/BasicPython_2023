#LeetCode Word Capital

word=input()
def detectCapitalUse(word):
    count=0
    count1=0
    for i in word:
        if len(word)>1:
            if i.isupper():
                count+=1
            elif i.islower():
                count1+=1
        elif i.isupper() or i.islower():
            count=len(word)    
    if count==len(word) or count1==len(word):
        return "True"
    elif count==1 and len(word)==1:
        return "True"
    elif count==1 and word[0]==word[0].upper():
        return "True"
    else:
        return "False"
    
print(detectCapitalUse(word))
