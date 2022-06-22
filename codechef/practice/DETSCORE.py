"""Problem link: https://www.codechef.com/submit-v2/DETSCORE"""

t = int(input())
while t:
    x, n = map(int, input().split())

    print(x // 10 * n)  # since given, x is a multiple of 10

    t -= 1
