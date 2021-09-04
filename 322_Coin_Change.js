
/*
https://leetcode.com/problems/coin-change/
*/
var coinChange = function(coins, amount) {
    let arr = new Array(amount + 1)
    
    arr.fill(1<<16); // invalid value
    arr[0] = 0;
    
    for(let a = 0; a <= amount; a++) {
        for (let c of coins) {
            arr[a + c] = Math.min(arr[a + c], arr[a] + 1);
        }
    }
    // check if amount can be changed
    return (arr[amount] != 1 << 16) ? arr[amount] : -1;
};
