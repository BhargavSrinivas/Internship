# 1Q)https://leetcode.com/problems/two-sum/
# class Solution(object):
#     def twoSum(self, nums, target):
#         a = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     a.append(i)
#                     a.append(j)
#                     return a

# 2Q)https://leetcode.com/problems/roman-to-integer/
# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sum = 0
#         current_value = 0
#         roman_char_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
#         for char in reversed(s):
#             num = roman_char_to_int[char]
            
#             if current_value > num:
#                 sum -= num
#             else:
#                 sum += num

#             current_value = num
            
#         return sum

# 3Q)https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0

#         unique_idx = 0  # Index for unique elements

#         for i in range(1, len(nums)):
#             if nums[i] != nums[unique_idx]:
#                 unique_idx += 1
#                 nums[unique_idx] = nums[i]

#         return unique_idx + 1

# 4Q)https://leetcode.com/problems/plus-one/
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         num = 0

#         for digit in digits:
#             num = num * 10 + digit

#         num += 1

#         result = []
#         while num > 0:
#             result.insert(0, num % 10)
#             num //= 10

#         return result

# 5Q)https://leetcode.com/problems/climbing-stairs/
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         first,second = 1,1
#         for i in range (2,n+1):
#             first,second = second , first+second
#         return second

# 6Q)https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         slow = fast = head

#         if head == None:
#             return head

#         while fast:
#             while fast and slow.val == fast.val:
#                 fast = fast.next
#             slow.next = fast
#             slow = fast

#         return head
        
# 7Q)https://leetcode.com/problems/binary-tree-inorder-traversal/
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root is None:
#             return[]
#         return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)


# 8Q)https://leetcode.com/problems/symmetric-tree/description/
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True

#         def isMirror(left, right):
#             if not left and not right:
#                 return True
#             if not left or not right:
#                 return False

#             return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

#         return isMirror(root.left, root.right)

# 9Q)https://leetcode.com/problems/valid-palindrome/
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         filter = ''.join([i.lower() for i in s if i.isalnum()])
#         return filter == filter[::-1]

# 10Q)https://leetcode.com/problems/number-of-1-bits/
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ans = 0
#         while(n):
#             ans+=n%2
#             n//=2
#         return ans
                
# 11Q)https://leetcode.com/problems/happy-number/
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         def get_next(n):
#             # Calculate the sum of the squares of digits
#             total_sum = 0
#             while n > 0:
#                 n, digit = divmod(n, 10)
#                 total_sum += digit**2
#             return total_sum
        
#         seen = set()
#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = get_next(n)
        
#         return n == 1

# 12Q)https://leetcode.com/problems/isomorphic-strings/description/
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         zipped_set = set(zip(s, t))
#         return len(zipped_set) == len(set(s)) == len(set(t))

# 13Q)https://leetcode.com/problems/contains-duplicate/
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         seen = set()
        
#         for num in nums:
            
#             if num in seen:
#                 return True
#             seen.add(num)
        
#         return False

# 14Q)https://leetcode.com/problems/contains-duplicate-ii/
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         seen = set()
        
#         for i, num in enumerate(nums):
#             if num in seen:
#                 return True
#             seen.add(num)
            
#             # Keep the set size limited to k
#             if len(seen) > k:
#                 seen.remove(nums[i - k])
        
#         return False

# 15Q) https://leetcode.com/problems/count-complete-tree-nodes/
# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0

#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# 16Q)https://leetcode.com/problems/counting-bits/
# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         return [list(str(bin(i))).count("1") for i in range(0, n + 1)]

# 17Q)https://leetcode.com/problems/valid-perfect-square/
# class Solution(object):
#     def isPerfectSquare(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         ans = num**0.5
#         if int(ans) == ans:
#             return True
#         return False
        
# 18Q)https://leetcode.com/problems/number-of-segments-in-a-string/
# class Solution(object):
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         segments = s.split()

#         non_empty_segments = [segment for segment in segments if segment]  # Filter out empty segments
#         return len(non_empty_segments)  # Return the count of non-empty segments

# 19Q)https://leetcode.com/problems/longest-common-prefix/
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""  # If the list is empty, there is no common prefix

#         # Find the shortest string in the list
#         min_str = min(strs, key=len)
        
#         for i, char in enumerate(min_str):
#             for string in strs:
#                 if string[i] != char:
#                     return min_str[:i]
        
#         return min_str  # If no mismatch is found, the entire min_str is the common prefix

# 20Q)https://leetcode.com/problems/valid-parentheses/ 
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         bracket_pairs = {')': '(', '}': '{', ']': '['}

#         for char in s:
#             if char in bracket_pairs.values():
#                 stack.append(char)
#             elif char in bracket_pairs:
#                 if not stack or stack.pop() != bracket_pairs[char]:
#                     return False

#         return not stack  # If the stack is empty at the end, all brackets are matched

# 21Q)https://leetcode.com/problems/pascals-triangle-ii/
# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         a = [0] * (rowIndex + 1)
#         a[0] = 1

#         for i in range(1, rowIndex + 1):
#             for j in range(i, 0, -1):
#                 a[j] = a[j] + a[j - 1]

#         return a

# 22Q)https://leetcode.com/problems/binary-tree-postorder-traversal/
# class Solution(object):
#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         s=[]
#         def postorder(root):
#             if not root:
#                 return root
#             else:
#                 postorder(root.left)
#                 postorder(root.right)
#                 s.append(root.val)
#         postorder(root)
#         return s
        
                