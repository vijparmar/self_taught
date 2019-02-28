'''
Author: Vijay Parmar
Date: 2/27/19
Description: Write a program with an infinite loop (with the option to type q to quit)
             and a list of numbers. Each time through the loop ask the user to guess a
             number on the list and tell them whether or not they guessed correctly.
'''

number = [1,3,5,7,9,11,13,17]

while True:
    a = input("please type a number or q to quit: ")
    if a == "q":2
        break
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
    if a in number:
        print("you guessed it correctly")
    else:
        print("You guessed incorrectly")



