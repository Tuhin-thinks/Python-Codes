class Solution:
    def calculate_jump(self, arr, curr_index, num, path_length=0):
        print("\tsearching index:", curr_index, f"current element:{num}")
        next_index = curr_index + num
        lengths = []
        for index in range(curr_index+1, next_index+1, 1):
            print("next index:", index)
            if curr_index == (len(arr) - 1):
                lengths.append(path_length)
                return lengths
            if index < len(arr):
                elem = arr[index]
                lengths.append(self.calculate_jump(arr, index, elem, path_length + 1))
            else:
                return 0
        print("lengths:", lengths)
        return lengths
    def minJumps(self, arr, n):
        i = 0
        while i < len(arr):
            print("searching index :", i)
            path_length = self.calculate_jump(arr, i, arr[i], 0)
            print(f"returned: {path_length}")
            if path_length:
                return path_length
                i += path_length
            else:
                i += 1
        return i


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)