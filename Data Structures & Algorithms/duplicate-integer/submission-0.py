class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in l1:
                return True
            else:
                seen.add(n)
        return False