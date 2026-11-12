class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stores pairs of (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # If the current height is less than the top of the stack, we resolve previous bars
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate the area extending from the popped bar's original start index to the current index i
                max_area = max(max_area, height * (i - index))
                # The new height can effectively be extended backward to where the popped bar started
                start = index
            stack.append((start, h))

        # Resolve any remaining bars in the stack that extend all the way to the end of the histogram
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area