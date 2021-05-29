"""
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).
"""

import re

def strstr(s,x):
    flag = 1
    for i in re.finditer(x,s):
        return i.span()[0]
        flag = 0
    if flag == 1:
        return -1

print(strstr("GeeksForGeeks", "For"))