"""
Problem link: https://www.hackerearth.com/problem/algorithm/maximum-profit-5-c3c2ce7c/
HackerEarth january easy 21
"""

# Write your code here
t = int(input())  # test cases

while t:
    n, k = list(map(int, input().split()))
    coins = list(set(map(int, input().split())))
    coins_sorted = sorted(coins)
    max_sum = 0
    for i in range(len(coins_sorted)-1,-1,-1):
        if k:
            max_sum += coins_sorted[i]
            k -= 1
    print(max_sum)
    t -= 1