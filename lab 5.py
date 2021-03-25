
def isLeapYear(year):
    if not (year % 4) == 0:
        return False
    elif (year % 100) == 0:
        if (year % 400) == 0:
            return False
    else:
        return True
print("enter a date")
date = input()
month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])


thirties = [4,6,9,11]
print(date)
if month == 2:
    if 1 <= day <= 28:
        print("valid day")
    elif day == 29:
        if isLeapYear(year):
            print("valid date")
        else:
            print("not leap year")
    else:
        print("day is invalid")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day <= 30:
        print("day valid")
    else:
        print("day is invalid")
        
elif month == 1 or month == 3 or month == 5 or month == 7 or month ==10 or month ==12:
    if 1 <= day <= 31:
        print("valid day")
    else:
        print("day is invalid")
else:
    print("invalid day")
