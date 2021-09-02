#
# https://leetcode.com/problems/wildcard-matching/submissions/
#

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M = {}

        # there is a string to match but not a pattern to use
        if len(s) and not len(p):
            return False
            
        # no string than only true if pattern is all stars
        if not len(s):
            return not any([c for c in p if c != '*'])

        # M[(x, y)] == 0    means matches without consuming a char
        # M[(x, y)] == 1    means matches with consuming a char
        # M[(x, y)] == None means no match
        
        # test if first char can be matched and update M with a valid init state
        if p[0] == '*' or p[0] == '?' or p[0] == s[0]:
            M[(0, -1)]  = 0 
        else:
            return False
            
        for y in range(0, len(p)):
            for x in range(0, len(s)):
                    
                # if char matches pattern or is ? than match diagonally
                # can also match after a star that does not consume anything
                if p[y] == '?' or p[y] == s[x]:
                    if M.get((x, y - 1), -1) == 0 or M.get((x - 1, y - 1), -1) == 1:
                        M[(x, y)] = 1

                # a star matches in the diagonal with a char or ?
                # or it matches if the star consumed the previous char
                if p[y] == '*':
                    if M.get((x, y - 1), -1) >= 0:
                        M[(x, y)] = M[(x, y - 1)]
                        
                    if M.get((x - 1, y), -1) >= 0:
                        M[(x, y)] = 0

        return M.get((len(s) - 1, len(p) - 1), -1) >= 0
                    
                    
            
        

    
                    
       
