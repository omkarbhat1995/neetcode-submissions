class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start, end = 0, 0
        
        for i, char in enumerate(s):
            # Continuously push the end of the partition outward if a character 
            # appears later in the string
            end = max(end, last_occurrence[char])
            
            # When our current index catches up to the furthest boundary, 
            # the partition is safely closed
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
                
        return partitions