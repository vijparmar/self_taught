'''
Author: Vijay Parmar
Date: 2/25/19
Description: Write a program that collects two strings from a user,
            inserts them into the string "Yesterday I wrote a [response_one].
            I sent it to [response_two]!" and prints a new string..
'''

n1 = input("Enter first word: ")
n2 = input("Enter second word: ")

r = """Yesterday I wrote a {}. I sent it to {}
    """.format(n1,n2)

print(r)
