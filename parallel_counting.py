def countEleLessThanOrEqual(arr1, n1, arr2, n2):
    # sorting both the arrays in increasing order
    sorted_arr2 = sorted(arr2)
    # sorted_arr1 = sorted(arr1)

    result = []
    # traversing the first array
    for elem in arr1:
        l = 0
        h = n2 - 1
        while(l <= h):
            mid = int((l + h) / 2)
            if(sorted_arr2[mid] <= elem):
                l = mid + 1;
            else:
                h = mid - 1
        # store the required index
        result.append(h+1)
    return result



#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())

    for tcs in range(t):

        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]

        res = countEleLessThanOrEqual(arr1,n1,arr2,n2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
