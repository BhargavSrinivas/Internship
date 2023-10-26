# # # class Solution(object):
# # #     def isPalindrome(self, x):
# # #         if x<0:
# # #             return False

# # #         empty = []

# # #         while x > 0:
# # #             x, remd = divmod(x, 10)
# # #             empty.append(remd)

# # #         a=empty[::-1]
# # #         if a==empty:
# # #             return True
        
# # #         else:
# # #             return False
        
# # class Solution:
# #     def romanToInt(self, s: str) -> int:
# #         translations = {
# #             "I": 1,
# #             "V": 5,
# #             "X": 10,
# #             "L": 50,
# #             "C": 100,
# #             "D": 500,
# #             "M": 1000
# #         }
# #         number = 0
# #         s = s.replace("IV", "IIII").replace("IX", "VIIII")
# #         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
# #         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
# #         for char in s:
# #             number += translations[char]
# #         return number



# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         return str(int(num1)+int(num2))
    

# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         return mod(num, 9) or min(num, 9)

# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         s=list(s)
#         for i in range(0,len(s),2*k):
#             if len(s[i:i+k])<k:
#                 s[i:i+k]=s[i:i+k][::-1]
#             elif 2*k>len(s[i:i+k])>=k:
#                 s[i:i+k]=s[i:i+k][::-1]
#         return "".join(s)
    
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         nums[:] = [x for x in nums if x != val]
#         return len(nums)
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val

# class Solution(object):
#     def subtractProductAndSum(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         product = 1
#         sum = 0
#         while n > 0:
#             digit = n % 10
#             product *= digit
#             sum += digit
#             n //= 10
#         return product - sum
    
l1= [2,4,3]
l2= [1,4,7]
c= int(l1)+int(l2)
print(c)        
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
    
    
prev = None

while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            return prev