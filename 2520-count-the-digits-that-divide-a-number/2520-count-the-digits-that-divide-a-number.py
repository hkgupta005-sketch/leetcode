class Solution(object):
    def countDigits(self, num):
        count = 0
        for i in str(num):
            i = int(i)
            if num % i == 0:
                count+=1
        return count
        