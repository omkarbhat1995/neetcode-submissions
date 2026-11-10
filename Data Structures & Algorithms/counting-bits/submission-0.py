class Solution:
    def hammingweight(self,n:int)->int:
        count=0
        while n:
            n&=(n-1)
            count+=1
        return count
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n+1):
            counts.append(self.hammingweight(i))
        return counts
        