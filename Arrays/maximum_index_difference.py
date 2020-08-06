#Complete this function
def maxIndexDiff(arr, n): 
    ##Your code here
    max_diff = 0
    for i in range(n-1):
        prev = arr[i]
        for j in range(i+1,n):
            elem = arr[j]
            print(f'i={i},j={j},prev={prev},elem={elem}')
            index_diff = j - i
            print("Index diff = ",index_diff)
            if index_diff > max_diff and prev >= elem:
                print("here")
                max_diff = index_diff.copy()
            print(f'max_diff={max_diff}')
    return max_diff

if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxIndexDiff(arr,n))
        t -= 1