"""
Problem statement: https://www.codechef.com/LRNDSA01/problems/CARVANS
"""

def calculate(n, max_speeds):
    max_speed_count = 0
    lowest_so_far = -1
    for speed in max_speeds:
        if lowest_so_far == -1:
            lowest_so_far = speed
            max_speed_count += 1
            continue
        if speed <= lowest_so_far:  # cars having speed eqauls to or lesser than the lowest speed so far, are moving at their max speed.
            lowest_so_far = speed
            max_speed_count += 1
    return max_speed_count


if __name__ == '__main__':
    T = int(input())  # input number of test cases.

    for i in range(T):
        N = int(input())  # enter number of cars
        max_car_speeds = list(map(int, input().split()))
        res = calculate(N, max_car_speeds)
        print(res)


    