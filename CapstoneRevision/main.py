def calculate_average(marks):
    return sum(marks)/5

def avg(dict,n):
    Sum=0
    idx=1
    marksSum=[0,0,0,0,0]
    for y in dict.values():
        for j in range(0,5):
            marksSum[j] += y[j]
    for x in marksSum:
        print(f"Subject {idx} : {x/5:.2f}\n")
        idx+=1


def highest_lowest_marks(dict):
    highestMarks = [0,0,0,0,0]
    lowestMarks = [10**18,10**18,10**18,10**18,10**18]
    for y in dict.values():
        Min = y[0]
        for i in range(0,5):
            if(lowestMarks[i] > y[i]): lowestMarks[i] = y[i]
            if(highestMarks[i] < y[i]): highestMarks[i] = y[i]
    for i in range(0,5):
        print(f"\nSubject {i+1}\nHighest Marks: {highestMarks[i]}\nLowest Marks: {lowestMarks[i]}\n")
    
def failed_students(dict):
    count=0
    for x,y in dict.items():
        if(calculate_average(y) < 50): count+=1
    print(f"\nFailed Students: {count}\n")

def Subject_Analysis(dict):
    failed_students(dict)  #Failed Students
    highest_lowest_marks(dict) #Highest Lowest Marks

def assign_grade(avg):
    if(calculate_average(avg)>=85): return 'A'
    elif(calculate_average(avg)>=70): return 'B'
    elif(calculate_average(avg)>=50): return 'C'
    else: return 'F'

def topper(dict):
    topper_Name=" "
    topper_avg=0
    for x,y in dict.items():
        if(calculate_average(y) > topper_avg):
            topper_Name=x
            topper_avg=calculate_average(y)
    print(f"Topper\nTopper Name: {topper_Name}\nAverage Marks: {topper_avg:.2f}")

n = int(input("Enter Number of Students: "))
dict = {}
topper_name = ""
topper_marks = 0
for i in range(0,n):
    name = input(f"Enter Student {i+1} Name: ")
    list = []
    for j in range(0,5):
        marks = int(input(f"Enter Marks in Subject {j+1}: "))
        list.append(marks)
    dict[name] = list

#Avg marks
print("\nAVERAGE MARKS \n")
for x,y in dict.items():
    print(x," : ",calculate_average(y))

#Assign Grade
print("\nGrades\n")
for x,y in dict.items():
    print(x," : ",assign_grade(y))

#Class topper
print("\nTopper Name: ",topper_name," with Marks",topper_marks,"\n")

#class Avg
print("\nCourse Avg Marks\n")
avg(dict,n)

#Subject Analysis
Subject_Analysis(dict)
