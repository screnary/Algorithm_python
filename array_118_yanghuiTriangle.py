class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ 118 """
        if numRows==0:
            return []
        res = [[1]]
        for r in range(1, numRows):
            pre_list = res[-1]
            cur_list = [1] * (len(pre_list)+1)
            for i in range(len(pre_list)-1):
                cur_list[i+1] = pre_list[i] + pre_list[i+1]
            res.append(cur_list)
        return res
    
    def getRow(self, rowIndex: int) -> List[int]:
        """ 119 """
        # 优化： 可以从后往前更新数组值，从倒数第二位，a[i] = a[i] + a[i-1]，这样更新后不影响后续其他位置更新
        if rowIndex == 0:
            return [1]
        
        pre_row = [1]
        for r in range(1, rowIndex+1):
            cur_row = [1] * (r+1)
            for i in range(r-1):
                cur_row[i+1] = pre_row[i] + pre_row[i+1]
            pre_row = cur_row
        return cur_row
