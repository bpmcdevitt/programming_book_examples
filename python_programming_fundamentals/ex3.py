#!/usr/bin/env python
# python programming fundamentals
# page 34

# 3. you can keep track of your car's miles per gallon if you keep track of how many miles you drive your car on a tank of gas and you always fill up your tank when getting gas
# write a program that asks the user to enter the number of miles you drove your car and the numbe rof gallons of gas you put in your car and then prints the miles per gallon you 
# got on that tank of gas.

miles = input('How many miles did you drive your car? ')
gallons = input('How much gas did you put into your car? ')

# miles drive / gallons used

mpg = int(miles) / int(gallons) 

print('Here is the total mpg based on those numbers:' + str(mpg))
