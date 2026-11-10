class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            # Drops the lowest set 1-bit
            n &= (n - 1)
            count += 1
            
        return count