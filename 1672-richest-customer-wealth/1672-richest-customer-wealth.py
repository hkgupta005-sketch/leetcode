class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for i in accounts:
            total = sum(i)
            if total > richest:
                richest = max(richest,total)
        return richest

       

        