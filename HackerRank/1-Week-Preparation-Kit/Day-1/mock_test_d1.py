"""
Find the media element of the array
"""


def findMedian(arr):
    """
    find median element from the arr
    :param arr:
    :return:
    """
    len_arr = len(arr)
    if len_arr > 1:
        return list(sorted(arr))[len_arr // 2]
    else:
        return arr[0]
