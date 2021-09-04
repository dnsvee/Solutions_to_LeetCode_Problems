
/*
https://leetcode.com/problems/count-nice-pairs-in-an-array/
*/
var countNicePairs = function(nums) {
    // reverse number
    var rev = function(num) {
        let d = 0;
        let n;
        while (num) {
            d     = d * 10;
            n     = num % 10;
            d     = d + n;
            num   = (num - n) / 10
        }
        return d;
    }
        
    // calc. the difference between a number and its reverse
    // numbers that have the same diff. form nice pairs.
    
    let r;    
    let amap = nums.reduce((a, e) => {
        r = rev(e)
        a[e - r] = (a[e - r] || 0) + 1;
        return a
    }, []);
    
    // for each interval there are N numbers. 
    // calc. the permutations of len. 2 and sum them
 
    // if more than 2 numbers form a nice pair
    // calulate the permutations of picking 2 numbers from 
    // the total amount using the formula n * (n - 1)
    
    return (amap.reduce((a, e) => a + e * (e - 1) / 2, 0)) % (10 ** 9 + 7);
};
