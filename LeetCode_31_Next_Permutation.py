# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # split permutation in prefix and largest suffix of numbers all in descending order
        idx = -1
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                idx = i
                
        # is already largest permutation
        if idx == -1:
            nums = nums.sort()
            return
            
        v    = 999
        idxj = 0

        # find smallest number in suffix larger than idx
        for j in range(idx + 1, len(nums)):
            if nums[j] > nums[idx] and nums[j] <= v:
                v    = nums[j]
                idxj = j
                
        # swap idx and the smallest largest number
        nums[idx], nums[idxj] = nums[idxj], nums[idx]
        
        a = idx       + 1
        z = len(nums) - 1
        
        # reverse suffix into ascending order
        while a < z:
            nums[a], nums[z] = nums[z], nums[a]
            a += 1
            z -= 1
        
        # done
   
        
            
