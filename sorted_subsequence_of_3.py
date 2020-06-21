


def find3number(A, n):
    # code here
    greater=[0]*n
    smaller=[0]*n
    smaller[0]=-1
    greater[n-1]=-1
    s,g=0,n-1
    for i in range(1,n):
        if A[i]<=A[s]:
            s=i
            smaller[i]=-1
        else:
            smaller[i]=s
    for i in range(n-2,-1,-1):
        if A[i]>=A[g]:
            g=i
            greater[i]=-1
        else:
            greater[i]=g
    for i in range(n):
        if smaller[i]!=-1 and greater[i]!=-1:
            return [A[smaller[i]],A[i],A[greater[i]]]
    return []



#{
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, lis, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    lis = find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis)!=0 and len(lis)!=3:
        print(-1)
        continue
    if len(lis)==0:
        print(0)
    elif lis[0]<lis[1] and lis[1]<lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)

# } Driver Code Ends
