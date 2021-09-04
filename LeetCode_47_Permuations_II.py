
# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        L = set()
        
        # add permutation as tuple to set so
        # it will remove non-duplicates
        
        def p(i):
            if i == len(nums):
                L.add(tuple(nums))

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                p(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        p(0)

        # convert tuple to set
        L = list(L)
        for i in range(len(L)):
            L[i] = list(L[i])
                
        return L
