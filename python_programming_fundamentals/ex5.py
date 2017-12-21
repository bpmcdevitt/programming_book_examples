#!/usr/bin/env python
# python fundamentals
# ex5.py
# page 34

# 5. Write a program that converts centimeters to yards, feet, and inches. There are 2.54cm in an inch. You can solve this problem by doing division, multiplication, addition, and subtraction. Converting a float to an int at the appropriate time will help in solving this problem. When you run the program, it should look exactly like this(except possibly for decimal places in the inches):

# How many centimeters do you want to convert? 127.25
# This is 1 yards, 1 feet, 2.098425 inches.

cm_per_inch = 2.54

total_cm = float(input('How many centimers do you want to convert? '))
inches = float(total_cm/cm_per_inch)

# 36 inches in 1 yard
yard = int(inches/36)

# 3 feet in 1 yard
feet = int(yard/3)

print("This is {0} yards, {1} feet, {2} inches." .format(yard, feet, inches))
