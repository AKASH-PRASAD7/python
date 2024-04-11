
color = input("enter color: ")

if color not in ["Green", "Yellow", "Brown"]:
    print("Invalid color")
    exit()

if color=="Green":
    print("Unripe")
elif color=="Yellow":
    print("ripe")
else :
    print("Ovverripe")
    