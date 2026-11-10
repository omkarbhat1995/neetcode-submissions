class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #l1, x = list(sorted(nums)),len(nums)
        #return l1[x-k]
        l1 = len(nums)
        heapq.heapify(nums)
        for i in range(l1-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

