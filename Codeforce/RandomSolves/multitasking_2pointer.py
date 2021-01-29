"""
problem link: https://codeforces.com/problemset/problem/384/B
"""
if __name__ == '__main__':
    # n, m, k = list(map(int, input().split()))
    n, m, k = 2, 5, 0
    arrays = [[1, 3, 2, 5, 4],
              [1, 4, 3, 2, 5]]
    # arrays = []
    # for i in range(n):
    #     array = list(map(int, input().split()))
    #     arrays.append(array)

    sort_steps = []

    i, j = 0, m - 1
    while i < j:
        print(i, j)
        x = 0
        while x < n:
            array = arrays[x]
            if array[i] < array[j] and k == 1:
                array[i], array[j] = array[j], array[i]
                sort_steps.append([array[i], array[j]])
                print(f'\t[+1]')
            elif array[i] > array[j] and k == 0:
                array[i], array[j] = array[j], array[i]
                sort_steps.append([array[i], array[j]])
                print(f'\t[+1]')
            x += 1
        if i < m // 2:
            i += 1
        if i == m // 2:
            i = 0
            j -= 1

    print(f"\n\n{sort_steps}")
