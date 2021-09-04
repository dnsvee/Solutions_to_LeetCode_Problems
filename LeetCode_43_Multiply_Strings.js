/*
https://leetcode.com/problems/multiply-strings/submissions/
*/

var mult = function(a, b) {
    a = a.split('').reverse();
    b = b.split('').reverse();

    // result 
    let res = [];
    for(let i = 0; i < b.length; i++) {
        for(let j = 0; j < a.length; j++) {
            let d = parseInt(b[i]) * parseInt(a[j]) + (res[j + i] || 0);
            
            // value of single digit
            let r =  d      % 10;
            // carry over
            let c = (d - r) / 10;

            res[j + i] =  r;

            // add remaining carry over in next position
            if (c) 
                res[j + i + 1] = (res[i + j + 1] || 0) + c;
        }            
    }
    
    // fix situation when prefix of res == 0000... 
    return res.reverse().join('').replace(/^0*/, '') || '0'
}
    
var multiply = function(num1, num2) {
    return mult(num1, num2)
};
