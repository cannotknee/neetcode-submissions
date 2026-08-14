class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i : i[0])
        curEnd = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if curEnd > start:
                curEnd = min(curEnd, end)
                count += 1
            else:
                curEnd = end
        return count
# brute force: loop for each interval to check if intersect
# better: sort the intervals, so we can compare side-by-side if overlaps
# if overlaps, count += 1, we remove it, then check next
# else, this is then new base interval and check again for next
