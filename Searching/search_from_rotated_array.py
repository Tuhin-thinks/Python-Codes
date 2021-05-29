"""Search in a
Sorted and Rotated
Array
Given
a
sorted and rotated
array
A
of
N
distinct
elements
which is rotated
at
some
point, and given
an
element
K.The
task is to
find
the
index
of
the
given
element
K in the
array
A.

Input:
The
first
line
of
the
input
contains
an
integer
T, denoting
the
total
number
of
test
cases.Then
T
test
cases
follow.Each
test
case
consists
of
three
lines.The
first
line
of
each
test
case
contains
an
integer
N
denoting
the
size
of
the
given
array.The
second
line
of
each
test
case
contains
N
space - separated
integers
denoting
the
elements
of
the
array
A.The
third
line
of
each
test
case
contains
an
integer
K
denoting
the
element
to
be
searched in the
array.

Output:
For
each
test
case, print
the
index(0
based
indexing) of
the
element
K in a
new
line,
if K does not exist in the array then print -1.

User
Task:
Complete
Search()
function and
return the
index
of
the
element
K if found in the
array.If
the
element is not present, then
return -1.

Expected
Time
Complexity: O(log
N).
Expected
Auxiliary
Space: O(1).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 ≤ Ai ≤ 108
1 ≤ K ≤ 108

Example:
Input:
3
9
5
6
7
8
9
10
1
2
3
10
3
3
1
2
1
4
3
5
1
2
6

Output:
5
1
-1

Explanation:
Testcase
1: 10 is found
at
index
5.
Testcase
2: 1 is found
at
index
1.
Testcase
3: 6
doesn
't exist.

"""


def Search(arr,n,k):
    #code here
    if k in arr:
        return arr.index(k)
    else:
        return -1



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends