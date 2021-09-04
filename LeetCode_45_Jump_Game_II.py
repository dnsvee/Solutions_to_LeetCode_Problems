# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:     
        i     = 0 # where we are at
        jumps = 1
        
        if len(nums) == 1: 
            return 0            
        
        # we start at location index and can jump to maxsofar
        maxsofar = nums[0]
        
        # while not end reached
        while maxsofar < len(nums) - 1:            
            
            # we need a jump
            jumps += 1           
            
            # find best new point to jump to; which is the point that
            # allows us to jump furthest
            m0 = maxsofar # furthest point
            i0 = 0        # tmp. index
            
            while i < maxsofar:                
                i += 1
                if m0 < nums[i] + i:
                    m0 = nums[i] + i
                    i0 = i
            
            # jump to this point
            maxsofar = m0 
            i        = i0    
            
        return jumps
        
