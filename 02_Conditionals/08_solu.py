password=input("Enter password: ")

if len(password)>10:
    print("strong")
elif len(password)>=6:
    print("medium")
else:
    print("weak")