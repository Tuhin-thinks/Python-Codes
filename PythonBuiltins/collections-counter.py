"""
problem solved: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
"""
from collections import Counter

X = int(input())  # number of shoes
shoe_sizes = list(map(int, input().split()))
N = int(input())  # number of customers
shoe_counter = Counter(shoe_sizes)
price_earned = 0
for _ in range(N):
    req_size, price = map(int, input().split())
    if shoe_counter[req_size] > 0:
        shoe_counter[req_size] -= 1
        price_earned += price

print(price_earned)
