def is_anagram(subject, anagram):
    if len(subject) != len(anagram):
        return False  # Anagram must consist same number of letters.

    list2 = list(subject)  # To convert the string into a list.
    for x in anagram:
        try:
            list2.remove(x)  # Remove this letter because it has been "used up".
        except ValueError:
            return False  # It is not anagram if the letter is not found in the list.

    # return len(list2) == 0  # <-- This is redundant.
    return True


if __name__ == '__main__':
    words = dict()
    limit = 1_50_000
    with open('/home/tuhin190211/Documents/python_singles/help/words_alpha.txt') as f:
        # words = f.read().splitlines()  # f.readlines()
        count = 0
        for line in f:
            # words.append(line.strip())
            words[count] = line.strip()
            if count == limit:
                break
            count += 1

    length2 = 12  # <-- Get this from user input.
    N = len(words)

    for i in range(N):
        if len(words[i]) == length2:
            for j in range(i + 1, N):
                if is_anagram(words[i], words[j]):
                    print("{}, {}".format(words[i], words[j]))
