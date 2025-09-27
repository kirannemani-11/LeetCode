class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1 = points[i][0]
                    x2 = points[j][0]
                    x3 = points[k][0]
                    y1 = points[i][1]
                    y2 = points[j][1]
                    y3 = points[k][1]
                    area = max(abs(0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))), area)
        return area