# 1Q)https://leetcode.com/problems/summary-ranges/
# class Solution(object):
#     def summaryRanges(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         ranges = []
#         for n in nums:
#             if not ranges or n > ranges[-1][-1] + 1:
#                 ranges += [],
#             ranges[-1][1:] = n,
#         return ['->'.join(map(str, r)) for r in ranges]

# 2Q)https://leetcode.com/problems/valid-anagram/
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        
#         s = s.replace(" ", "").lower()
#         t = t.replace(" ", "").lower()
        
        
#         return sorted(s) == sorted(t)

# 3Q)https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# class Solution(object):
#     def toHex(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         return "{0:x}".format(num) if num >= 0 else "{0:x}".format(num + 2 ** 32)
        
# 4Q)https://leetcode.com/problems/teemo-attacking/
# class Solution(object):
#     def findPoisonedDuration(self, timeSeries, duration):
#         if not timeSeries:
#             return 0
#         total_duration = duration  # Initialize with the first duration

#         for i in range(1, len(timeSeries)):
#             if timeSeries[i] < timeSeries[i-1] + duration:
#                 total_duration += timeSeries[i] - timeSeries[i-1]
#             else:
#                 total_duration += duration

#         return total_duration
    
# 5Q)https://leetcode.com/problems/find-the-town-judge/
# class Solution(object):
#     def findJudge(self, n, trust):
#         """
#         :type n: int
#         :type trust: List[List[int]]
#         :rtype: int
#         """
#         count = [0] * (n + 1)
        
#         for i, j in trust:
#             count[i] -= 1
#             count[j] += 1
            
#         for i in range(1, n + 1):
#             if count[i] == n - 1:
#                 return i
            
#         return -1

# 6Q)https://leetcode.com/problems/find-common-characters/
# class Solution(object):
#     def commonChars(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         ans = Counter(words[0])
#         for i in range (1,len(words)):
#             ans &= Counter(words[i])
#         return ans.elements()
    
# 7Q)https://leetcode.com/problems/complement-of-base-10-integer/
# class Solution(object):
#     def bitwiseComplement(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 1  # Special case: The complement of 0 is 1.
        
#         # Step 1: Convert to binary and remove the '0b' prefix.
#         binary_str = bin(n)[2:]
    
#         # Step 2: Invert each bit (complement).
#         complemented_str = ''.join(['1' if bit == '0' else '0' for bit in binary_str])
    
#         # Step 3: Convert back to base-10 integer.
#         complement = int(complemented_str, 2)
    
#         return complement

# 8Q)https://leetcode.com/problems/day-of-the-week/
# import datetime
# class Solution(object):
#     def dayOfTheWeek(self, day, month, year):
#         """
#         :type day: int
#         :type month: int
#         :type year: int
#         :rtype: str
#         """
#         input_date = datetime.date(year,month,day)
#         day_of_week = input_date.strftime('%A')

#         return day_of_week

# 9Q)https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# from collections import Counter

# class Solution(object):
#     def countCharacters(self, words, chars):
#         """
#         :type words: List[str]
#         :type chars: str
#         :rtype: int
#         """
#         def cnt(word):
#             # Count the occurrences of each character in the word
#             return Counter(word)

#         return sum(not (cnt(w) - cnt(chars)) and len(w) for w in words)

# 10Q)https://leetcode.com/problems/prime-arrangements/
# class Solution(object):
#     def numPrimeArrangements(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         k=len([x for x in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] if x<=n])
#         return (factorial(k)*factorial(n-k))%(10**9+7)

# 11Q)https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# class Solution(object):
#     def luckyNumbers (self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})
    
# 12Q)https://leetcode.com/problems/merge-strings-alternately/
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         word3 = ""

#         p = 0
#         while p < len(word1) or p < len(word2):
#             if p < len(word1):
#                 word3 += word1[p]
#             if p < len(word2):
#                 word3 += word2[p]
#             p += 1
        
#         return word3
