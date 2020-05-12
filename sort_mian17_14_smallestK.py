# 最小K个数： 堆排序
# 维护K维大顶堆

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        """
        input|  arr: List[int], k: int
        output| List[int]
        """
        if k==0: return []
        # max heap
        def sift_down(arr, root, n):
            cur_val = arr[root]
            while (2*root+1) < n:  # if has child
                child = 2*root + 1
                if child+1 < n and arr[child+1]>arr[child]:
                    child = child + 1
                # check if valid
                if cur_val < arr[child]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = cur_val
        
        # construct k-max heap
        k_max_heap = arr[:k]
        for i in range((k-1-1)//2, -1, -1):
            sift_down(k_max_heap, i, k)
        
        # process the remained items
        for num in arr[k:]:
            if num < k_max_heap[0]:
                k_max_heap[0] = num
                sift_down(k_max_heap, 0, k)

        return k_max_heap