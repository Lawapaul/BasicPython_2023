
""" 
Hello Everyone! Welcome back to my another MiniProject. This project helps to 
solve problems of user who runs cleaning agency
"""

print("")
print("Welcome to Franks Cleaning Agency")
print("")


a=int(input("Enter Number of Small Rooms: "))
b=int(input("Enter Number of Large Rooms: "))
c=0.066
d=25
f=35
print("Cost of Cleaning Small Rooms: $25")
print("Cost of Cleaning Small Rooms: $35")
print("Tax: 6.6%")
print("="*50)
print("Total Estimation: $",((a*d)+(b*f))+((a*d)+(b*35))*c)
print("Price Valid for 30 days only")