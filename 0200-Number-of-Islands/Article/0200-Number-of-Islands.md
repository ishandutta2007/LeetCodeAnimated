# LeetCode Illustration | 200. Number of Islands

## Title description

Given a 2D grid consisting of `'1'` (land) and `'0'` (water), count the number of islands. An island is surrounded by water and is connected by adjacent land masses either horizontally or vertically. You can assume that all four sides of the grid are surrounded by water.

**Example 1:**

```
enter:
11110
11010
11000
00000

Output: 1
```

**Example 2:**

```
enter:
11000
11000
00100
00011

Output: 3
```

## Question analysis

The main idea of ​​​​this question is depth-first search. Every time you go to a grid with a 1, search the entire island.

The grid can be viewed as an undirected graph structure, with each grid adjacent to its four grids above, below, left, and right. If the coordinates of the four adjacent grids are legal and they are land, you can continue searching.

When doing depth-first search, be careful to avoid repeated traversals. We can change the land that has been traversed to 2, so that when we encounter 2, we will know that we have already traversed this grid and will not repeat the traversal.

Every time a land grid is encountered, a depth-first search is performed. Finally, after several searches, the number of islands is known.

## Animation understanding

![](../Animation/Animation.gif)

## Reference code

```Java
class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == '1') {
                    dfs(grid, r, c);
                    count++;
                }
            }
        }
        return count;
    }
    
    void dfs(char[][] grid, int r, int c) {
        if (!(0 <= r && r < grid.length && 0 <= c && c < grid[0].length)) {
            return;
        }
        if (grid[r][c] != '1') {
            return;
        }
        grid[r][c] = '2';
        dfs(grid, r - 1, c);
        dfs(grid, r + 1, c);
        dfs(grid, r, c - 1);
        dfs(grid, r, c + 1);
    }
}
```

## Complexity analysis

Assuming the side length of the grid is $n$, the time complexity is $O(n^2)$.