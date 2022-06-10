from collections import Counter


def main(string):
    c = Counter(string)
    max_display = 3
    for letter, freq in reversed(sorted(c.items(), key=lambda xy: (xy[1], -1 * ord(xy[0])))):
        print(letter, freq)
        max_display -= 1
        if max_display <= 0:
            break


if __name__ == '__main__':
    s = input()
    main(s)
