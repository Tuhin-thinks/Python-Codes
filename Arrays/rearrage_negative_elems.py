"""
source: https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/
"""
class Solution:
    def segregateelements(self, arr, n):
        # ------------ APPROACH WONT WORK IF QUESTION REQUIRES SHIFTING OF ELEMENTS ------------------
        # j = n-1
        # for i in range(n):
        #     print(f"Checking {arr[i]}")
        #     if arr[i] < 0 and i < j:
        #         print(f"\tswapped with :{arr[j]}")
        #         arr[i], arr[j] = arr[j], arr[i]
        #         print(f"\t{arr}")
        #         j -= 1

        # ------------ APPROACH 2 ----------------
        negatives = []
        positives = []
        i = 0
        for elem in arr:
            if elem < 0:
                negatives.append(elem)
            else:
                positives.append(elem)
        arr.clear()
        arr.extend(positives + negatives)

def main():
    T = int(input())

    while T > 0:
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateelements(a, n)
        print(*a)
        
        T -= 1

if __name__ == '__main__':
    main()
    
