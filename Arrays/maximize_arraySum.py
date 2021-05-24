def solve(arr, max_sum=0):
    if len(arr) == 1:
        max_sum += arr[0]
        print(max_sum)
        return
    elif len(arr) == 0:
        print(max_sum)
        return
    
    max_elem = max(arr)
    elem_index = arr.index(max_elem)
    if len(arr) > 1 and elem_index == 0 :
        max_elem = max(arr[1:])
        elem_index = arr.index(max_elem)
    max_sum += max_elem
    print(f"selected: {max_elem}, removed: {arr[elem_index-1]}")
    del arr[elem_index]
    del arr[elem_index-1]
    print("arr now:", arr)
    solve(arr, max_sum)

if __name__=='__main__':
    test_cases=int(input())
    for i in range(test_cases):
        size = int(input())  # take size of the array
        arr_elems = list(map(int, input().split()))  # take the array elements
        solve(arr_elems)