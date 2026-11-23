class Solution(object):
    def balancedStringSplit(self, s):
        balance = 0
        count = 0
        for i in s:
            if i == 'L':
                balance += 1
            if i == 'R':
                balance -=1
            if balance == 0:
                count+=1
        return count
        