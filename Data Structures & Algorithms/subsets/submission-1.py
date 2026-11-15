class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(start:int,current_subset:list[int]):
            res.append(list(current_subset))

            for i in range(start,len(nums)):
                current_subset.append(nums[i])
                backtracking(i+1,current_subset)
                current_subset.pop()
        backtracking(0,[])
        return res