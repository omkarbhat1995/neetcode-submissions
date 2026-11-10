class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)

        frequency = [[] for _ in range(len(nums)+1)]

        for num,freq in ctr.items():
            frequency[freq].append(num)
        res = []

        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        