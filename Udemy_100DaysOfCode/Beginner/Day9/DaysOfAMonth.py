def isLeapYear(year):
    if(year%4 == 0):
        if(year%100):
            if(year%400):
                return True
            else:
                return False
        else: 
            return True
    else: 
        return False
    
def days_in_the_month(year, month):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if(isLeapYear(year) and month == 2):
        return 29
    return days[month]
    
year = int(input("Enter the  year : "))
month = int(input("Enter the month : "))
print(f"days : {days_in_the_month(year,month)}")