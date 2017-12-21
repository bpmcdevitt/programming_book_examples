#!/usr/bin/env python
# python programming fundamentals
# page 33
# 1.19 excercise #2

# 2. write a program that capitalizes the first four characters of a string by converting their characters to their ASCII equivlaent , then adding the necessary amount to capitlize them , and converting the integers back to characters. Print the capitalized string.

# the developers of ascii made the 6th bit be a 0 for the upper case and a 1 for lower case. here is an example
#A - 01000001 or 65 in dec
#a - 01100001 or 65(+32) in dec = 97

# so subtract or add 32 depending on if you wanna go lower --> upper or vice versa and it is the equivalent to flipping the 6th bit. 

name = input('Enter your name in lowercase: ')
print('\n')
# store the integers in a list so we don't have to rewrite the same code
name_ascii_list_l= [int(ord(name[0])), int(ord(name[1])), int(ord(name[2])), int(ord(name[3]))]

print('lower case:')

# print lower case decimal ascii value
print(name[0] + ' ' + 'ASCII value is ' + str(name_ascii_list_l[0]))
print(name[1] + ' ' + 'ASCII value is ' + str(name_ascii_list_l[1]))
print(name[2] + ' ' + 'ASCII value is ' + str(name_ascii_list_l[2]))
print(name[3] + ' ' + 'ASCII value is ' + str(name_ascii_list_l[3]))
print('\n')

# now convert to upper case. again we store values in a list. 
name_ascii_list_u = [name_ascii_list_l[0] - 32, name_ascii_list_l[1] - 32, name_ascii_list_l[2] - 32, name_ascii_list_l[3] - 32]

print ('upper case:')

print(chr(name_ascii_list_u[0]) + ' ' + 'ASCII value is ' + str(name_ascii_list_u[0]))
print(chr(name_ascii_list_u[1]) + ' ' + 'ASCII value is ' + str(name_ascii_list_u[1]))
print(chr(name_ascii_list_u[2]) + ' ' + 'ASCII value is ' + str(name_ascii_list_u[2]))
print(chr(name_ascii_list_u[3]) + ' ' + 'ASCII value is ' + str(name_ascii_list_u[3]))
