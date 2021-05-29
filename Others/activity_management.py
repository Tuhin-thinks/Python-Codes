"""Statement:You are given n activities with their start and finish times. Select the maximum number of activities
that can be performed by a single person, assuming that a person can only work on a single activity at a time.

References Used:

1. For sorting two arrays based on one array
https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/

Problem statement:
2. https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
"""


def sort_with_ref(f, s):
    map_f = {}
    map_s = {}
    for i in range(len(f)):
        map_f[i] = f[i]
    for i in range(len(s)):
        map_s[i] = s[i]
    sorted_f = []
    new_s = []
    for k, v in sorted(map_f.items(), key=lambda x: x[1]):
        sorted_f.append(v)
        new_s.append(map_s[k])
    return new_s, sorted_f


def main(s, f):
    m, n = len(s), len(f)
    if sorted(f) == f:
        pass
    else:
        s, f = sort_with_ref(f, s)

    ind = 0
    print(s[ind], f",start index=[{ind}]")  # first activity always selected
    ind += 1
    previous_activity = f[ind - 1]

    while ind < m:
        """If the start time of this activity is greater than or equal to the finish time of previously selected 
        activity then select this activity and print it. """

        this_activity = s[ind]
        if this_activity >= previous_activity:
            previous_activity = s[ind]
            print(s[ind],f",start index=[{ind}]")
        ind += 1


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
print("Possible Tasks:")
main(s, f)
