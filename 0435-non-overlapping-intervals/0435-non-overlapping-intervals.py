class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prev_end = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < prev_end:
                count += 1
                prev_end = min(prev_end, i[1])
            else:
                prev_end = i[1]
        return count