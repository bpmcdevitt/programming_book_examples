#!/usr/bin/env python
# ex4.py
# python programming fundamentals - page34

# 4. Write a program that converts US dollars to a Foreign Currency. You can do this by finding the exchange rate on the internet and then prompting for the exchange rate in your program. It should look exactly like this:
# What is the amount of US Dollars you wish to convert? 31.67
# What is the current exchange rate
# (1 US Dollar equals what in the Foreign Currency)? 0.9825
# The amount in the Foreign Currency is $31.12

usd = input('What is the amount of US Dollars you wish to convert? ')
exchange_rate = input('(1 US Dollar equals what in the Foreign Currency?) ' )

# formula is total usd / exchange rate. we need to make sure usd is represented as a float to do the math correctly.

conversion = float(usd) / float(exchange_rate)
print(conversion)
