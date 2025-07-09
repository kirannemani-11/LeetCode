class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        r = []
        m1 = intervals[0][0]
        m2 = intervals[0][1]
        for i in range(len(intervals)):
            x = intervals[i][0]
            y = intervals[i][1]
            if x > m2:
                r.append([m1,m2])
                m1 = x
                m2 = y
            elif y < m2:
                if i == len(intervals) - 1:
                    r.append([m1,m2])
                continue
            else:
                m2 = y
            if i == len(intervals) - 1:
                r.append([m1,m2])
        return r