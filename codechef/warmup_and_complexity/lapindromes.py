t = int(input())
while t:
    test_string = input()
    middle_point = len(test_string)//2
    if len(test_string) % 2 == 0:  # string length is even
        f_half = test_string[:middle_point]
        s_half = test_string[middle_point:]
    else:
        f_half = test_string[:middle_point]
        s_half = test_string[middle_point+1:]
    if sorted(f_half) == sorted(s_half):
        print('YES')
    else:
        print('NO')
    t -= 1
