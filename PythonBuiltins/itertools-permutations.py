from itertools import permutations

sk = input().split()

s = sk[0]
k = int(sk[1])

perms = permutations(s, k)
perms_list = sorted([''.join(p) for p in perms])
print('\n'.join(perms_list))