"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

参考基数排序思想，不太合适
自定义排序:
x, y are two strings
x+y > y+x => x>y
"""

class Solution:
    def minNumber(self, nums):
        """ input|  nums: List[int]
           output|  str
        """
        nums_str = list(map(str, nums))

        def quick_sort(arr, l, r):
            if l >= r:  # terminate condition
                return
            # process this node            
            i, j = l, r
            while i < j:
                # arr[l] <= arr[j]
                while i<j and arr[l]+arr[j] <= arr[j]+arr[l]:
                    j -= 1
                # arr[i] <= arr[l]
                while i<j and arr[i]+arr[l] <= arr[l]+arr[i]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            # i==j
            arr[l], arr[i] = arr[i], arr[l]

            quick_sort(arr, l, i-1)  # left part
            quick_sort(arr, i+1, r)  # right part

        quick_sort(nums_str, 0, len(nums_str)-1)
        return "".join(nums_str)
            

if __name__ == '__main__':
    sol = Solution()
    res = sol.minNumber([3,30,34,5,9])
    print(res)