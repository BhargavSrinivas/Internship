# 1Q)https://leetcode.com/problems/search-insert-position/
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         nums_lower = []
#         for i in range(len(nums)):
#             if target == nums[i]:
#                 return i
#         for i in range(len(nums)):
#             if target > nums[i]:
#                 nums_lower.append(nums[i])
#         return len(nums_lower)

# 2Q)https://leetcode.com/problems/linked-list-cycle/
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#             if slow == fast:
#                 return True 
        
#         return False 

# 3Q)https://leetcode.com/problems/intersection-of-two-linked-lists/
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         a = headA
#         b = headB
#         intersectNode = None
#         while a:
#             a.val = str(a.val)
#             a = a.next
#         while b:
#             if type(b.val) == str:
#                 intersectNode = b
#                 break
#             b = b.next
#         a = headA
#         while a:
#             a.val = int(a.val)
#             a = a.next
#         return intersectNode
        
# 
# 4Q)https://leetcode.com/problems/majority-element/
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         candidate = None
#         count = 0

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1
            
#         return candidate

# 5Q)https://leetcode.com/problems/reverse-bits/
# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         bin_num = bin(n).replace("0b", "")
#         reverse_bin = str(bin_num)[::-1]
#         reverse_bin += '0'*(32 - len(reverse_bin))
#         return int(reverse_bin,2)

# 6Q)https://leetcode.com/problems/remove-linked-list-elements/
# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#         # Create a dummy node to simplify removal of the first node
#         dummy = ListNode(0)
#         dummy.next = head
#         left = dummy
#         right = head

#         while right:
#             if right.val == val:
#                 # Skip the current node by updating the next pointer of the previous node
#                 left.next = right.next
#             else:
#                 # Move both left and right pointers to the next nodes
#                 left = left.next
#             right = right.next

#         return dummy.next

# 7Q)https://leetcode.com/problems/reverse-linked-list/
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         curr = head
#         prev = None

#         while curr is not None:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
        
#         return prev

# 8Q)https://leetcode.com/problems/nim-game/
# class Solution(object):
#     def canWinNim(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         return n%4 != 0

# 9Q)https://leetcode.com/problems/is-subsequence/
# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         j = 0
#         for i in range(len(t)):
#             if j >= len(s):
#                 return True
#             elif t[i] == s[j]:
#                 j += 1
#         if j>=len(s):
#             return True
#             return False
        
# 10Q)https://leetcode.com/problems/fizz-buzz/       
# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         out = []
#         for i in range(1,n+1):
#             res = ""
#             if i%3 == 0:
#                 res+="Fizz"
#             if i%5 == 0:
#                 res+="Buzz"
#             if res == "":
#                 res+=str(i)
#             out.append(res)
#         return out
        
# 11Q)https://leetcode.com/problems/construct-the-rectangle/
# class Solution(object):
#     def constructRectangle(self, area):
#         """
#         :type area: int
#         :rtype: List[int]
#         """
       
#         length = int(area ** 0.5)  
#         width = 1

       
#         while length >= 1:
#             if area % length == 0:
#                 width = area // length
#                 break
#             length -= 1

       
#         return [width, length]  

# 12Q)https://leetcode.com/problems/relative-ranks/
# class Solution(object):
#     def findRelativeRanks(self, score):
#         """
#         :type score: List[int]
#         :rtype: List[str]
#         """
#         m = dict(zip(sorted(score,reverse=True),["Gold Medal","Silver Medal","Bronze Medal"]+list(range(4, len(score)+1))))
#         return map(str,[m[n] for n in score])
        
# 13Q)https://leetcode.com/problems/reshape-the-matrix/
# import numpy
# class Solution(object):
#     def matrixReshape(self, mat, r, c):
#         """
#         :type mat: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         return numpy.reshape(mat,(r,c)) if r*c == len(mat)*len(mat[0]) else mat
        
# 14Q)https://leetcode.com/problems/maximum-product-of-three-numbers/
# class Solution(object):
#     def maximumProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
        

# 15Q)https://leetcode.com/problems/set-mismatch/
# class Solution(object):
#     def findErrorNums(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n , a, b= len(nums), sum(nums),sum(set(nums))
#         s = n*(n+1)//2

#         return [a-b,s-b]
        
