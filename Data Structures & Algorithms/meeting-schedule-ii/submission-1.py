"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i : i.start)
        rooms = []
        for i in range(len(intervals)):
            if rooms and intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i].end)
        return len(rooms)

# sort the intervals
# check if they conflict, if yes, 
# if not, we move on to check the next one
# keep the end time of the current interval (1 room) maybe deque