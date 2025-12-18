class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        res = []
        med = (m+n) // 2
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
            if len(res) > med:
                break
        if len(res) <= med:
            if i < len(nums1):
                while i < len(nums1):
                    res.append(nums1[i])
                    i+=1
                    if len(res) > med:
                        break
            elif j < len(nums2):
                while j < len(nums2):
                    res.append(nums2[j])
                    j += 1
                    if len(res) > med:
                        break
        if (m+n) % 2 == 1:
            return res[med]
        return (res[med - 1] + res[med]) / 2