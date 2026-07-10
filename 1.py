"""
Logic:

if we have a number say num = 5873. If we want to extract digits 3,7,8,5 then
num = 5873 % 10 == 3
5873 //10 == 587 then 587 % 10 == 7
587 //10 == 58 then 58 % 10 == 8
5 //10 == 0 then 5 % 10 == 5

"""
num = int(input("Enter number: "))
while num>0:
    last_digit = num % 10
    print(last_digit)
    num = num //10