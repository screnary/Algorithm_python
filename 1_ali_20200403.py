""" valuable nums count
brute force: maintain max_l and min_r  O(n^2)
optimize:
    1,merge idea
    2,sort dict {num:idx} O(nlogn)
      then traverse O(n)
"""
import pdb
import sys
MAX_INT = sys.maxsize


def count_valuable(n, nums):
    """ input: 
            n: len of input array, int
            nums: list[int]
        output: 
            res: int
        too slow
    """
    count = 0
    if n < 3:
        return 0
    max_l = MAX_INT
    min_r = -MAX_INT
    for i in range(1, n-1):
        curr = nums[i]
        # check for cur valid, skip if not
        if curr >= max_l or curr <= min_r:
            continue
        min_l = nums[i-1]
        max_r = nums[i+1]
        # search left # for j in range(i-1, -1, -1):
        j = i-1
        while j >= 0:
            if nums[j] <= curr:
                j -= 1
                continue
            # condition: nums[j] > curr
            # pdb.set_trace()
            if min_l > nums[j]:
                min_l = nums[j]
            while (j > 0) and (nums[j-1]==nums[j]):
                j -= 1
            j -= 1

        # search right # for k in range(i+1, n, 1):
        k = i+1
        while k < n:
            if nums[k] >= curr:
                k += 1
                continue
            if max_r < nums[k]:
                max_r = nums[k]
            while (k < n-1) and (nums[k+1]==nums[k]):
                k += 1
            k += 1

        # judge ? f = d*g, d is int
        if not (min_l % max_r) and (min_l > max_r):
            count += 1
    return count


if __name__ == '__main__':
    # input
    n = int(input())
    nums = list(map(int, input().split(' ')))
    # n = 3
    # nums = [4,3,2]
    res = count_valuable(n, nums)
    print(res)
