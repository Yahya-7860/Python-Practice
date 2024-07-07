year = int(input("Enter Year = "))

isLeap = "false"

if year % 100 == 0:
    if (year/100) % 4 == 0:
        isLeap = 'true'
elif year % 4 == 0:
    isLeap = 'true'

if isLeap == 'true':
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
