#
# Example file for working with timedelta objects
#   LinkedIn Learning Python course
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))


# TODO: print today's date
# now 


### How many days until April fools day?
today = date.today()
afd = date(today.year, 4, 1)

# TODO: Use date comparision to see if April Fool's day has already gone for this year
# if it has use the replace() function to get the date for next year

if afd < today:
    print("April Fool's day already went by %d days ago" % ((today - afd).days))
    afd = afd.replace(year=today.year + 1)
    

# TODO: Calculate the amount of time until April Fool's day
time_to_afd = afd - today
print("It is :", time_to_afd, "days until April Fool's day.") 