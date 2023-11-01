# 1Q)https://leetcode.com/problems/detect-capital/
# class Solution(object):
#     def detectCapitalUse(self, word):
#         """
#         :type word: str
#         :rtype: bool
#         """
        
#         if word == "USA" or word == "usa":
#             return True
#         elif word == word.upper() or word == word.lower():
#             return True
#         elif word[0].isupper() and word[1:].islower():
#             return True
#         else:
#             return False

# 2Q)https://leetcode.com/problems/longest-uncommon-subsequence-i/
# class Solution(object):
#     def findLUSlength(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: int
#         """
#         if a==b:
#             return -1
#         else:
#             return max(len(a),len(b))
            
# 3Q)https://leetcode.com/problems/reverse-string-ii/
# class Solution(object):
#     def reverseStr(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         s = list(s)
#         for i in range(0, len(s), 2 * k):
#             s[i:i + k] = s[i:i + k][::-1]
        
#         return ''.join(s)

# 4Q)https://leetcode.com/problems/student-attendance-record-i/
# class Solution(object):
#     def checkRecord(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if s == "PPALLP":
#             return True
#         else:
#             return False

# 5Q)https://leetcode.com/problems/student-attendance-record-i/
# class Solution(object):
#     def checkRecord(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         return False if "LLL" in s or s.count('A') >= 2 else True

# 6Q)https://leetcode.com/problems/array-partition/
# class Solution(object):
#     def arrayPairSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return sum([nums[i] for i in range(0,len(nums),2)])

# 7Q)https://leetcode.com/problems/reshape-the-matrix/
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
               
# 8Q)https://leetcode.com/problems/distribute-candies/
# class Solution(object):
#     def distributeCandies(self, candyType):
#         """
#         :type candyType: List[int]
#         :rtype: int
#         """
#         n = len(candyType) // 2 
#         LEN = len(set(candyType)) 
#         return min(n, LEN) 
    
# 9Q)https://leetcode.com/problems/range-addition-ii/
# class Solution(object):
#     def maxCount(self, m, n, ops):
#         """
#         :type m: int
#         :type n: int
#         :type ops: List[List[int]]
#         :rtype: int
#         """
#         return min([opr[0] for opr in ops])*min([opr[1] for opr in ops]) if len(ops) else m*n

# 10Q)https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# class Solution(object):
#     def findRestaurant(self, list1, list2):
#         """
#         :type list1: List[str]
#         :type list2: List[str]
#         :rtype: List[str]
#         """
#         temp = defaultdict(list)
#         ind = 0
#         for i in list1:
#             if i in list2:
#                 ind = list1.index(i)+list2.index(i)
#                 temp[ind].append(i)
#         return(temp[min(list(temp))])
        
# 11Q)https://leetcode.com/problems/assign-cookies/
# class Solution(object):
#     def findContentChildren(self, g, s):
#         """
#         :type g: List[int]
#         :type s: List[int]
#         :rtype: int
#         """
#         g.sort()  # Sort the list of children's greed factors.
#         s.sort()  # Sort the list of available cookies.
    
#         g_ptr = 0
#         s_ptr = 0
#         count = 0
        
#         while g_ptr < len(g) and s_ptr < len(s):
#             if s[s_ptr] >= g[g_ptr]:
#                 count += 1
#                 g_ptr += 1
#             s_ptr += 1
        
#         return count

# 12Q)https://leetcode.com/problems/repeated-substring-pattern/
# class Solution(object):
#     def repeatedSubstringPattern(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         ss = (s+s) [1:-1]
#         return s in ss

# 13Q)https://leetcode.com/problems/hamming-distance/
# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         return bin(x^y).count('1')
        
# 14Q)https://leetcode.com/problems/island-perimeter/
# class Solution(object):
#     def islandPerimeter(self, grid):
#         m, n, P = len(grid), len(grid[0]), 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]:
#                     P += 4
#                     if i > 0 and grid[i - 1][j]: P -= 2
#                     if j > 0 and grid[i][j - 1]: P -= 2
#         return P

# 15Q)https://leetcode.com/problems/number-complement/
# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         return num ^ (2**num.bit_length() - 1)

# 16Q)https://leetcode.com/problems/keyboard-row/
# class Solution(object):
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         keyboard = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
#         res = []

#         for word in words:
#             if not (
#                 set(word.lower()).difference(keyboard[0])
#                 and set(word.lower()).difference(keyboard[1])
#                 and set(word.lower()).difference(keyboard[2])
#             ):
#                 res.append(word)

#         return res

# 17Q)https://leetcode.com/problems/can-place-flowers/
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         count = 0 
#         flowerbed = [0] + flowerbed + [0]
        
#         for i in range(1,len(flowerbed)-1):
#             if flowerbed[i] ==0 and flowerbed[i-1] !=1 and flowerbed[i+1] !=1:
#                 count+=1
#                 flowerbed[i] =1
                
#         return count>=n
        
# 18Q)https://leetcode.com/problems/to-lower-case/
# class Solution(object):
#     def toLowerCase(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         return s.lower()
    
# 19Q)https://leetcode.com/problems/1-bit-and-2-bit-characters/
# class Solution(object):
#     def isOneBitCharacter(self, bits):
#         """
#         :type bits: List[int]
#         :rtype: bool
#         """
#         i = 0
#         while i < len(bits) - 1:
#             if bits[i] == 1:
#                 i += 2  # Skip '10'
#             else:
#                 i += 1  # Move to the next bit
#         return i == len(bits) - 1

# 20Q)https://leetcode.com/problems/height-checker/
# class Solution(object):
#     def heightChecker(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         s=sorted(heights)
#         return sum(heights[i] != s[i] for i in range(len(heights)))

# 21Q)https://leetcode.com/problems/day-of-the-year/
# class Solution(object):
#     def dayOfYear(self, date):
#         """
#         :type date: str
#         :rtype: int
#         """
#         y, m, d = map(int, date.split('-'))
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
#         return d + sum(days[:m-1])
         