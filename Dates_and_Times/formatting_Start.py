#
# Example file for formatting time and date output
# LinkedIn Learning Python course
#

from datetime import datetime

def main():
    # Time and dates can be formatted using a set of predefined string control codes
    now = datetime.now()
    print("The current date and time is ", now)
    
    
    
    #### Date formatting ####
    
    # %y%Y - Year, %a/%A - weekday, %b/%B - month name, %d - day of month
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("Today is: %a, %d %B, %y"))
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))
    #### Time formatting ####
      
    # %I/%H - 12/24 hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    
    
    # You can even include literal characters in the output by escaping them with a percentage sign
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("Current time: %H:%M"))




if __name__ == "__main__":
    main()
    