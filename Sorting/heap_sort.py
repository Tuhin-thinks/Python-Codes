"""
Knowledge Source: 
Learned from book: "Introduction to algorithms"
By cormen.

Details about heap sort:

- running time is O(N Log N)
"""
def heapify(arr, n, i):
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range((n//2)-1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [10,40,11,19,70,60,25]
heapsort(arr)
n = len(arr)
print("sorted array is:")
for i in range(n):
    print(arr[i], end="," if i<n-1 else "\n")

