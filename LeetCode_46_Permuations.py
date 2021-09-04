
# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        L = []
        
        # permutations with backtracking
        def p(i):
            if i == len(nums):
                L.append(nums[:])

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                p(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        p(0)
                
        return L

