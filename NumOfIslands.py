"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


def numOfIslands(grid):
    no_of_islands = 0
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def checkNeighbour(i, j):
        visited[i][j] = True
        i_off = [-1, 0, 1, 0]
        j_off = [0, -1, 0, 1]

        for k in range(len(i_off)):
            new_i = i + i_off[k]
            new_j = j + j_off[k]
            if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == '1' and not visited[new_i][new_j]:
                checkNeighbour(new_i, new_j)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not visited[i][j]:
                no_of_islands += 1
                checkNeighbour(i, j)

    return no_of_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print("Max Islands", numOfIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print("Max Islands", numOfIslands(grid))
