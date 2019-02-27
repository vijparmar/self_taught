'''
Author: Vijay Parmar
Date: 2/25/19
Description: Create a dictionary that contains different
             attributes about you: height, favorite color,
             favorite author, etc.
'''

Me = {"Height": "5.7",
      "Weight": "150",
      "Favorite color":"Black",
      "Author":"Ayn Rand"
      }

question = input("Ask me about my height, Weight, Favorite color or Author : ")

if question in Me:
    answer = Me[question]
    print(answer)
else:
    print("Invalid question")

