if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        elements = list(map(int, input().split()))
        element_weight = {}
        flag =0
        for elem in elements:
            if elem not in element_weight.keys():
                element_weight[elem] = 1
                if element_weight[elem] > int(n / 2):
                    print(elem)
                    flag = 1
                    break
            else:
                element_weight[elem] += 1
                if element_weight[elem] > int(n / 2):
                    print(elem)
                    flag = 1
                    break
        if flag == 0:
            print(-1)
