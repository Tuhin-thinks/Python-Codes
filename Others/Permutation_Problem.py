"""
How many different ways can you arrange 3 digits to find the product of a 2-digit number and a 1-digit number?
"""

# find the smallest 3 digit number that is a multiple of a two digit number and an one-digit number
# it is 100 (= 2 x 50)
# and maximum is 891 (=9*99)

# run a loop from 100 to 891 to find the other 3 digits number between them, which are multiples of ...

multiples = []
for i in range(100,892):
    for j in range(2,10):
        if i % j == 0:
            multiples.append(i)
            break
# print(multiples)  # these multiples are the possible 3-digit numbers
print(f'Total {len(multiples)} multiples are available.')
# now we have to find number of ways, each digit place can be arranged
digit = {}
for number in multiples:
    for pos,digits in enumerate(str(number)):
        if digits in digit.keys():
            digit[digits] = digit[digits] + 1
        else:
            digit[digits] = 1
print(digit)
# thus our answer should be 610