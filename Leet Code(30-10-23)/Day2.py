#1Q) https://leetcode.com/problems/length-of-last-word/
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         last=s.split()
#         m=len(last)
#         n=len(last[m-1])
#         return n

# 2Q)https://leetcode.com/problems/sqrtx/
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         return int(floor(sqrt(x)))

#3Q)https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def hasPathSum(self, root, targetSum):
#         """
#         :type root: TreeNode
#         :type targetSum: int
#         :rtype: bool
#         """
#         if not root:
#             return False

#         if not root.left and not root.right and root.val == targetSum:
#             return True
        
#         targetSum -= root.val

#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# 4Q)https://leetcode.com/problems/pascals-triangle/
# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         result = []
#         for i in range(numRows):
#             row = [1] * (i + 1)
#             for j in range(1, i):
#                 row[j] = result[i - 1][j] + result[i - 1][j - 1]
#             result.append(row)
#         return result

# 5Q)https://leetcode.com/problems/single-number/
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         uniqNum = 0;
#         for i in nums:
#             uniqNum ^= i;
#         return uniqNum;

# 6Q)https://leetcode.com/problems/move-zeroes/
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         i = 0
#         for j in range(n):
#             if (nums[j] != 0):
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1

# 7Q)https://leetcode.com/problems/power-of-three/
# class Solution(object):
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n <= 0:
#             return False

#         while n % 3 == 0:
#             n //= 3

#         return n == 1

# 8Q)https://leetcode.com/problems/power-of-four/
# class Solution(object):
#     def isPowerOfFour(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n <= 0:
#             return False

#         while n % 4 == 0:
#             n //= 4

#         return n == 1

# 9Q)https://leetcode.com/problems/reverse-vowels-of-a-string/        
# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         vowels = re.findall('(?i)[aeiou]', s)
#         return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

# 10Q)https://leetcode.com/problems/intersection-of-two-arrays/
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         return set([value for value in nums1 if value in nums2])

# 11Q)https://leetcode.com/problems/intersection-of-two-arrays-ii/
# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         ans=[]
#         for i in nums1:
#             if i in nums2:
#                 ans.append(i)
#                 nums2.remove(i)
#         return ans
        
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# 12Q)https://leetcode.com/problems/guess-number-higher-or-lower/
# class Solution(object):
#     def guessNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         low = 1
#         high = n
#         while low <= high:
#             mid = (low + high)//2
#             res =  guess(mid)
#             if res == 0 :
#                 return mid
#             elif res == -1:
#                 high = mid - 1
#             else:
#                 low = mid + 1

# 13Q)https://leetcode.com/problems/find-the-difference/
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         if len(s)>len(t):
#             for i in s:
#                 if s.count(i)>t.count(i):
#                     return(i)
#                     break
#         if len(t)>len(s):
#             for i in t:
#                 if t.count(i)>s.count(i):
#                     return(i)
#                     break

# 14Q)https://leetcode.com/problems/rotate-string/
# class Solution(object):
#     def rotateString(self, s, goal):
#         """
#         :type s: str
#         :type goal: str
#         :rtype: bool
#         """
#         if len(s) != len(goal):
#             return False

#         s += s  

#         if goal in s:
#             return True
#         else:
#             return False

# 15Q)https://leetcode.com/problems/merge-sorted-array/        
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         i, j, k = m - 1, n - 1, m + n - 1

#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1

        
#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 16Q)https://leetcode.com/problems/same-tree/
# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q 

# 17Q)https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         max_profit,min_price = 0, float('inf')
#         for price in prices:
#             min_price = min(min_price,price)
#             profit = price-min_price
#             max_profit = max(max_profit,profit)
#         return max_profit

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 18Q)https://leetcode.com/problems/binary-tree-paths/
# class Solution(object):
#     def binaryTreePaths(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         if not root: return []
#         result= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.left)]
#         result+= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.right)]
#         return result or [str(root.val)]     



# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 19Q)https://leetcode.com/problems/first-bad-version/
# class Solution(object):
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         def search(low, high):
#             while low < high:
#                 mid = (low + high) // 2
#                 if not isBadVersion(mid):
#                    low = mid + 1
#                 else:
#                     high = mid
#             return low
#         return search(1, n)
        
# 20Q)https://leetcode.com/problems/word-pattern/
# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         s = s.split()
#         return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s))) and len(pattern) == len(s)

# 21Q)https://leetcode.com/problems/ransom-note/
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         for i in set(ransomNote):
#             if magazine.count(i) < ransomNote.count(i):
#                 return False
#         return True
        
# 22Q)https://leetcode.com/problems/first-unique-character-in-a-string/
# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 return i
#         return -1
        
# 23Q)https://leetcode.com/problems/longest-palindrome/
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         return min(sum(count - (count % 2) for count in collections.Counter(s).values()) + 1, len(s))        

# 24Q)https://leetcode.com/problems/third-maximum-number/
# class Solution(object):
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return max(nums) if len(set(nums)) < 3 else sorted(list(set(nums)))[-3]

# 25Q) https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         return set(range(1, len(nums)+1)) - set(nums)


