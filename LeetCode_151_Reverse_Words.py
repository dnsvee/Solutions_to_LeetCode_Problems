
# https://leetcode.com/problems/reverse-words-in-a-string/submissions/
class Solution:
    def reverseWords(self, s: str) -> str:
        # split on spaces and strip each word clean from leading and trailing whitespace
        s = map(lambda x: x.strip(), s.split(' '))
        
        # after stripping remove all strings with zero length
        s = list(filter(lambda x: len(x), s))
        
        # reverse the words in the list
        s = s[::-1]
        
        # turn list into string by joining each word with a single space between them
        s = ' '.join(s)
        
        return s
            
