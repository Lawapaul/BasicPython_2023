drinks = [{"type": "water","calories": 0,"number_consumed": 7,"caffeinated": False },
    { "type": "orange juice","calories": 220,"number_consumed": 4,"caffeinated": False },
    {"type": "gatorade","calories": 140,"number_consumed": 1,"caffeinated": False},
    { "type": "cappuccino", "calories": 350,"number_consumed": 2,"caffeinated": True},
    {"type": "hot tea","calories": 5,"number_consumed": 3, "caffeinated": True}]

"""Exercise 1: How many different kinds of drinks are represented?
Exercise 2: How many total consumed drinks?
Exercise 3: How many total consumed calories?
Exercise 4: How many types of drinks are caffeinated?
Exercise 5: How many total consumed drinks were non-caffeinated?
Exercise 6: What is the drink with the highest amount of calories per drink?
Exercise 7: Which drink was consumed the least? (has the lowest number_consumed)
Exercise 8: If we consume all of these beverages, what is the average calorie count per drink?"""

print("Types:",len(drinks))

count=0
for i in range(len(drinks)):
    count=count+drinks[i]['number_consumed']

print("Total consumed: ",count)

coun=0
for i in range(len(drinks)):
    coun+=drinks[i]['calories']
print("Total Calories:",coun)

cou=0
co=0
for i in range(len(drinks)):
    if drinks[i]['caffeinated']==True:
        cou=cou+1
    elif drinks[i]['caffeinated']==False:
        co=co+1

print("Caffeinated Drinks are:",cou)
print("Non Caffeinated Drinks are:",co)

lst=[]
for i in drinks:
    d=i["calories"]
    lst.append(d)

a_min=min(lst)
a_max=max(lst)
for i in drinks:
    if i["calories"]==a_max:
        print("Max Calory Drink:",i["type"])
    if i["calories"]==a_min:
        print("Least Calory Drink:",i["type"])

print("Average Calories:",sum(lst)/len(lst))
