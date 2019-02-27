'''
Author: Vijay Parmar
Date: 2/25/19
Description: Slice the string "It was a bright cold day in April,
             and the clocks were striking thirteen." to only include
             the characters before the comma.
'''

str = "It was a bright cold day in April, and the clocks were striking thirteen."

str=str[:str.index(",")]

print(str)

