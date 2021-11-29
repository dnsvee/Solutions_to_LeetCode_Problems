// https://leetcode.com/problems/sudoku-solver/
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<short> R(10), C(10), S(10);
        
        for(int y = 0; y < 9; y++) 
            for(int x = 0; x < 9; x++) {
                int z = (y / 3) * 3 + x / 3;
                int v = (board[y][x] == '.') ? 0 : board[y][x] - '0';
                R[y] |= 1 << v;
                C[x] |= 1 << v;
                S[z] |= 1 << v;
            }
			
        try {
            solve(R, C, S, board, -1, -1);
        } catch (const char* c) {
            return;
        }
    }
    
    void solve(vector<short>& R, vector<short>& C, vector<short>& S, vector<vector<char>>& board, int x, int y) {
        x =            (x + 1) % 9;
        y = (x == 0) ? (y + 1) : y;
        
        if (y == 9) 
            throw "done";
        
        if (board[y][x] == '.') {
            int z = (y / 3) * 3 + x / 3;

            for(int i = 1; i < 10; i++) {
                if (((R[y] | C[x] | S[z]) & (1 << i)) != 0) 
                    continue;

                short x0 = C[x];
                short y0 = R[y];
                short z0 = S[z];

                R[y] |= 1 << i;
                C[x] |= 1 << i;
                S[z] |= 1 << i;
                board[y][x] = '0' + i;
                
                solve(R, C, S, board, x, y);

                C[x] = x0;
                R[y] = y0;
                S[z] = z0;
                board[y][x] = '.';
            }
        } else {
            solve(R, C, S, board, x, y);
        }
    }
};
