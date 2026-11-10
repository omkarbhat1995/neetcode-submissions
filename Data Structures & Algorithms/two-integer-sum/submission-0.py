class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       prev_pos = {}
       for i,n in enumerate(nums):
        find_tar = target - n
        if find_tar in prev_pos:
            return [prev_pos[find_tar],i]
        prev_pos[n] = i
       return []
