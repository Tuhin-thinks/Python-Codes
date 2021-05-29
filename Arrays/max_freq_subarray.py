from collections import Counter

def find_sub_array_length(nr, arr_list):
    index_f, index_l = arr_list.index(nr), len(arr_list) - arr_list[::-1].index(nr)
    return index_l - index_f


def find_shortest_sublist(freq_list, nr_array, max_freq):
    min_len = None
    for elem, freq in freq_list:
        sub_array_length = find_sub_array_length(elem, nr_array)
        if min_len is None:
            min_len = sub_array_length
        elif sub_array_length < min_len:
            min_len = sub_array_length
    return min_len

def most_frequent_nr(nr_array):
    freq_dict = Counter(nr_array)

    freq_list = sorted(dict(freq_dict).items(), key=lambda x: x[1], reverse=True)
    max_freq = freq_list[0][1]
    freq_list = list(filter(lambda x: x[1] == max_freq, freq_list))
    return freq_list, max_freq

if __name__ == '__main__':

    n = int(input())
    elems = list(map(int, input().split()))
    freq_list, max_freq = most_frequent_nr(elems)
    res = find_shortest_sublist(freq_list, elems, max_freq)
    print(res)