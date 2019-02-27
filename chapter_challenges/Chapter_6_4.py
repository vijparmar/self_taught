'''
Author: Vijay Parmar
Date: 2/25/19
Description: Take the string "Where now? Who now? When now?"
             and call a method that returns a list that looks
             like: ["Where now?", "Who now?", "When now?"].
'''


lst ="Where now? Who now? When now?".split("? ")

lst[0]=lst[0]+"?"
lst[1]=lst[1]+"?"

print(lst)

