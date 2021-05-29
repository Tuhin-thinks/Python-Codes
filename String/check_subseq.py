''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def check_subseq(V, B):
    new_str = V
    order = []
    index_now = 0
    for c in B:
        index_ = new_str.find(c)
        index_now += index_
        if index_ > -1:
            order.append(index_now)
            new_str = new_str[index_:]
        else:
            return False
    if sorted(order) == order:
        return True
    else:
        return False

def main():
    V = input()  # take input of the virus
    n = int(input())  # number of samples
    for p in range(n):
        B = input()
        if check_subseq(V, B):
            print("POSITIVE")
        else:
            print("NEGATIVE")

main()

