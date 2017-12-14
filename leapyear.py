# leap year prograsm in  python  using the functions
def leapyear(n):
    if n%4==0 and n%100!=0:
        if n%400==0:
            print("the given year is leap year")
        elif n%100!=0:
            print("the given year is not a leap yaer")
    elif n%4==0:
        print("the givewn year is leap ")
print(leapyear(2017))

#leap year program using conditions and user input
year =int(input("enter the yeaar:"))
if year%4==0:
        if year%100!=0:
            if year%400==0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year ".format(year))