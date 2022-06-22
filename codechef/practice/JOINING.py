t = int(input())
while t:
    n, k = map(int, input().split())

    if k == n or n <= 5:
        print(0)
        t -= 1
        continue

    next_higher_multiple = round(k / 5) * 5
    remaining_candidates = n - next_higher_multiple
    date_changed_for = remaining_candidates // 5 if remaining_candidates >= 5 else 1
    print(date_changed_for)

    t -= 1