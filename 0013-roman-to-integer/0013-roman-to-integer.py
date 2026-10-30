class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        def convert(x):
            return values[x]

        n = list(map(convert,s))
        total = 0
        for i in range(len(n)-1):
            if n[i]<n[i+1]:
                total = total-n[i]
            else:
                total = total+n[i]
        total = total+n[-1]
        return total


        




