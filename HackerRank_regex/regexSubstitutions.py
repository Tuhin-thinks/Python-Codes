"""
Problem link: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
"""
import re

def find_and_replace(string: str) -> str:
    if re.search(pattern_or, string):
        return find_and_replace(re.sub(pattern_or, " or ", string))
    elif re.search(pattern_and, string):
        return find_and_replace(re.sub(pattern_and, " and ", string))
    else:
        return string

if __name__ == "__main__":
    pattern_or = r' \|{2} '
    pattern_and = r' \&{2} '
    n = int(input())  # the integer n
    complete_code_text = ""
    while n > 0:
        code_line = input()  # a code line
        complete_code_text += find_and_replace(code_line) + '\n'
        n -= 1

    # when taking input is complete
    print(complete_code_text.strip())
