file_obj = open("/Users/harshitsingh/Developer/Python/File_Handling/practice.txt",'r')
data = True

def check_line(word):
    data = True
    line_no = 1
    while data:
        data = file_obj.readline()
        if(word in data):
            print(line_no)
            return
        line_no+=1
    print(-1)

check_line("learning")
file_obj.close()
