weather=input("Enter weather: ")

if weather not in ["sunny","rainy","snowy"]:
    print("only these valuse allowed 'sunny','rainy','snowy' ")
    exit()

if weather=="sunny":
    print("Go for a walk")
elif weather=="rainy":
    print("Read a book")
else:
    print("Build a snowman")