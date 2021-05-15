import math

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def check_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def find_prime(r):
    for i in r:
        res = check_prime(i)
        if res == True:
            print("prime:", i)
            return i
    return False

def main():
    T = int(input())
    for i in range(T):
        L, R = list(map(int, input().split()))
        lower_prime, higher_prime = find_prime(range(L, R+1)), find_prime(range(R, L-1, -1))
        if lower_prime != higher_prime and False not in {lower_prime, higher_prime}:
            print(higher_prime - lower_prime)
        elif lower_prime == higher_prime and lower_prime is not False:
            print(0)
        else:
            print(-1)

main()