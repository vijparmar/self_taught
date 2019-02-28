'''
Author: Vijay Parmar
Date: 2/27/19
Description: Create a module named cubed with a function that takes a number as a parameter, and
returns the number cubed.
'''

def cubed(x):
    try:
        x=int(x)
        y = x**3
        return y
    except ValueError:
        print("Invalid number")



