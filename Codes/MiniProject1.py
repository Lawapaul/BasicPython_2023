"""Hello Everyone! Welcome to my github page. Hope you will find it interesting as I am newbie. 
My first mini project was to create python programme which helps to calculate disconted Mrp for 
a cloth store. It helps the customer to calculate without any hard efforts.
"""

print("           X Y Z    C O L L E C T I O N S         ")

original_price=int(input("Enter Original Price: "))
quantity=int(input("Enter Quantity: "))

if quantity>=1 and quantity<=9:
    print("Thankyou , you entered right format")
    if quantity>=6 and quantity<=9:
        print("Buy 6 and Get 1 free and 10% discount Applicable")
        x=quantity+1
        a=original_price*x*(1-10/100)
        print("Original Price: ",original_price)
        print("Quantity: ",x)
        print("Total Price: ",original_price*x)
        print("Discounted Price: ",a)
        print("Money Saved:  ",(original_price*x)-a)

    elif quantity>=3 and quantity<=4:
        print("20% Discount Applicable")
        a=original_price*quantity*(1-20/100)
        print("Original Price: ",original_price)
        print("Quantity: ",quantity)
        print("Total Price: ",original_price*quantity)
        print("Discounted Price: ",a)
        print("Money Saved:  ",(original_price*quantity)-a)

    elif quantity>=2 and quantity<3:
        print("15% Discount Applicable")
        a=original_price*quantity*(1-15/100)
        print("Original Price: ",original_price)
        print("Quantity: ",quantity)
        print("Total Price: ",original_price*quantity)
        print("Discounted Price: ",a)
        print("Money Saved:  ",(original_price*quantity)-a)

    elif quantity==1:
        print("Sorry No discount Applicable")
        print("Original Price: ",original_price)
        print("Quantity: ",quantity)
        print("Total Price: ",original_price*quantity)
        print("Discounted Price:0 ")
        print("Money Saved: 0 ")
else:
    print("Enter quantity less than 10")