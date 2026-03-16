#
# Example file for the challenge on dates and times
# LinkedIn Learning Python course
#

from calendar import calendar


def count_days(theyear, themonth, theday):
    import calendar
    daycnt = 0
    weeklist = calendar.monthcalendar(theyear,themonth)
# monthcalendar returns an array of week lists, like this:
# [
# [0, 0, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1],  
# [1, 1, 1, 1, 1, 1, 1], 
# [1,1,1,0,0,0,0]
#   ]


    for week in weeklist:
        if week[whichday] != 0:
        daycnt += 1
        return daycnt