class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        # Traverse backwards from the second-to-last element down to index 0
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0