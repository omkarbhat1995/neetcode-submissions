class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c,t_c = Counter(s), Counter(t)
        if s_c == t_c:
            return True
        return False