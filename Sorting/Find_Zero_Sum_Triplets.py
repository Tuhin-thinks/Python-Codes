def findTriplets(arr, n):
    for i in range(n - 1):
        # Find all pairs with sum
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                return 1
            else:
                s.add(arr[j])
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(findTriplets(a, n))
