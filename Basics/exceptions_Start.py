#
# Example file for working with classes
# LinkedIn Learning Python course
#

# Errors can happen in programs and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero
# x = 10/0

#TODO exceptions provide a way of catching errors and then handling them in a clean way
# a separate section of the code to group them together
# try:
#     x = 10/0
# except:
#     print("well that didn't work")
    
# TODO You can also catch specific exceptions
try:
    answer = input("What should I divide 10 by? ")
    num =   int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("Can't divide by zero")
except ValueError as e:
    print("You didn't give a valid number")
    print(e)
finally:
    print("This code alwys runs")
