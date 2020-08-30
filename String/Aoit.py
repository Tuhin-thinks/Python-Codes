"""
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

Example 1:

Input:
str = 123
Output: 123

Example 2:

Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.

Your Task:
Complete the function atoi() which takes a string as input parameter and returns integer value of it. if the input string is not a numerical string then returns 1..

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)
"""
def atoi(string):
    # Code here
    if string.strip('-').isdigit():
        return int(string)
    else:
        return -1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(atoi(string))