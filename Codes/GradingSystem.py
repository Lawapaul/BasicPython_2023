a=int(input("Enter Attendence Percentage: "))
b1=int(input("Enter Marks in Test1: "))
b2=int(input("Enter Marks in Test2: "))
b3=int(input("Enter Marks in Test3: "))

bmw=(b1+b2+b3)/3

def main()
 if a>=90:
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
     if bmw>=90:
         print("Final Grade: A")
     elif bmw>=80 and bmw<=89:
         print("Final Grade: B")
     elif bmw>=70 and bmw<=79:
         print("Final Grade: C")
     elif bmw>=60 and bmw<=69:
         print("Final Grade: D")
     elif bmw<60:
         print("Final Grade: F")
  

main()

while True:
    a=int(input("Do you wish to continue (y/n): "))
    if a=='y' or a=='Y':
        print(main)
    else:
        print("Thankyou! Have a great day :) ")