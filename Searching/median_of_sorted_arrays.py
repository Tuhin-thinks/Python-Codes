"""
Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines. First line will contain m followed by m space separated integers for array1. Second line will contain n followed by n space separated integers for array2.

Output:
Print the median of the two sorted arrays.

User Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as input and returns their median.

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 200
0 <= m,n <= 10000
1 <= array1[i], array2[i] <= 10^5

Example:
Input:
2
3 1 5 9
4 2 3 6 7
2 4 6
4 1 2 3 5

Output:
5
3.5

Explanation:
Case 1: The middle element for {1,2,3,5,6,7,9} is 5
Case 2: The middle 2 elements for {1,2,3,4,5,6} are 3 and 4 and their average is 3.5
"""

def MedianOfArrays(array1, array2):
    new_array = array1.copy()
    new_array.extend(array2)
    new_array = sorted(list(new_array))
    length = len(new_array)
    if length % 2 != 0:  # odd
        median_index = int((length + 1) / 2) - 1
        median_element = new_array[median_index]
        return median_element
    else:
        median_index_1 = int(length / 2) - 1
        median_index_2 = median_index_1 + 1
        median_element_1 = new_array[median_index_1]
        median_element_2 = new_array[median_index_2]
        result = (median_element_2 + median_element_1) / 2
        if result - int(result) != 0:
            return result
        else:
            return int(result)


# {
#  Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        array1, array2 = arr1[1:], arr2[1:]

        print(MedianOfArrays(array1, array2))

# } Driver Code Ends