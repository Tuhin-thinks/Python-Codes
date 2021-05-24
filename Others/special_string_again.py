import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s) -> int:
    # --------------- approach 1 ---------------

    # substr = list(s)
    # substring_count = n
    # for i in range(2, n+1):
    #     for j in range(n):
    #         if (j + i) <= n:
    #             sub = s[j:j + i]
    #             if len(sub) % 2 == 0 and sub == sub[::-1]:
    #                 substring_count += 1
    #                 substr.append(sub)
    #             elif len(sub) % 2 == 1 and sub[:len(sub)//2] == sub[len(sub)//2+1:]:
    #                 substring_count += 1
    #                 substr.append(sub)
    # print(substr)
    # return substring_count

    # --------------- approach 2 -----------------
    count = n
    for x in range(n):
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y + 1:2 * y - x + 1]:
                    count += 1
                break

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("length="))

    s = input("string=")

    result = substrCount(n, s)

    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
