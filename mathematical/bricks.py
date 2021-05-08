def make_bricks(small, big, goal):
    big_rem = goal // 5
    if (goal - (big_rem * 5)) <= small and big_rem <= big:
        return True
    elif big_rem > big and (goal - 5*big <= small):
        return True
    return False

if __name__ == '__main__':
    tests = [
        (1,4,11),
        (3,1,8),
        (3,1,9),
        (3,2,10),
        (3,2,9),
        (3,2,8),
        (6,1,11),
        (6,0,11),
        (0,3,10),
        (3,1,7),
        (1,1,7),
        (2,1,7),
        (1,4,12),
        (7,1,11)
    ]
    for test in tests:
        res = make_bricks(*test)
        print(test, "=", res)