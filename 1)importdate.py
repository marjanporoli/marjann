import datetime
today = datetime.date.today()
startyear=today.year
endyear= int(input("Enter end year: "))
print("leap years are: \n")
for year in range(startyear,endyear):
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year.".format(year))
    elif (year % 4 ==0) and (year % 100 != 0):
        print("{0} is a leap year.".format(year))



