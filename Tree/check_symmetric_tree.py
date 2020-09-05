
# return true/false denoting whether the tree is Symmetric or not
def condition(root1, root2):
    if root1 == root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return (condition(root1.left, root2.right) and condition(root1.right, root2.left))

    return False


def isSymmetric(root):
    return condition(root, root)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip =list(map(str ,s.split()))

    # Create the root of the tree
    root =Node(int(ip[0]))
    size =0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size +1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0 ]
        q.popleft()
        size=size -1

        # Get the current node's value from the string
        currVal=ip[ i ]

        # If the left child is not null
        if(currVal!="N ") :
            # Create the left child for the current node
            currNode.left=Node (int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size +1
        # For the right child
        i=i+1
        if(i>= len(ip)):
            break
        currVal=ip[ i ]

        # If the right child is not null
        if(currVal!="N ") :
            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size +1
        i=i+1
    return root


if __name__=="_ _m ain__":
    t=int ( input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if isSymmetric(root):
            print("True")
        else:
            print("False")

# } Driver Code Ends