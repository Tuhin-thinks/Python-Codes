def countingSort(arr):
    """return the number of times each element appears in the array"""
    max_val = max(arr)
    size_of_array = 100 if max_val <= 100 else max_val  # as given constraint array must have least 100 elements
    frequency_array = [0] * size_of_array
    for i in arr:
        frequency_array[i] += 1

    return frequency_array


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    # ----------- for self validations -------------
    with open("../output.txt", "w") as f:
        f.write(" ".join(map(str, result)))
