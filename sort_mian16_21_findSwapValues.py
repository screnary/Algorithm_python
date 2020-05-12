

class Solution:
    def findSwapValues(self, array1, array2) -> List[int]:
        """ input| array1: List[int], array2: List[int]
           output| List[int]
        """
        sumA = sum(array1)
        sumB = sum(array2)
        if (sumA - sumB) % 2 != 0: return []

        target = (sumA-sumB) // 2
        # 可使用散列表，或者排序加快下步遍历
        arrA = set(array1)
        arrB = set(array2)

        for b in arrB:
            if target+b in arrA:
                return [target+b, b]
        return []
