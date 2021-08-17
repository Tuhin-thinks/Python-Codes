import re

targetSum = 50

data = [
        ('Theory of Computation', 7.5),
        ('Compiler Design', 2.75),
        ('Computer Organization & Architecture', 9.0),
        ('Programming & Data Structures', 10.5),
        ('Algorithms', 8.0), ('Digital Logic', 5.25),
        ('Operating System', 9.0),
        ('General Aptitude', 15.0),
        ('Computer Networks', 7.5),
        ('Soft. Engg/ Web Technology', 1.5),
        ('Engineering Maths', 14.75),
        ('Database Management Systems', 7.5)
        ]

        
copy = lambda x: x[::]
append = lambda x, y: [tuple(sorted([*l, y])) for l in x]
sortedTuple = lambda x: tuple(sorted(x))

def generate_short_string(string):
    new_string = re.sub("[^\w\s]", '',string, re.DOTALL)
    new_string = re.sub('(\s)\1+', ' ', new_string, re.DOTALL)
    return ''.join([words[0].upper() for words in new_string.split()]) + '.'

        
def allSumstoN(arr, targetSum, memory={}):
    global count
    if targetSum <= 0: return [tuple()]
    resInMem = memory.get(sortedTuple(arr), None)
    if resInMem:
        if targetSum<=resInMem[0]:
            return resInMem[1]
        
    result = set()
    for index, val in enumerate(arr):
        remainder = targetSum-val[1]
        copyArr = copy(arr)
        copyArr.pop(index)
        remainderOptions = allSumstoN(copyArr, remainder, memory)
        for option in append(remainderOptions, val):
            result.add(option)
    
    memory[sortedTuple(arr)] = [targetSum, result]
    
    return result
    
if __name__ == '__main__':
    res = allSumstoN(data, targetSum)

    n_results = int(input("Show how many results:"))
    print()

    for i in data:
        print(f"{i[0]} -> {generate_short_string(i[0])}")
    
    print()
    print(''.center(50, '='))
    print()

    for sl, combo in enumerate(res, start=1):
        items = []
        sum = 0
        if sl > n_results:
            break
        for item in combo:
            items.append(generate_short_string(item[0]))
            sum += item[1]
        items_string = ' + '.join(items)
        print(f"{sl}. {items_string}" + f"| count=({len(items)}) | sum={sum}\n".ljust(10).rjust(25))