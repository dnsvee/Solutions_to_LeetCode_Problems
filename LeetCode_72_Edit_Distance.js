/*
https://leetcode.com/problems/edit-distance/
*/
var minDistance = function(word1, word2) {
    a = word1;
    b = word2;
    
    // single array; index of char i and j is j * len(a) + i
    let M = [];

    let W = a.length + 1;
    
    for(let j = 0; j <= b.length; j++) {
        for(let i = 0; i <= a.length; i++) {
            if (i === 0) {
                // edit distance if one string has no chars is length of prefix of other word
                M[j * W] = j;
            } else if (j === 0) {
                // edit distance if one string has no chars is length of prefix of other word
                M[i    ] = i;
                
            } else {
                // no cost added if letters match
                let v = (a[i - 1] === b[j - 1]) ? 0 : 1;

                // cost for edit distance with prefix of word a[:i] and b[j]
                M[j * W + i] = Math.min( 
                    v + M[(j - 1) * W + i - 1],
                    1 + M[ j      * W + i - 1],
                    1 + M[(j - 1) * W + i    ]);
            };
        };
    };
    
    return M[b.length * W + a.length];
};