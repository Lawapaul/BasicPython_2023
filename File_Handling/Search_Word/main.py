file_obj = open("/Users/harshitsingh/Developer/Python/File_Handling/practice.txt",'r')
data = file_obj.read()
if(data.find("learning")):
    print(data.index("learning"))
else:
    print("No")
