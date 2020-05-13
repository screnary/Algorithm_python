""" 
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

贪心算法，每次找零从大面额开始给出。

注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 
"""

class Solution:
    def lemonadeChange(self, bills):
        """ input| bills: List[int]
           output| int
        """
        fives, tens = 0, 0
        for money in bills:
            if money == 5:
                fives += 1
            elif money == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif money == 20:
                # greedy, change from larger pocket money
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                    # twenty can not be used as change
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
