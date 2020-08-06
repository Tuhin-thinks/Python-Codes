"""
Problem statement:
You'll be given 3 integers L, D and X.

Determine min (N) such that L <= N <= D and the sum of it's digits is X
Determine the max (M) such that L <= M <= D and the sum of it's digits is X
"""
def sum_of_digits(num):
    return sum([int(i) for i in list(str(num))])


def trap_escape(L,D,X):
    N,M = -1,-1

    for i in range(L, D+1):
        if sum_of_digits(i) == X:
            N = i
            break
    for i in range(D, L-1, -1):
        if sum_of_digits(i) == X:
            M = i
            break
    print(f"{N}\n{M}")

if __name__ == "__main__":
    # t = int(input("test-cases:"))
    # while t:
    L = int(input())
    D = int(input())
    X = int(input())
    trap_escape(L, D, X)
        # t -= 1