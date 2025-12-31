file_obj = open("/Users/harshitsingh/Developer/Python/File_Handling/practice.txt",'r')
data = file_obj.read()
file_obj.close()

#Write
file_obj = open("/Users/harshitsingh/Developer/Python/File_Handling/practice.txt",'w')
file_obj.write(data.replace("Java","Python"))
file_obj.close()
