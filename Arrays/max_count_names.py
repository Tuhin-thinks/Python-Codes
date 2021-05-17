spam = ["aaa", "aba", "aaa", "aaaa"]
max_count = 0
disputes=list()
for name in spam:
    now_count = spam.count(name)
    if now_count > max_count:
        max_count = now_count
        disputes.clear()
        disputes.append(name)
    elif now_count == max_count:
        disputes.append(name)

if len(disputes) > 1:
    print(sorted(disputes)[-1])  # sort alphabetically
else:
    print(disputes[0])
print(max_count)
