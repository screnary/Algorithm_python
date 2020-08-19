"""
347. 前 K 个高频元素
堆，优先队列练习
要求时间复杂度优于O(n log n)，n为数组大小
"""
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        inputs:
        nums: List[int]
        k: int
        outputs:
        return List[int]
        """
        # count of every element of input list, save to a dict {num: count}
        frequent_dict = {}
        for num in nums:
            if num in frequent_dict:
                frequent_dict[num] += 1
            else:
                frequent_dict[num] = 1

        assert (k <= len(frequent_dict)), "invalid k"

        def sift_up(arr, k):
            # arr is a list, elements are (key, value) tuples
            # add an element, check with its parent node, if go up
            cur_item, cur_idx = arr[k-1], k-1  # the end of heap
            while cur_idx > 0 and arr[(cur_idx-1)//2][1] > cur_item[1]:
                arr[cur_idx] = arr[(cur_idx-1)//2]
                cur_idx = (cur_idx-1) // 2
            arr[cur_idx] = cur_item  # if the location is correct, put the item in

        def sift_down(arr, root, k):
            # update an element (as root), check with its sub tree, if go down
            cur_item = arr[root]
            while 2*root + 1 < k:  # if has child
                child = 2*root + 1
                if child+1 < k and arr[child+1][1] < arr[child][1]:
                    child = child + 1
                if cur_item[1] > arr[child][1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break  # the remain heap is in correct order
            arr[root] = cur_item
        
        # using count as value, create a min heap of scale k
        frequent_list = list(frequent_dict.items())
        heap_min = []  # init a list of len k
        for i in range(k):
            heap_min.append(frequent_list[i])
            sift_up(heap_min, i+1)

        # maintain the min heap, look through the remained items in dict
        # if value > heap top, then enheap
        for item in frequent_list[k:]:
            if item[1] > heap_min[0][1]:
                heap_min[0] = item
                sift_down(heap_min, 0, k)

        # heap sort the result list, max heap
        heap_max = self.heap_sort(heap_min)
        # return [item[0] for item in heap_min]
        return [item[0] for item in heap_min]
    
    def heap_sort(self, arr):
        # max heap
        def sift_down(arr, root, k):
            cur_item = arr[root]
            while 2*root + 1 < k:
                child = 2*root + 1
                if child + 1 < k and arr[child+1][1] > arr[child][1]:
                    child = child + 1
                if arr[root][1] < arr[child][1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = cur_item
        
        k = len(arr)
        for i in range((k-2) // 2, -1, -1):
            sift_down(arr, i, k)
        
        for scale in range(k-1, 0, -1):
            arr[scale], arr[0] = arr[0], arr[scale]
            sift_down(arr, 0, scale)
        
        return arr
    
    # >>> use python lib heapq >>>
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
    # <<< use python lib heapq <<<


if __name__=='__main__':
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    sol = Solution()
    output = sol.topKFrequent(nums, k)
    print(output)
