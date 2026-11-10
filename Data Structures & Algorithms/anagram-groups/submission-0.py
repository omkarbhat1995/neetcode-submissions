class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for string in strs:
            count = [0]*26
            for s in string.lower():
                count[ord(s)-ord('a')] += 1
            ana[tuple(count)].append(string)
        res = list(ana.values())
        return res        