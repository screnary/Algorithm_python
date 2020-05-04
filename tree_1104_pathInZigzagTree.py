class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [label]
        # get the depth
        depth = 0
        while (2**depth) <= label:
            depth += 1
        for d in range(depth, 1, -1):
            max_num = 2**d - 1
            min_num = 2**(d-1)
            if d % 2 == 0:
                res.append((min_num + (max_num-res[-1]))//2)
            else:
                res.append((max_num - (res[-1]-min_num))//2)
        return res[::-1]
