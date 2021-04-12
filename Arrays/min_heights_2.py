class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        result = arr[-1] - arr[0]
        
        for i in range(n):
            if arr[i] >= k:
                max_elem = max(arr[i-1] + k, arr[n-1] - k)
                min_elem = min(arr[0] + k, arr[i] - k)
                
                result = min(result, max_elem - min_elem)
            else:
                continue
        return result

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1