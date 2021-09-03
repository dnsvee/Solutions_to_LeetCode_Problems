/*
https://leetcode.com/problems/valid-sudoku/
*/

var isValidSudoku = function(board) {
    /*
    create a hashmap for each horiz, vert and box and while
    iterating each number put it in the correct map and
    if the number already exists than it's not a valid sudoku
    */
    
    H = new Map();
    V = new Map();
    B = new Map();
    
    for (let y = 0; y < 9; y++) {
        for (let x = 0; x < 9; x++) {
            let c = board[y][x];
            
            if (c == '.') 
                continue;
            
            let i = parseInt(c) 
            
            // calculate if which box (x,y) lies
            let box = ~~(y / 3) * 3 + ~~(x / 3)
            
            H.set(y,   H.get(y)   || new Set());
            V.set(x,   V.get(x)   || new Set());
            B.set(box, B.get(box) || new Set());
            
            if (H.get(y).has(i) || V.get(x).has(i) || B.get(box).has(i)) 
                return false;
            
            H.get(y).add(i);
            V.get(x).add(i)
            B.get(box).add(i)
            
        }
    }
    
    return true;
};
