'''
Author: Vijay Parmar
Date: 2/25/19
Description: Take the list ["The", "fox", "jumped", "over", "the", "fence",
             "."] and turn it into a grammatically correct string.
             There should be a space between each word, but no space
             between the word fence and the period that follows it.
             (Don't forget, youlearned a method that turns a list of
             strings into a single string.)
'''


lst =["The", "fox", "jumped", "over", "the", "fence","."]

str = " ".join(lst)

str=str.replace(" .",".")

print(str)
