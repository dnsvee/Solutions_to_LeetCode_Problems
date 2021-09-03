# https://leetcode.com/problems/count-and-say/
import re

class Solution:
    def countAndSay(self, n: int) -> str:
        def func(m):
            g = m.group(0)
            return str(len(g)) + g[0]
        
        s = '1'
        for i in range(2, n + 1):
            s = re.sub(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+', func, s)
            i += 1

        return s
        
