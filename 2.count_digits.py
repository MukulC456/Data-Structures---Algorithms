"""
Logic1:
num = 5873, digits = 4
num = 165458, digits = 6

num = 5873
count += 1
num //10

num = 587
count += 1
num // 10

num = 58
count += 1
num //10

num = 5
count += 1
num //10

num = 0
loop ends. we have count = 4

Logic2:
int(log 10 (num+1)) = number of digits in num
"""
class Solution:
    def countdigits(self, n:int) -> int:
        num = n
        count = 0
        while num >0:
            count += 1
            num //= 10
        return count
"""
TC: whenever we have N//a floor division in a while loop TC is O(loga (N))
for e.g. here we have n//10 so TC = O(log10 (N))
for n//5 TC will be O(log5 (N))
for n //2 TC  = O(log2 (N))
"""