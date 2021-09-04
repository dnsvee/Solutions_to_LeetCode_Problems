
/*
https://leetcode.com/problems/non-decreasing-array/submissions/
*/
var checkPossibility = function(nums) {
    let left = 0, right = 0;
    let i = 0;
    let j = nums.length - 1;
    
    let x = nums[i];
    let y = nums[j];
    
    while (i < nums.length) {
        if (x > nums[i]) {
            left++;
        } else {
            x = nums[i];
        }
        i++;
        
        if (y < nums[j]) {
            right++;
        } else {
         y = nums[j];
        }
        j--;
        
        // foudn a place with two or more elements in the wrong order
        // cant be fixed
        if (left >= 2 && right >= 2) 
            return false;
    }
    return true;
};
