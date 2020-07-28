"""
The Mad King arrested Shil's comrades for
participating in a rebellion against the King. Instead of punishing them
 with death, the King decided to play the Game of survival with them.
The game is played as follows:

All the N people are forced to stand in a line.
Now the king randomly chooses  any two persons standing next to each other in line and kills the one having lower strength.
King keeps on performing step 2 until there are only 2 survivors.
The Last two survivors are forgiven for their crimes and are free to go.

As Shil is worried for his comrades, he wants to find out the ones
who could survive - at least, one out of all the possible games.
Given N integers denoting the strengths of comrades, you must print the position of comrades who could survive at least one Game.
Input format:
The first Line of input consists of an integer N denoting the total number of comrades. The next line consists of N integers S1, S2 , .....   SN  denoting the strength of comrades standing in a line. Si denotes the strength of ith comrade standing in a line. The strengths of all the comrades will be distinct.
Output format:
Print the positions of comrades standing in line who could be one of the
 two possible survivors in any possible game. You must print the
positions in an increasingly sorted manner.
Constraints:
3 ≤ N ≤ 105
1 ≤ Si ≤ 109
"""
import logging


# logging.basicConfig(level=logging.INFO)
def survive(line, survivors, main_line):
    logging.info('line=', line)
    if len(line) <= 2:
        logging.info(f"main line={main_line}")
        for ij in line:
            elem = main_line.index(ij) + 1
            logging.info(f"adding {elem}[{ij}] to survivors.")
            survivors.add(elem)
        return list(survivors)
    else:
        for i in range(len(line) - 1):
            a = line[i]
            b = line[i + 1]
            if a > b:  # kill b
                new_line = line.copy()
                del new_line[i + 1]
            else:
                new_line = line.copy()
                del new_line[i]
            logging.info('new_line=', new_line)
            surv = survive(new_line, survivors, main_line)
            logging.info(surv)
            for x in surv:
                survivors.add(x)
    return list(survivors)


t = int(input())
i = 0
while i < t:
    N = int(input())
    strength = list(map(int, input().split()))
    result = survive(strength, set(), strength)
    print(' '.join(list(map(str, result))))
    i += 1
