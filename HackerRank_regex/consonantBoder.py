"""hackerrank problem link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem"""

import re

v = "aeiou"
c = "^aeiou+-"

# using +ve lookahead
pattern = "[%s]([%s]{2,})(?=[%s])" % (c,v,c)
print("final pattern:", pattern)

if __name__ == '__main__':
    s = input()
    if re.search(pattern, s, re.I):
        res = re.findall(pattern, s, flags=re.IGNORECASE)
        print("\n".join(res))
    else:
        print(-1)
