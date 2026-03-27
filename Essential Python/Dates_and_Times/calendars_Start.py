#
# Example file for working with calendars
# LinkedIn Learning Python course
#


# TODO: import the calendar module
import calendar

# # TODO: create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2026, 3, 0, 0)
# print(str)

# #TODO: create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth(2026, 3)
# print(str)

# # TODO: loop over the days of a month
# # zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2026, 7):
#     print(i)

# # TODO: The calendar module provides useful utilities for the given locale
# # For example, you can find out what day of the week it is, where Monday is 0 
# for name in calendar.month_name:
#     print(name)
     
# for day in calendar.day_name:
#     print(day)

# TODO: Calculate days based on a rule: for example, consider
# a team meeting on the first Friday of every month.
# to figure out what dys that would be for each month,
# you can use this script:

print("Team meetings will be on:")
for m in range(1,13):
    cal = calendar.monthcalendar(2026, m)
    weekone = cal[0]
    weektwo = cal[1]
    
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
        
    #print("%10s %2d" % (calendar.month_name[m], meetday))
    print(calendar.month_name[m], meetday)
   