CIFRE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZαβγδεζ"
# change the CIFRE string to allow for a different maximum base.
# Currently, I chose 42, because this appears to answer most problems ;-)


def b2dec(nums, bas):
    """
    Converts a string representing a number in a specified base, to an int.
    The minimum allowed base is 2, the maximum depends on the number of the
    allowed digit values found in the string CIFRE, currently 42. 
    """
    res = 0
    # print(f"Given: {nums=}, {bas=}")
    if not isinstance(nums, str):
        raise TypeError(f"First argument must be a string. Given <{nums}>")
    if not isinstance(bas, int):
        raise TypeError(f"Second argument must be an integer. Given <{bas}>")
    if bas < 2 or bas > len(CIFRE):
        raise ValueError(f"Base must be an integer in the range 2..{len(CIFRE)}. Given <{bas}>")
    nums = nums.upper()
    # print(f"{res=}")
    for i, c in enumerate(nums[::-1]):
        co = CIFRE.index(c)
        if co >= bas:
            raise ValueError(f'Invalid number string containing <{c}> with base {bas}')
        # print(f"Power={bas ** i}, coeff={co}:") 
        res += ((bas ** i) * co)
        # print(f"{res=}")
    return res

def dec2b(num, bas):
    """
    Converts an integer to a string representing that number in a specified base.
    The minimum allowed base is 2, the maximum depends on the number of the
    allowed digit values found in the string CIFRE, currently 42. 
    """
    res = ""
    # print(f"Given: {num=}, {bas=}")
    if not isinstance(num, int):
        raise TypeError(f"First argument must be an integer. Given <{num}>")
    if not isinstance(bas, int):
        raise TypeError(f"Second argument must be an integer. Given <{bas}>")
    if bas < 2 or bas > len(CIFRE):
        raise ValueError(f"Base must be an integer in the range 2..{len(CIFRE)}. Given <{bas}>")
    # print(f"res = <{res}>")
    while num >= bas:
        # print(f"Remaining={num}:") 
        q, r = divmod(num, bas)
        res += CIFRE[r]
        num = q
        # print(f"{res=}")
    res += CIFRE[num]
    # print(f"final res = {res}")
    # print(f"returning {res[::-1]}")
    return res[::-1]



def main():
    res = -1
    while True:
        num = input("Enter a number, or just Enter to quit: ")
        if num == "":
            print("End of Job!")
            return res
        else:
            num = int(num)
        if num < 0:
            print(f"{num} is negative: not allowed!")
            res = -1
            continue
        if num < 3:
            print(f"{num} in base 10 is <{num}>: problem solved!")
            res = num
            continue
        B = 2
        stop = min(num, len(CIFRE))
        while B <= stop:
            encod = dec2b(num, B)
            test = encod[0]
            if all((x == test for x in encod)):
                print(f"{num} in base {B} is <{encod}>: problem solved!")
                res = B
                break
            B += 1
        else:
            print("No suitable base found!")
            res = -1

if __name__ == "__main__":
    main()
