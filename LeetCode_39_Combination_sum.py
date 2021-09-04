# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        M = dict()
        
        # M[x] = [a:list, b:list, c:list]
        # this means target x can by each list a, b, c, ... and by summing the numbers
        # in each list ex.:
        # M[1] == [[6], [3,3], [2,2,2]]
        # start from M[target] and try to reach M[0]
        
        M[target] = [[]]
        for i in range(target, 0, -1):
            if i not in M:
                continue
                
            for c in candidates:
                if i - c  < 0:
                    continue

                a = M.get(i - c, [])
                for l in M.get(i): 
                    # add candidate to each lsit from old target to make a list
                    # that can reach new rarget
                    a.append(l[:] + [c])
                
                M[i - c] = a

        # target cant be reached
        if 0 not in M:
            return []
        
        # remove uniques
        s = {tuple(sorted(i)) for i in M[0]}
        return [list(i) for i in s]

    
