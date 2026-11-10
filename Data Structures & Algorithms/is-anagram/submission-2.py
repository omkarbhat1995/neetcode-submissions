class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if Counter(s) == Counter(t):
            return True
        return False
        """
        return True if Counter(s) == Counter(t) else False