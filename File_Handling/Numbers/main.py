
#Creating File

# data = "1,2,3,4,5,6,7,8,9\n,10,11,12,13,14,15"
# file = open("Numbers.txt","w")
# file.write(data)
# file.close()

#Count Even Numbers
file = open("/Users/harshitsingh/Developer/Python/File_Handling/Numbers/Numbers.txt",'r')
data = file.read().split(',')
count = 0
for i in data:
    if(int(i)%2==0): count+=1
print(count)
result = " ".join(data)
print(result)