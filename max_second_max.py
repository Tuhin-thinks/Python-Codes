def largestAndSecondLargest(sizeOfArray, arr):
    if sizeOfArray < 2:
        return [arr[0], -1]
    else:
        maxx, second_max = sorted(arr)[-1], sorted(arr)[-2]
        if maxx == second_max:
            set_arr = list(sorted(set(arr)))
            if len(set_arr) > 1:
                return [set_arr[-1], set_arr[-2]]
            else:
                return [set_arr[-1], -1]
        else:
            return [maxx, second_max]


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        sizeOfArray = int(input())
        arr = [int(x) for x in input().split()]
        li = largestAndSecondLargest(sizeOfArray, arr)
        for val in li:
            print(val, end=" ")
        print()
        t -= 1
