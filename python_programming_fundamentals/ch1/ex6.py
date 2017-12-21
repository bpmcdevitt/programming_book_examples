#!/usr/bin/env python
# python programming fundamentals
# chapter 1 - page 34 - ex6

#6. write a program that computes the minimum number of bills and coins needed to make change for a person. For instance, if you need to give $34.36 in change you would need one twenty, one ten, four ones, a quarter, a dime, and a penny. You don't have to compute change for bills greater than $20 dollar bills or for fifty cent pieces. You can solve this problem by doing division, multiplication, subtraction, and converting floats to ints when appropriate. So when you run the program it should look exactly like this:
# How much did the item cost: 65.64
# How much did the person give you: 100.00
# The person's change is $34.36
# The bills or the change should be:
# 1 twenties
# 1 tens
# 0 fives
# 4 ones
# 1 quarters
# 1 dimes
# 0 nickels
# 1 pennies

cost = float(input('How much did the item cost: '))
amt_given = float(input('How much did the person give to you: '))

# dictionary mapping bill/coin name to currency value
bills = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25, 'one': 1.00, 'five': 5.00, 'ten': 10.00, 'twenty': 20.00}

# compute the change
change = float(amt_given - cost)

# conditional to test each if each dict value goes into the total # of change
