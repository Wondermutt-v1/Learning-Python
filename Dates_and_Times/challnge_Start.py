#
# Example file for the challenge on dates and times
# LinkedIn Learning Python course
#


import calendar
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

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


def count_days(year, month, day):
    if week[whichday] != 0:
        daycnt += 1
return daycnt