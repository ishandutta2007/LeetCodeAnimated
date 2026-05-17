# LeetCode Illustration | 48. Rotate Image

## Title description

Given an n × n 2D matrix representing an image.

Rotate the image 90 degrees clockwise.

**illustrate:**

You have to rotate the image in place, which means you need to modify the input 2D matrix directly. **Please do not** use another matrix to rotate the image.

**Example 1:**

```
Given matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the input matrix in place so that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Example 2:**

```
Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

Rotate the input matrix in place so that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

## Question analysis

The main difficulty of this question is how to rotate the matrix **in place**.

We found that an element in the matrix will return to its original position after being rotated four times. That is, the positions of these four elements are swapped with each other during rotation. For example, the four positions corresponding to the element `(i, j)` are:

+ `(i, j)`
+ `(N-1-j, i)`
+ `(N-1-i, N-1-j)`
+ `(j, N-1-i)`

In order to rotate these four elements, we can use a temporary variable to save one of the elements, and then let several elements be assigned values ​​in sequence.

So, how many such four-element groups are there in total? This depends on the situation. If $n$ is an even number, this is equivalent to dividing the matrix into four blocks, and the number of elements in each block is $ (n/2) \times (n/2)$. If $n$ is an odd number, the center element of the matrix does not move with the rotation, and the remaining elements are divided into four blocks, and the number of elements in each block is $\lfloor n/2 \rfloor \times \lceil n/2 \rceil$. We just do a four-element rotation on all elements in a block.

## Animation understanding

![](../Animation/Animation.gif)

## Reference code

```Java
class Solution {
    public void rotate(int[][] matrix) {
        int N = matrix.length;
        for (int i = 0; i < N/2; i++) {
            for (int j = 0; j < (N+1)/2; j++) {
                int t = matrix[i][j];
                matrix[i][j] = matrix[N-1-j][i];
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j];
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i];
                matrix[j][N-1-i] = t;
            }
        }
    }
}
```

## Complexity analysis

+ Time complexity: $O(n^2)$.
+ Space complexity: $O(1)$.

