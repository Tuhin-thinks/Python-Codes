'''
problem statement:
In Byteland they have a very strange monetary system. Each Bytelandian gold
coin has an integer number written on it. A coin n can be exchanged in a bank
into three coins: n/2, n/3 and n/4. But these numbers are all rounded down
(the banks have to make a profit).
You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins. You have one gold coin. What is the maximum amount of American dollars you can get for it?
Input The input will contain several test cases (not more
than 10). Each testcase is a single line with a number n, 0 <= n <= 1 000 000
000. It is the number written on your coin.
Output For each test case output a
single line, containing the maximum amount of American dollars you can make.
Explanation
You can change 12 into 6, 4 and 3, and then change these into
$6+$4+$3 = $13.
If you try changing the coin 2 into 3 smaller coins, you will get
1, 0 and 0, and later you can get no more than $1 out of them.
It is better just to change the 2 coin directly into $2.
'''

# Write your code here
def split(n):
    a,b,c = n//2, n//3, n//4
    return a,b,c

def process(n):
    a,b,c = split(n)
    value = a+b+c
    if value >= n:
        new_value = 0
        value_list = [a,b,c]
        for i in range(len(value_list)):
            x,y,z = split(value_list[i])
            if x+y+z >= value_list[i]:
                new_value += x+y+z
        if new_value > value:
            value = process(new_value)
        else:
            return value
    else:
        return n


if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        print(process(n))
        t -= 1