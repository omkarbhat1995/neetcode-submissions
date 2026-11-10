import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_chars = string.punctuation +' '
        s= s.lower().translate(str.maketrans('','',remove_chars))
        left, right = 0, len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True


