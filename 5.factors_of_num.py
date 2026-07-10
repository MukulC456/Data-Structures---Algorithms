# Logic
"""
if there is a number num then there will be no factors of num after num//2 (floor div)
except the num itslef.
SO we wil use for loop to iterate from 1 to num//2 and keep storing the factors
in a list. 
Since num is a factor itself so we will use append function for that
count the number of fators we got in the list and output that.
"""
# Code
class Solution:
    def findFactors(self, n:int) -> int:
        n = 60
        num = n

        my_list = []
        my_list.append(num)
        count = 0
        for i in range(1, (num//2)+1):
            if num%i== 0:
                my_list.append(i)
                count += 1
        # now we count the number of factors 
        return (count+1) 

# TC,SC
"""
Time complexity is TC = O(N/2) or we can write O(N)
Space complexity SC = O(k), where k is the number of factors obtained from list
""" 