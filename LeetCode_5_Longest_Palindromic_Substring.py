#
# https://leetcode.com/problems/longest-palindromic-substring/
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def grow(seed):
            # consider s[i:j - i + 1] a palindrome; make it as large as possible 
            # by increasing j and decreasingij by per iteration
            i, j = seed
            
            try:
                while i:
                    if s[i - 1] == s[j + 1]:
                        i = i - 1
                        j = j + 1
                    else:
                        break
            finally:
                return (j - i + 1, i)
            
        seeds = []
        
        # create a list of indices (seeds) representing a substring of s 
        # which is a palindrome
        try:
            for i in range(0, len(s) - 1):
                if s[i] == s[i + 1]:
                    seeds.append((i, i + 1))
                    
                if s[i] == s[i + 2]:
                    seeds.append((i, i + 2))
        except:
            pass
                    
        Max = (1, 0)
        
        # grow each seed and keep track of the seed with the longest length
        while len(seeds):
            Max = max(Max, grow(seeds.pop()))
            
        l, i = Max
        return s[i:i + l]
            