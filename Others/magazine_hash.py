#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    checked = set()
    note_hash = {w: note.count(w) for w in note}
    for word, freq in note_hash.items():
        if word not in checked:
            if magazine.count(word) >= freq:
                checked.add(word)
            else:
                print("No")
                return 0
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
