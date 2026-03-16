#
# Example file for the challenge on dates and times
# LinkedIn Learning Python course
#

#from calendar import calendar


def count_days(theyear, themonth, whichday):
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

def main():
    testyear = 2025
    testmonth = 12
    testday = 0
    result = count_days(testyear, testmonth, testday)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    