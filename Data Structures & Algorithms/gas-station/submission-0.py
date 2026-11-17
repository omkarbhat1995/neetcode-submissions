class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        current_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            # If our tank drops below zero, it means we cannot reach station i + 1 
            # from our current start_index (or from any station in between).
            if current_gas < 0:
                # The earliest possible start must be the next station
                start_index = i + 1
                # Reset our current tank for this new potential start
                current_gas = 0
                
        return start_index