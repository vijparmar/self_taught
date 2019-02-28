'''
Author: Vijay Parmar
Date: 2/27/19
Description: Multiply all the numbers in the list [8, 19, 148, 4]
             with all the numbers in the list [9, 1, 33, 83], and
             append each result to a third list.
'''

nums1 = [8, 19, 148, 4]
nums2 = [9, 1, 33, 83]
mult = []

for i in nums1:
    for j in nums2:
        mult.append(i*j)
print(mult)


