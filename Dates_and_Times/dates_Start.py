#
# Example file for working with date information
# LinkedIn Learning Python course
#

from datetime import date
from datetime import time
from datetime import datetime

def main():

## Date Objects
# TODO: Get todays date from the simple today() method for the date class
    today = date.today()
    print("Today's date is ", today)

# # TODO: print out the date"s individual components
#     print("Date components:", today.year, today.month, today.day)

# # TODO: retrieve todays weekday (0=Monday, 6=Sunday)
#     print("Today's weekday:", today.weekday())
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     print("Which is a ", days[today.weekday()]) 

## Datetime Objects
# TODO: Get todays date from the datetime class
    today = datetime.now()
    print("The current date and time is ", today)
    
# TODO: Get the current time
    t= datetime.time(datetime.now())
    print("The current time is ", t)


if __name__ == "__main__":
    main()
    