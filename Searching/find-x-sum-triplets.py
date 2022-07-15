def find3Numbers(A, n, X):
    sorted_arr = sorted(A)

    for index1 in range(n):
        index2 = index1 + 1
        index3 = n-1
        while index2 < index3:
            sum_ = sorted_arr[index1] + sorted_arr[index2] + sorted_arr[index3]
            if sum_ == X:
                return True

            if sum_ < X:
                index2 += 1
            elif sum_ > X:
                index3 -= 1

    return False
