# Problem source: https://leetcode.com/problems/count-servers-that-communicate/
# Servers that communicate

from typing import List


class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        discovered = set()

        for i in range(rows):
            has_server = 0
            temp_discovery = None
            for j in range(cols):
                el = grid[i][j]
                if el:
                    if has_server:
                        discovered.add((i, j))
                        if temp_discovery:
                            discovered.add(temp_discovery)
                            temp_discovery = None
                    else:
                        temp_discovery = (i, j)
                    has_server = 1
                    found_servers = self.discover_cols(i + 1, j, grid, discovered, rows, cols)
                    if found_servers and temp_discovery:
                        discovered.add(temp_discovery)
                        temp_discovery = None

        return len(discovered)

    def discover_cols(self, row, col, grid, discovered, rows, cols):
        found_servers = 0
        for c in range(row, rows):
            el = grid[c][col]
            if el == 1:
                discovered.add((c, col))
                found_servers = 1

        return found_servers


if __name__ == '__main__':
    ob = Solution()
    rows, cols = input().split(" ")
    _grid = []
    for row in range(int(rows)):
        line = input()
        _grid.append([int(x) for x in line.split(" ")])
    print(ob.countServers(_grid))
