''' 
Author: Vijay Parmar
Date: 2/17/19
Description: Write a program with two functions. The first function should take an integer as a parameter
and return the result of the integer divided by 2. The second function should take an integer
as a parameter and return the result of the integer multiplied by 4. Call the first function, save
the result as a variable, and pass it as a parameter to the second function.
'''

def func1(x):
    try:
       return x/2
    except ZeroDivisionError:
        print("b cannot be zero.")
    except ValueError:
        print("Input has to be number")

def func2(y):
    print(y*2)

a = input("Enter an integer: ")
a = int(a)
b = func1(a)
func2(b)

