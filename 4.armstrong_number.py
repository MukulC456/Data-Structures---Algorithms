# Logic
"""
153 = (3)^3 + (5)^3 + (1)^3 = 1+125+27 = 153
1634 = (4)^4 + (3)^4 + (6)^4 + (1)^4 = 1+1296+81+256 = 1634

sum of digits to the power of number of digits in number
here 2 logics can be used: extraction of last digit and count digits in number

extract the last digit, power it to count digits in num and store result in a 
variable named total. Iterate this process till you get number
"""
# Code
class Solution:
    def armstrongNumber(self,n:int) -> int:
        n = 153

        # find count in number
        num = n
        count = 0
        while num>0:
            count += 1
            num //= 10
        
        num = n # value reset to n

        # last digit**count
        result = 0
        while n>0:
            last_digit = num % 10
            result += last_digit**count
            num //10
        
        return result
# TC,SC
"""
TC: time complexity will be O(log10 (N))
SC: space complexity will be O(1) bcoz it takes constant no. of variables
"""