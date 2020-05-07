class Solution:
    """ 使用 list pop 操作太耗费时间了，但是利于理解
        主要是重复计算了太多同样的时间，所以很慢？
        找到了原因： [A,C] 和 [C,A] 会重复遍历决策树，这样是回溯的弊端
        通过集合或列表的方式描述 选择空间，造成选择空间冗余，没能压缩。如从'C'开始时，仍会下层遍历'A'
    """
    def readBinaryWatch(self, num: int) -> List[str]:
        led_dict = {'A':8, 'B':4, 'C':2, 'D':1,
                    'a':32, 'b':16, 'c':8, 'd':4, 'e':2, 'f':1}

        res = []

        def backtrack(n, h_track, h_val, m_track, m_val):
            # terminate condition
            if len(h_track) + len(m_track) == n:
                cur_time = "{:d}:{:02d}".format(h_val, m_val)
                if cur_time not in res:
                    res.append(cur_time)
                return
            
            for led in led_dict:
                # check for invalid choice
                if led in h_track or led in m_track:
                    continue
                # make choice
                if led >='A' and led <='D' and h_val+led_dict[led] < 12:
                    h_track.append(led)
                    h_val += led_dict[led]
                elif led >='a' and led <='f' and m_val+led_dict[led] < 60:
                    m_track.append(led)
                    m_val += led_dict[led]
                else:
                    continue  # if invalid
                # deeper into dicision tree
                backtrack(n, h_track, h_val, m_track, m_val)
                # remove choice
                if led >='A' and led <='D':
                    h_track.pop()
                    h_val -= led_dict[led]
                elif led >='a' and led <='f':
                    m_track.pop()
                    m_val -= led_dict[led]

        h_track, h_val = [], 0  # hours track, hour value
        m_track, m_val = [], 0  # minutes track, minute value
        backtrack(num, h_track, h_val, m_track, m_val)
        return res


class Solution_better(object):
    """ 使用访问列表来记录track， 另外写函数判断时间合法性 
        visited 数组，dfs 有一个 start 控制，缩小了下层的搜索空间（选择列表压缩）
        这样 从 'C' 开始时，就不会重新遍历 'A' 了
    """
    def __init__(self):
        self.result_all = None
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = None
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.result_all = []
        self.visited = [0 for _ in range(len(self.nums))]
        self.dfs(num, 0, 0)
        return self.result_all
    
    def dfs(self, num, step, start):
        if step == num:
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            if not self.calc_sum(self.visited):
                self.visited[i] = 0
                continue
            self.dfs(num, step + 1, i + 1)
            self.visited[i] = 0
        return
            
    def calc_sum(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        return 0 <= sum_h <= 11 and 0 <= sum_m <= 59
    
    def handle_date(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        result = "" + str(sum_h) + ":"
        if sum_m < 10:
            result += "0" + str(sum_m)
        else:
            result += str(sum_m)
        return result
