# Problem source: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
# Max sub array with 0 sum

class Solution:
    def maxLen(self, n, arr):
        sum_dict = {-1: 0}
        pre_sum = 0
        max_arr_len = 0
        for idx, el in enumerate(arr):
            pre_sum += el
            if pre_sum in sum_dict:
                max_arr_len = max(max_arr_len, idx - sum_dict[pre_sum])
            else:
                sum_dict[pre_sum] = idx
        return max_arr_len


# {
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n, arr))
