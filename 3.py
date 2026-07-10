# Logic
"""
n = 1234
we want 4321 as output.
if we take last digit 4 from 1234 and do 4*10+3 = 43
now take previous result 43 and do 43*10+2 = 432
now take previous result 432 and do 432*10+1 = 4321

"""
# Code
class Solution:
    def reverseNumber(self,n:int) ->int:
        n = 1234
        num = n
        result = 0
        
        while num>0:
            last_digit = num % 10
            result = (result*10)+last_digit
            num //10
        return result
# TC, SC
"""
TC: since we have floor division //10 so TC = log10 (N)
SC: depends on number of variables. so Constant sapce. SC = O(1)
"""