# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        R = []
        def parens(pre, n, o):
            print(pre, n, o)
            # o   is  open parens
            # n   is total parens
            # pre is prefix
            if n == 0:
                R.append(pre)

            if o + 1 <= n - 1:
                parens(pre + '(', n - 1, o + 1)

            if o > 0 and n > 0:
                parens(pre + ')', n - 1, o - 1)

        parens('', n * 2, 0)

        return R
