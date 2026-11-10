class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l1, x = list(sorted(nums)),len(nums)
        return l1[x-k]