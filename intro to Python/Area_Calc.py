#
# intro to Python - Programming and Python
# Area_Calc.py
#

import math



a = 3
b = 4
# c = 5
c = 4

s =(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

# area = round(area,2) # round the area to 2 decimal places
# print("The area of the triangle is:", area)
print("The area of the triangle is:", round(area, 2))

# def area_of_circle(radius):
#     area = 3.14 * radius ** 2
#     return area

# def area_of_rectangle(length, width):
#     area = length * width
#     return area

# def area_of_triangle(base, height):
#     area = 0.5 * base * height
#     return area

# def area_of_square(side):
#     area = side ** 2
#     return area 


# def area_of_trapezoid(base1, base2, height):
#     area = 0.5 * (base1 + base2) * height
#     return area


# def area_of_parallelogram(base, height):
#     area = base * height
#     return area

# def area_of_ellipse(a, b):
#     area = 3.14 * a * b
#     return area


# def main():
#     r =float(input("Enter the radius of the circle: "))
#     # b1 = float(input("Enter the length of the first base of the trapezoid: "))
#     # b2 = float(input("Enter the length of the second base of the trapezoid: "))
#     # h = float(input("Enter the height of the trapezoid: "))
#     # b= float(input("Enter the base of the parallelogram: "))
#     # h1 = float(input("Enter the height of the parallelogram: "))   
#     print("The area of the circle is:", area_of_circle(r))
    
    
    
# if __name__ == "__main__":
#     main() 