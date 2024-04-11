import datetime

age:int= int(input("Enter age: "))

day=datetime.datetime.today().strftime("%A")

price = 12 if age>=18 else 8

if day=="Wednesday":
    print("$",price-2)
else:
    print("$",price)
    

    



