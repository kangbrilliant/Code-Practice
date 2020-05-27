
# 2. center diffusion
class Solution:
    # time cost: o(n^2)
    # space cost: o(1)
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        max_str = s[0]
        max_len = 1
        for i in range(size):
            odd, odd_len = self._center_spread(s, size, i, i)
            even, even_len = self._center_spread(s, size, i, i+1)

            max_sub = odd if odd_len >= even_len else even
            if len(max_sub) > max_len:
                max_len = len(max_sub)
                max_str = max_sub
        return max_str

    def _center_spread(self, s, size, left, right):
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j], j-i-1

# 1. force method
# class Solution:
#     # time cost: o(n^3)
#     # space cost: o(1)
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s

#         max_str = ''
#         max_len = 1
#         for i, _ in enumerate(s):
#             for j, st in enumerate(s[i:]):
#                 if j - i + 1 > max_len and self._valid(s, i, j):
#                     len_ = j - i + 1
#                     max_str = s[i:j+1]
#                     break
#         return max_str
    
#     def _valid(self, s, left, right):
#         while left < right:
#             if s[left] != s[right]:
#                 return False
            
#             left += 1
#             right -= 1
#         return True