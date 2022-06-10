import time
from collections import Counter

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
c = Counter(numbers)

# input 2 sets, each containing m integers
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

time_a = time.perf_counter_ns()
happiness = 0
for num, freq in c.items():
    if num in set_a:
        happiness += freq
    if num in set_b:
        happiness -= freq
time_b = time.perf_counter_ns()
print(happiness)
print(f"Time required: {(time_b - time_a) / 10**6 :.03f}ms")
