## **LeetCode Question No. 70: Climbing Stairs**

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 70 on LeetCode: Climbing Stairs. The difficulty level of the questions is Easy.

### Title description

Suppose you are climbing stairs. It takes `n` steps for you to reach the top.

You can climb `1` or `2` steps at a time. How many different ways can you climb to the top of a building?

**Note: Given n is a positive integer. **

### Example 1

> Input: 2
>
> Explanation: There are two ways to climb to the top of the building.
>
> 1. 1st order + 1st order
>
> 2. Level 2

### Question analysis

Try to think backwards and you will find that this problem can be decomposed into some sub-problems containing optimal sub-structures, and its optimal solution can be derived from its sub-problems
to effectively construct the optimal solution, so we can use `dynamic programming` to solve this problem.

The `i`th order can be obtained by the following two methods:

After step `(i - 1)` go up 1 step.

After step `(i - 2)` go up 2 steps

So the total number of ways to reach `i`th level is the sum of the number of ways to reach `(i - 1)`th level and `(i - 2)`th level.

`dp[i]dp[i]` represents the total number of methods that can reach the `i`th order, then the DP derivation formula is:

> $$
> dp[i] = dp[i − 1] + dp[i − 2]
> $$



### Animation understanding

<img src="../Animation/Animation.gif" alt="Animation" style="zoom:150%;" />

### Reference code

```javascript
/**
 * JavaScript description
 */
var climbStairs = function(n) {
    let temp = new Array(n+1);
    temp[1] = 1;
    temp[2] = 2;
    for (let i = 3; i < temp.length; i++) {
        temp[i] = temp[i-1] + temp[i-2];
    }
    return temp[n];
}
```

#### Complexity analysis

- Time complexity: `O(n)`, single loop to n.
- Space complexity: `O(n)`, the dpdp array uses n space.

### Further optimization

According to the derivation formula, it is not difficult to find that the result we require is the last item of the array, and the last item is the superposition of the previous values, so we only need two variables to store the values ​​​​of `i - 1` and `i - 2`.

```javascript
/**
 * JavaScript description
 */
var climbStairs = function(n) {
    if (n == 1) {
        return 1;
    }
    let first = 1,
        second = 2;
    for (let i = 3; i <= n; i++) {
       let third = first + second;
       first = second;
       second = third;
    }
    return second;
}
```

#### Complexity analysis

- Time complexity: O(n), single loop to n.
- Space complexity: O(1), using constant space.

![qrcode](../../Pictures/qrcode.jpg)