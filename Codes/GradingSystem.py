



def main(): 
 abd=int(input("Enter attendance percentage: "))
 b1=int(input("Enter Marks in Test1: "))
 b2=int(input("Enter Marks in Test2: "))
 b3=int(input("Enter Marks in Test3: "))
 bmw=(b1+b2+b3)/3
 if abd>=90:
     xyz=(b1+b2+b3+5)/3
     if xyz>=90:
         print("Final Grade: A (5 Marks Extra of Attendance)")
     elif xyz>=80 and xyz<=89:
         print("Final Grade: B (5 Marks Extra of Attendance)")
     elif xyz>=70 and xyz<=79:
         print("Final Grade: C (5 Marks Extra of Attendance)")
     elif xyz>=60 and xyz<=69:
         print("Final Grade: D (5 Marks Extra of Attendance)")
     elif xyz<60:
         print("Final Grade: F (5 Marks Extra for Attendance)")

 else:
     mno=(b1+b2+b3)/3
     if mno>=90:
         print("Final Grade: A")
     elif mno>=80 and mno<=89:
         print("Final Grade: B")
     elif mno>=70 and mno<=79:
         print("Final Grade: C")
     elif mno>=60 and mno<=69:
         print("Final Grade: D")
     elif mno<60:
         print("Final Grade: F")
  

main()

while True:
    a=input("Do you wish to continue (y/n): ")
    if a=='y' or a=='Y':
        main()
    else:
        print("Thankyou! Have a great day :) ")
        break