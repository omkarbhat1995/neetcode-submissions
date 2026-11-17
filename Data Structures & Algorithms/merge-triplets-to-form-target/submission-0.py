class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        found_x = found_y = found_z = False
        
        for a, b, c in triplets:
            # A triplet is only valid if NONE of its elements exceed the target components.
            # Once an element exceeds the target, a max() operation would permanently overshoot it.
            if a <= x and b <= y and c <= z:
                # If valid, check which target components this triplet perfectly provides
                if a == x:
                    found_x = True
                if b == y:
                    found_y = True
                if c == z:
                    found_z = True
                    
                # Early exit optimization if all components are already found
                if found_x and found_y and found_z:
                    return True
                    
        return found_x and found_y and found_z