#
# https://leetcode.com/problems/3sum/
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        D    = {}
        S    = set() # solution set
        
        # map list into (index, value) combos
        for e, k in enumerate(nums):
            D[k] = (e, k)
            
        # iterate over the list N ** 2 style; try each unique 2 pair combo
        for a in range(0, len(nums) - 2):
            for b in range(a + 1, len(nums) - 1):
                
                try:
                    # if nums[a] == 5 and nums[b] == 3 than there must exist a value of 8
                    # for a 3sum to exist; find it and add to solution
                    e, k = D[-nums[a] -nums[b]]
                    
                    if e > b:
                        S.add((nums[a], nums[b], -nums[a] -nums[b]))
                        
                except:
                    pass
                
        return list(S)
                    
                