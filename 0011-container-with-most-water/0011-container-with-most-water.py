class Solution:
    def maxArea(self, height: List[int]) -> int:
        areamax = 0
        i = 0
        j = len(height) - 1
        while i != j:
            area = (j-i) * (min(height[i], height[j]))
            areamax = max(area, areamax)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return areamax