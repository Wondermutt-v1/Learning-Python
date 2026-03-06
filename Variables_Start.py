#
# Example file for variables
# LinkedIn Learning Python course
#

# Basic data types in Python: Numbers, strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [ 0,1, "two",3.2, False]
mytuple = (0,1,2)
mydict = {"one" :1, "two":2}

# print(myInt)
# print(myFloat)
# print(myStr)
# print(myBool)
# print(myList)
# print(myTuple)
# print(myDict)
# 
# 
# # re-declaring a variable works
# 
# myInt = "abc"
# print(myInt)
# 
# # to access a member of a sequence type, use[]
# print(myList[2])
# print(myTuple[1])
# 
# 
# # use slices to get parts of a sequence
# print(myList[1:5])
# print(myList[1:5:2])
# 
# # you can use slices to revers a sequence
# print(myList[::-1])

# dictionaries are accessed via keys
# print(myDict["one"])
# ERROR: variables of different types cannot be combined
# print("string type" + 123)
print("string type" + str(123))
# Global vs local variables in functions
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)
    
someFunction()
print(mystr)

del mystr
print(mystr)
