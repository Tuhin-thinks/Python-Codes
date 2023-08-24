# Problem source: https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem4816/1
# input:
#  The input is represented by two things, the first is ‘N’ which
#  is a number of cells in the given board, second is an array ‘move[0…N-1]’ of size N.
#  An entry move[i] is -1 if there is no snake and no ladder from i,
#  otherwise move[i] contains index of destination cell for the snake or the ladder at i.

# output: Minimum number of dice throws required to reach the destination cell from the source or the 1st cell.

class QueueEntry:
    def __init__(self):
        self.v = 0
        self.dist = 0


class Solution:
    def minThrow(self, N, arr):
        q = []
        qe = QueueEntry()
        visited = [False] * N+1
        q.append(qe)

        mat = [-1] * 30
        for i in range(0, 2*N, 2):
            mat[arr[i]] = arr[i+1]

        while q:
            qe = q.pop(0)
            v = qe.v
            if v == 30:
                break

            for j in range(v+1, 7):
                if j > 30:
                    break
                if visited[j] == 0:
                    a = QueueEntry()
                    a.dist = qe.dist + 1

                    if mat[j] != -1:
                        a.v = mat[j]
                    else:
                        a.v = j

                    q.append(a)

        return qe.dist


# code here


# {
# Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2 * N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.minThrow(N, arr))
