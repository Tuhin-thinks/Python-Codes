'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
            # factor_count += 1
    if n > 1:
        factors.append(n)
        # factor_count += 1
    return len(set(factors))


def check_prime(num):
    if num > 1:
        flag = 0
        for i in range(2,num//2):
            if num // i == 0:
                flag = 1
                break
                # return False
        if flag == 0:
            return True
        else:
            return False
    else:
        return False
    

t = int(input())
while t:
    a,b = tuple(map(int, input().split()))
    lcm = compute_lcm(a,b)
    print("LCM=",lcm)
    count = prime_factors(lcm)
    print(f"count of prime factors:",count)
    if check_prime(count):
        print('Yes')
    else:
        print('No')
    t -= 1
