# Problem Statement - Write a program that determines whether a year is a leap year or not. In the Gregorian calendar, a leap year occurs every four years to compensate for the fact that the Earth's orbit around the Sun takes approximately 365.25 days.
year = int(input("Enter a year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is Leap year")
else :
    print(year,"is not a leap year")