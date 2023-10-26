
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