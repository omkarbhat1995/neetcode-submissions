class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen= set(nums)
        max_len =  0
        for num in nums:
            length = 0
            if num-1 not in seen:
                length = 1
            while num+length in seen:
                length +=1
            max_len = max(length,max_len)
        return max_len
        