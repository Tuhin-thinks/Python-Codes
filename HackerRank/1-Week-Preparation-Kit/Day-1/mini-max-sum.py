"""
Problem solved: https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-one
"""


def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    print(sum(sorted_arr[:4]), sum(sorted_arr[-4:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
