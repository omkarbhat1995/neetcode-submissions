"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # Separate and sort start and end times
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        
        start_ptr = 0
        end_ptr = 0
        used_rooms = 0
        
        while start_ptr < len(intervals):
            # If the current meeting starts strictly before the earliest ending meeting finishes,
            # we have a conflict and must allocate an additional room.
            if start_times[start_ptr] < end_times[end_ptr]:
                used_rooms += 1
            else:
                # A previous meeting has ended, freeing up a room.
                # We reuse the room and increment the end pointer to check the next earliest end time.
                end_ptr += 1
                
            start_ptr += 1
            
        return used_rooms