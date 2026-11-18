"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        
        # Traverse and check if the current meeting starts before the previous one ends
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
                
        return True