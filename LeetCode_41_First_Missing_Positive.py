#
# https://leetcode.com/problems/first-missing-positive/
#

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        j = len(nums) - 1
        
        # scan over the array and place each number in the index 
        # corresponding to its number so 5 goes into index 4, 1 into index 0
        
        # if a number cant be placed in a valid index skip it; so when it is
        # smaller than 0 or larger than the length of the array nums; or if 
        # there are multiples of the same number
        
        # so if the array is of length 5 then after the scan all the numbers from
        # nums that fall in the inclusive range of 1 ... len(nums) are in its 
        # proper index in the array
        
        # scan over the array again and find the first index of the array for
        # which it's value is not index + 1. This is the index of the first
        # missing number
        
        while j >= 0:
            n = nums[j]
            # ignore numbers smaller < 0 or larger than the size of the array
            # ignore if the number is already in the right spot or if swapping
            # makes no difference (avoids TLE)
            
            if n < 1 or n >= len(nums) or n == j + 1 or nums[j] == nums[n - 1]:
                j -= 1
                continue
                
            nums[n - 1], nums[j] = nums[j], nums[n - 1]

        # if number at index n is the number n + 1 it is in the right place
        # if not then the positive number index + 1 is missing
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1
            
        # if nums == [1, 2, 3, 4] then missing number is 5
        return len(nums) + 1
            
                
            
	    
        
