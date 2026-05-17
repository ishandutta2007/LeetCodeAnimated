# LeetCode Problem No. 36: Valid Sudoku

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from LeetCode Problem No. 36: Valid Sudoku.

## Title

Determine whether a 9x9 Sudoku is valid. You only need to verify whether the numbers you have filled in are valid according to the following rules.


	The numbers 1-9 can only appear once in each line.
	Numbers 1-9 can appear only once in each column.
	Numbers 1-9 can appear only once in each 3x3 house separated by a thick solid line.


Example 1:

```
enter:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

Example 2:


```
enter:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Except that the first number in the first line is changed from 5 to 8, the other numbers in the spaces are the same as Example 1.
     But since there are two 8s in the 3x3 palace in the upper left corner, this sudoku is invalid.
```

Example 3:


```
Input: [1,3,5,6], 7
Output: 4
```


Example 4:


```
Input: [1,3,5,6], 0
Output: 0
```



## Idea analysis

### One-time traversal method

#### Ideas

This question requires determining whether a value exists, so using Hash Map is a good choice.
Because each row, column, and cell needs to be judged separately, three HashMap arrays with a length of 9 need to be established to store the values ​​of the row, column, and cell respectively.

Traverse this 9*9 array through a two-level loop, store the current grid value in the corresponding HashMap, and determine whether it has been stored before. If it has been stored, exit and return false. If so, skip it, so that you only need to traverse one side.

### Animation understanding

![](../Animation/HashMap.gif)

#### Code implementation


```java
//Time complexity: O(n)
//Space complexity: O(1)
class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap[] row = new HashMap[9];
        HashMap[] column = new HashMap[9];
        HashMap[] box = new HashMap[9];
        for (int i = 0; i < 9; i++) {
            row[i] = new HashMap(9);
            column[i] = new HashMap(9);
            box[i] = new HashMap(9);
        }
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int boxIndex=i / 3 * 3 + j / 3;
                if ((boolean) row[i].getOrDefault(board[i][j], true)) {
                    return false;
                }
                if ((boolean) column[j].getOrDefault(board[i][j], true)) {
                    return false;
                }
                if ((boolean) box[boxIndex].getOrDefault(board[i][j], true)) {
                    return false;
                }
                row[i].put(board[i][j], false);
                column[j].put(board[i][j], false);
                box[boxIndex].put(board[i][j], false);
            }
        }

        return true;
    }
}
```

 ![](../../Pictures/qrcode.jpg)