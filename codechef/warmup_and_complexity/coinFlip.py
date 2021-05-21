if __name__ == '__main__':
    T = int(input())  # enter test cases
    for i in range(T):
        G = int(input())  # no. of games played
        for j in range(G):
            i,n,q = list(map(int, input().split()))  # 3 space separated integers
