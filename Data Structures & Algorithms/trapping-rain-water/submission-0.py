class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, trapped_water = 0, len(height)-1, 0
        max_left, max_right = height[left], height[right]
        while left <right:
            if max_left < max_right:
                left+=1
                max_left = max(height[left],max_left)
                trapped_water+=max_left-height[left]
            else:
                right-=1
                max_right = max(height[right],max_right)
                trapped_water+=max_right-height[right]
        return trapped_water


