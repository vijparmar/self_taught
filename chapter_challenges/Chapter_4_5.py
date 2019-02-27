''' 
Author: Vijay Parmar
Date: 2/17/19
Description: Write a function that converts a string to a float and returns the result. Use exception
handling to catch the exception that could occur.
'''

def string_conv():
    try:
       n = input("type a number:")
       print(float(n))
    except ValueError:
        print("Input has to be number")

string_conv()

