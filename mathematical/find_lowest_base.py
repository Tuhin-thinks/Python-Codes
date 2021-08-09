"""
Program to find the minimum base, where a entered decimal number can be represented using all same digits
"""

see_steps = True


def main(m):
    def get_n():
        """
        function to determine max number of times a decimal number has to be divided to get the Quotient as 0
        :return:
        """
        quo = m
        Xn = 1
        while quo > 0:  # can also be written as while quo, this is beginner friendly
            quo //= b ** Xn  # performing integer division
            Xn += 1
        return Xn

    def try_n(n):
        """
        try to find if all digits for the base b representation of decimal number m are same.
        :param n: the n, determined by the get_n function
        :return: boolean, the common digit (only useful when boolean part is True)
        """
        last_quo = m // (b ** n)  # this should be 0
        K = m % b
        if last_quo == 0:
            pass
        else:
            return False, K

        for i in range(1, n):
            if ((m // b ** i) % b) == K:
                pass
            else:
                resid = (m // b ** i) % b
                if see_steps:
                    print(f"\t{resid=} != {K}, at {i=}")
                return False, K
        return True, K

    for b in range(2, 10):  # iterate from 2 to 10 as given base is 10
        max_n = get_n()

        if see_steps:
            print(f"\nBase: {b}\nMax steps: {max_n}")

        res, common = try_n(max_n)

        if res:  # check if the returned boolean part is True
            if not see_steps:
                print(f"\nBase: {b}\nMax steps: {max_n}")
            print("Minimum base is:", b, f"Base ({b}) representation: {f'{common}' * max_n}")
            return

    print(f"{m} cannot be represented using all same digits.")


if __name__ == '__main__':
    main(int(input("Enter  the decimal number:")))

# @github.com/tuhin-thinks
