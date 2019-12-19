# using calendar module 
import calendar
year =int(input('Enter the value of year : '))
leap_year = calendar.isleap(year)
if leap_year :
    print ('The given year is a leap year. ')
else :
    print('The given year is a non leap year. ')

# By using leap year condition 
y=int (input ('Enter the value of year : '))
if y%400==0 or y%4==0 and y%100!=0:
    print('The given year is a leap year. ')
else:
    print('The given year is a non leap year. ')
    