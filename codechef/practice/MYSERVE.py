# cook your dish here
t = int(input())
while t:
    p, q = map(int, input().split())

    tot_score = p + q
    alice_condition = (tot_score % 4 == 0) or ((tot_score - 1) % 4 == 0)
    bob_condition = ((tot_score - 2) % 4 == 0) or ((tot_score - 3) % 4 == 0)
    if alice_condition:
        print("Alice")
    else:
        print("Bob")

    t -= 1
