class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        input:
            nums1: List[int]
            nums2: List[int]
        output:
            float
        """
        # brute force O(m+n)
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0:
            nums_merge = nums1 if n==0 else nums2
        else:
            nums_merge = [0 for _ in range(m+n)]
            self.merge(nums1, nums2, nums_merge)
        if (m+n) % 2:
            # odd len
            res = float(nums_merge[(m+n)//2])
        else:
            res = 0.5 * (nums_merge[(m+n)//2-1] + nums_merge[(m+n)//2])
        return res

    def merge(self, nums1, nums2, res_merge):
        # assume m,n > 0
        m, n = len(nums1), len(nums2)
        l1 = 0
        l2 = 0
        for k in range(len(res_merge)):
            if l1 >= m:
                res_merge[k] = nums2[l2]
                l2 += 1
            elif l2 >= n:
                res_merge[k] = nums1[l1]
                l1 += 1
            elif nums1[l1] > nums2[l2]:
                res_merge[k] = nums2[l2]
                l2 += 1
            else:
                res_merge[k] = nums1[l1]
                l1 += 1


if __name__ == '__main__':
    nums1 = [1,3,4]
    nums2 = [2]
    sol = Solution()
    res = sol.findMedianSortedArrays(nums1, nums2)
    print(res)
