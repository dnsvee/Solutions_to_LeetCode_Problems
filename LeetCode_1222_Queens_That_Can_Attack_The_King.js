
/*
https://leetcode.com/problems/queens-that-can-attack-the-king/submissions/
*/
var queensAttacktheKing = function(queens, king) {
    let [kx, ky] = king;
    let Qs = new Set();
    
    // add coords of queens as a single int in a set
    for (let [qx, qy] of queens) 
        Qs.add((qy << 16) + qx)

    let R = []
    // start from kings position and move in all 8 directions and when a queen encountered
    // store in R(esult) array
    for (let [x, y] of [[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [1,-1], [-1,1], [1,1]]) {
        let x0 = kx + x;
        let y0 = ky + y;
        
        while (x0 >= 0 && x0 <= 7 && y0 >= 0 && y0 <= 7) {
            
            // queen found stop moving in the direction
            if (Qs.has((y0 << 16) + x0)) {
                R.push([x0, y0])
                break
            }
            
            x0 += x;
            y0 += y;
        }
    }
    
    return R;
};
