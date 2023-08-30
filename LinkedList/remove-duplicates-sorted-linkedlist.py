# Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    prev = None
    curr = head

    while curr:

        if not prev:
            prev = curr

        if curr.data != prev.data:
            prev.next = curr
            prev = curr

        elif curr != prev and curr.data == prev.data:
            prev.next = None  # unlink the duplicated nodes, link back when different data node found

        curr = curr.next

    return head


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

import atexit
import io
import sys


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the
    # linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print('')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        removeDuplicates(a.head)
        a.printList()
# } Driver Code Ends
