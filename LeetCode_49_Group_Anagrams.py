
# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map each word in list to tuple of (word, sorted anagram of word)
        strs = map(lambda x : (x, ''.join(sorted([c for c in x]))), strs)
        
        # sort by anagram
        strs = sorted(strs, key=lambda x : x[1])
        
        res = []
        tmp = []

        # group each tuple with same anagram in a list
        for s in strs:
            if len(tmp):
                if tmp[-1][1] == s[1]:
                    tmp.append(s)
                else:
                    res.append(tmp)
                    tmp = [s]
            else:
                tmp.append(s)
                
        if len(tmp):
            res.append(tmp)
            
        # map back to list of words (grouped by anagram)
        return [[item[0] for item in r] for r in res]
            
