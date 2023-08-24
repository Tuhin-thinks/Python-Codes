class Solution:
    def longestCommonPrefix(self, arr, n):
        common_prefix = min(arr)
        filtered = list(filter(lambda x: len(x) >= len(common_prefix), arr))
        ans = ""
        for idx in range(len(common_prefix)):
            for el in filtered:
                if el[idx] == common_prefix[idx]:
                    continue
                else:
                    return ans or "-1"

            ans += common_prefix[idx]
        return ans or "-1"


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
