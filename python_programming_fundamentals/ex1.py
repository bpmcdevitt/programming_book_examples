#!/usr/bin/env python
# python programming fundamentals
# page 33
# 1.19 excercise #1

# 1. write a program that asks the user to enter their name. Then it should print out the ASCII equivalent of each of the first four characters of your name. For instance, here is a sample run of the program below:
# Please enter your name: Kent
# K ASCII value is 75
# e ASCII value is 101
# n ASCII value is 110
# t ASCII value is 116

name = input('Enter your name: ')

print(name[0] + ' ' + 'ASCII value is ' + str(ord(name[0])))
print(name[1] + ' ' + 'ASCII value is ' + str(ord(name[1]))) 
print(name[2] + ' ' + 'ASCII value is ' + str(ord(name[2])))
print(name[3] + ' ' + 'ASCII value is ' + str(ord(name[3])))
