# 1Q)Find the length of the last word in a given sentence.
# a = "Hello World"
# class Solution(object):
#     def lengthoflastword(self,a):
#         last = a.split
#         m = len(last)
#         n = len([m-1])

# 2Q) Find the square root of a given number.
# import math
# x = int(input("Enter a number: "))
# math.sqrt(x)
# print(math.sqrt(x))

# 3Q)Determine if there is a path in a binary tree with the given sum.

# 4Q) Generate the first few rows of Pascals triangle.
# class Solution(object):
#     def generate(self, numRows):
#         result = []
#         for i in range(numRows):
#             row = [1] * (i + 1)
#             for j in range(1, i):
#                 row[j] = result[i - 1][j] + result[i - 1][j - 1]
#                 result.append(row)
#         return result
        
# 5Q)Find the single number in a list of integers.
# num = [2,2,1,1,3,3,4]
# class Solution(object):
#     def singlenumberinlist(self,num):
#         uniqNum = 0;
#         for i in num:
#             uniqNum ^= i;
#         return uniqNum

# 6Q)Move all the zeroes to the end of an array.
# class Solution(object):
#     def moveZeroes(self, nums):
#         n = len(nums)
#         j = 0
#         for i in range(n):
#             if (nums[i] != 0):
#                 nums[i],nums[j] = nums[j],nums[i]
#                 j += 1

# 7Q)Check if a given number is a power of three
# n = 9
# class Solution(object):
#     def ispowerOfThree(self,n):
#         if n<=0:
#             return False
#         while n%3 == 0:
#             n //=3        
#         return n == 1

# 8Q)Check if a given number is a power of four.
# n = 16
# class Solution(object):
#     def ispowerOfFour(self,n):
#         if n<=0:
#             return False
#         while n%4 == 0:
#             n //=4
#       return n ==1

# 9Q)Reverse the vowels in a string.
# s = "hello"
# def reverse_vowels(s):
#     vowels = "aeiouAEIOU"
#     s = list(s)
#     left, right = 0, len(s) - 1

#     while left < right:
#         while s[left] not in vowels and left < right:
#             left += 1
#         while s[right] not in vowels and left < right:
#             right -= 1

#         s[left], s[right] = s[right], s[left]
#         left, right = left + 1, right - 1

#     return ''.join(s)
                
# 10Q) Find intersection of two arrays
# num1 = [1,2,2,1]
# num2 = [2,2]
# class Solution(object):
#     def intersection(self,num1,num2):
#         return set([value for value in num1 if value in num2])

# 11Q)Find the intersection of two arrays with duplicates
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
# def intersection_with_duplicates(nums1, nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)

#     intersection = set1 & set2
#     intersection_list = list(intersection)
    
#     return intersection_list

# result = intersection_with_duplicates(nums1, nums2)
# print(result)

#12Q)Guess a number between 1 and 10
# import random
# secret_number = random.randint(1, 10)
# guess = int(input("Guess a number between 1 and 10: "))

# if guess == secret_number:
#     print(" You guessed the correct number.")
# else:
#     print(f"Sorry, the correct number was {secret_number}.")

#13Q)Find the extra character in a string compared to another string.
# string1 = "abcd"
# string2 = "abcde"
# class Solution(object):
#     def find_extra_character(string1,string2):
#         return (set(string2) - set(string2)).pop()
# extra_char = Solution.find_extra_character(string1, string2)
# print(extra_char)    
    
# 14Q)Check if a string can be rotated to another string.
# s = "waterbottle"
# s1 = "erbottlewat"
# class Solution(object):
#      def rotatestring(self,s,s1):
#         if len(s) != len(s1):
#             return False   
#         s += s  
#         if s1 in s:
#             return True
#         else:
#             return False

# 15Q)Merge two sorted arrays.
# list1 = [1,3,5]
# list2 = [2,4,6]
# class Solution(object):
#     def mergetwolists(self,list1,list2):
#         if list1 and list2:
#             if list1.val > list2.val:
#                 list1,list2 = list2,list1
#             list1.next = self.mergetwolists(lis1.next,list2)
#         return list1 or list2

