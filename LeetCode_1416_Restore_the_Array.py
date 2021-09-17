# https://leetcode.com/problems/restore-the-array/
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # so in this DP solution M[x] = y 
        # y is the sum of the total paths that end at digit s[x]
        
        M = {-1: 1} # init condition
        for i in range(0, len(s)):
            if s[i] != '0': # numbers dont start with zeroes
                j = 0
                v = int(s[i])
                while v <= k:
                    M[i + j] = M.get(i + j, 0) + M.get(i - 1, 0)
                    
                    if i + j + 1 == len(s): # done
                        break

                    j = j + 1

                    v = v * 10 + int(s[i + j]) 
                    
        return M.get(len(s) - 1, 0) % (pow(10, 9) + 7)

