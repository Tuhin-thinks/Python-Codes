class Solution:
    def subArraySum(self, arr, n, s):
        sum_dict = {}
        pre_sum = 0
        for id_i in range(n):
            pre_sum += arr[id_i]
            if pre_sum > s:
                k = pre_sum - s
                idx = sum_dict.get(k)
                if idx:
                    return [idx+1, id_i+1]
            elif pre_sum == s:
                return [1, id_i+1]
            sum_dict[pre_sum] = id_i+1
        return [-1]


# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)

        for i in ans:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
