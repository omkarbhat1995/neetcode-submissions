class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s_c,t_c = 
        if Counter(s) == Counter(t):
            return True
        return False