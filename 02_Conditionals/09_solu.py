year=int(input("enter year: "))

leap=year%4==0

if(leap):
    print(year,"is leap year")
else:
    print(year,"is not leap year")