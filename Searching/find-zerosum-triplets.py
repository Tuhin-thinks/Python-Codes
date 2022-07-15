def findTriplets(arr, n):
    sorted_arr = sorted(arr)

    for index1 in range(n):
        index2 = index1+1
        index3 = n-1
        while index2 < index3:
            sum_ = sorted_arr[index1] + sorted_arr[index2] + sorted_arr[index3]
            if sum_ == 0:
                return True

            if sum_ > 0:
                index3 -= 1
            elif sum_ < 0:
                index2 += 1
    return False
