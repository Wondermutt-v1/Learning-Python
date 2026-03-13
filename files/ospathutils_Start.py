#
# Example file for working with os.path module
# LinkedIn Learning Python course
#

from genericpath import getmtime
import os
from os import path
import datetime
from datetime import date
import time



def main():
    # #print the name of the OS
    # print(os.name)
    
    # # Check for item existence and type
    # print("Item exists:", path.exists("textfile.txt"))
    # print("Item is a file:", path.isfile("textfile.txt"))
    # print("Item is a directory:", path.isdir("textfile.txt"))
    
    # # Work with file paths
    # print("Item path:", path.realpath("textfile.txt"))
    # print("Item path and name:", path.split(path.realpath("textfile.txt")))
    
    # Get the modification time
    t = time.ctime(getmtime("textfile.txt"))
    print("Modification time:", t)
    print((datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))))

    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been ",td, " since the file was modified")
    print("Or,", td.total_seconds(), "seconds")
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()