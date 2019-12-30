import calender 
d,m,y = map(int (input('Enter the value of date, month and year ').split()))
a=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
try:
    s=calender.weekday(y,m,d)
    print('Weekday: ',a[s])
except ValueError:
    print('You have entered an invalid date. ')