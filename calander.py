import calendar
print(calendar.TextCalendar(firstweekday=8).formatyear(2015))

date=input().split()
y=int(date[2])
m=int(date[1])
d=int(date[0])
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
