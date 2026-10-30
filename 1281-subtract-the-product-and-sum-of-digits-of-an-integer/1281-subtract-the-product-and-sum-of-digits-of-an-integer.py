class Solution(object):
    def subtractProductAndSum(self, n):
        sum_digit = 0
        product = 1
        while n>0:
            last_digit = n%10 #give last digit
            sum_digit = sum_digit + last_digit #sum 
            product = product * last_digit     #product
            n = n//10
            
        return product - sum_digit
        