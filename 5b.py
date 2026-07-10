# Logic
"""
Let's understand by example. for number = 36
if we take sqaure root of num we get 6. 
It means we will iterate our for loop only till 6
from 1 to 6 whichever number is factor of 36 will be written
after getting factors from 1 to 6. it will be paired with (36//that factor from 1 to 6)
In this way we get 2 numbers simulataneously in a single operation
i  num//i
1--36
2--18
3--12
4--9
6--6
once we get both i and num//i equal like here 6 and 6 we will stop
we will store pair of values obtained in a single operation in our list and 
at last count the number of factors. 
This is Optimal Solution
"""
# Code
class Solution:
    def findFactors(self, n:int) ->int:
        n = 36
        num = n

        my_list = []
        count = 0

        for i in range(1, int((num)**(1/2)) + 1):
            if num%i == 0:
                my_list.append(i)
                count += 1
                if num//i != i:
                    my_list.append(num//i)
                    count += 1
        return(count)

# TC,SC
"""
TC will be O(N^(1/2))
SC will be O(k) where k is number of factors in list
"""