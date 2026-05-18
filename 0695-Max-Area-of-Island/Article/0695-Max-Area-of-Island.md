# LeetCode Illustration |

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

Author of this solution: nettee

## Title description

Given a non-empty two-dimensional array `grid` containing some `0` and `1`.

An **Island** is a combination of some adjacent `1` (representing land). The "adjacent" here requires that two `1` must be adjacent horizontally or vertically. You can assume that the four edges of the `grid` are surrounded by `0` (representing water).

Find the largest island area in the given 2D array. (If there are no islands, the returned area is `0`.)

**Example 1:**

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```


For the given matrix above it should return 6. Note that the answer should not be 11 because the island can only contain `1`s in four directions, horizontal or vertical.

**Example 2:**

```
[[0,0,0,0,0,0,0,0]]
```


For the given matrix above, returns 0.

Note: The length and width of the given matrix `grid` cannot exceed 50.

## Question analysis

The main idea of ​​​​this question is depth-first search. Every time you go to a grid with a value of 1, search the entire island and calculate the area of ​​the current island. Finally, the maximum value of the island area is returned.

The grid can be viewed as an undirected graph structure, with each grid adjacent to its four grids above, below, left, and right. If the coordinates of the four adjacent grids are legal and they are land, you can continue searching.

When doing depth-first search, be careful to avoid repeated traversals. We can change the land that has been traversed to 2, so that when we encounter 2, we will know that we have already traversed this grid and will not repeat the traversal.

## Animation understanding

![](../Animation/Animation.gif)

## Reference code

C++ code:

```C++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c] == 1) {
                    int a = area(grid, r, c);
                    res = max(res, a);
                }
            }
        }
        return res;
    }
    
    int area(vector<vector<int>>& grid, int r, int c) {
        if (!(inArea(grid, r, c))) {
            return 0;
        }
        if (grid[r][c] != 1) {
            return 0;
        }
        grid[r][c] = 2;
        
        return 1
            + area(grid, r - 1, c)
            + area(grid, r + 1, c)
            + area(grid, r, c - 1)
            + area(grid, r, c + 1);
    }
    
    bool inArea(vector<vector<int>>& grid, int r, int c) {
        return 0 <= r && r < grid.size()
            && 0 <= c && c < grid[0].size();
    }
};
```

Java code:

```Java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    int a = area(grid, r, c);
                    res = Math.max(res, a);
                }
            }
        }
        return res;
    }

    int area(int[][] grid, int r, int c) {
        if (!inArea(grid, r, c)) {
            return 0;
        }
        if (grid[r][c] != 1) {
            return 0;
        }
        grid[r][c] = 2;

        return 1 
            + area(grid, r - 1, c)
            + area(grid, r + 1, c)
            + area(grid, r, c - 1)
            + area(grid, r, c + 1);
    }

    boolean inArea(int[][] grid, int r, int c) {
        return 0 <= r && r < grid.length 
            && 0 <= c && c < grid[0].length;
    }
}
```

Python code:

```Python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    a = self.area(grid, r, c)
                    res = max(res, a)
        return res
    
    def area(self, grid: List[List[int]], r: int, c: int) -> int:
        if not self.inArea(grid, r, c):
            return 0
        if grid[r][c] != 1:
            return 0
        grid[r][c] = 2
        
        return 1 \
            + self.area(grid, r - 1, c) \
            + self.area(grid, r + 1, c) \
            + self.area(grid, r, c - 1) \
            + self.area(grid, r, c + 1)
            
    def inArea(self, grid: List[List[int]], r: int, c: int) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
```



## Complexity analysis

Assuming the side length of the grid is n, the time complexity is O(n²).