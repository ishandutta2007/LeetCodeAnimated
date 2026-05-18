# LeetCode Issue 877: The Stone Game

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

### Title description

Pleasant Goat and Big Big Wolf are playing games with piles of stones. Even-numbered piles of stones are arranged in a row, and each pile contains a positive integer number of stones `piles[i]`.

The game is decided by who has the most stones in their hand. The total number of stones is an odd number, so there is no tie.

Pleasant Goat and Big Big Wolf take turns, with Pleasant Goat starting first. Each turn, players take the entire pile of stones from the beginning or end of the row. This continues until there are no more pebbles left, at which point the player with the most pebbles wins.

Assuming that both Pleasant Goat and Big Big Wolf perform at their best, `true` is returned when Pleasant Goat wins the game and `false` is returned when Big Big Wolf wins the game.

### Question analysis

Give two examples to help understand the meaning of the question.

#### Example 1:

Input: [5, 3, 4, 5]

Output: true

**explain**:

Pleasant Goat starts first and can only take the first 5 or last 5 stones.

Assuming he takes the first 5, this line becomes [3, 4, 5].

If Big Big Wolf takes away the first 3, then the remaining ones are [4, 5]. Pleasant Goat takes away the last 5 and wins 10 points.

If Big Wolf takes away the last 5, then the remaining ones are [3, 4]. Pleasant Goat takes away the last 4 and wins 9 points.

This shows that taking the first 5 stones is a winning move for Pleasant Goat, so we return true .





#### Example 2:

Input: [5, 10000, 2, 3]

Output: true

**explain**:

Pleasant Goat starts first and can only take the first 5 or last 3 stones.

Assuming he takes the last 3, this line becomes [5, 10000, 2].

Big Gray Wolf will definitely take the first 5 in the remaining row, and this row becomes [10000, 2].

Then Pleasant Goat takes the first 10,000, winning a total of 10,003 points, and Big Big Wolf wins 7 points.

This shows that taking the last 3 stones is a winning move for Pleasant Goat, so we return true .

**This example shows that it is not necessary to pick the largest pile of rocks every time**.



### Question answer

When it comes to optimal solution problems, you must try to use **dynamic programming** to solve it.

Let’s take a look at Likou’s formal solution first:

Let's change the rules of the game so that whenever Big Wolf scores, it's deducted from Pleasant Goat's score.

Let `dp(i, j)` be the maximum score that Pleasant Goat can obtain, where the number of stones remaining in the pile is `piles[i], piles[i+1], ..., piles[j]`. This is natural in score games: we want to know the value of every position in the game.

We can formulate the recursion of `dp(i,j)` in terms of `dp(i + 1,j)` and `dp(i,j-1)`, and we can use dynamic programming to not repeat the work in this recursion. (This method can output the correct answer because the states form a DAG (Directed Acyclic Graph).)

When the number of stones in the remaining pile is `piles[i], piles[i+1], ..., piles[j]`, the player on his turn can have up to 2 actions.

You can find out whose turn it is by comparing `j-i` with `N modulo 2`.

If the player is the Pleasant Goat, then it will take away `piles[i]` or `piles[j]` stones, increasing its score. After that, the total score is `piles[i] + dp(i+1, j)` or `piles[j] + dp(i, j-1)`; we want the maximum possible score among them.

If the player is Big Big Wolf, then it will take away `piles[i]` or `piles[j]` stones, reducing Pleasant Goat's score by this amount. After that, the total score is `-piles[i] + dp(i+1, j)` or `-piles[j] + dp(i, j-1)`; we want the smallest possible score among them.

The code is as follows:

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/af7fm.jpg)



The above code is not too complicated. Of course, it doesn’t matter if you don’t understand it. It will not affect the solution of the problem. Please see the mathematical analysis below.



### Mathematical analysis

Because the number of stones is an odd number, there are only two outcomes, lose or win.

Pleasant Goat starts to take the stones first, take whatever you want! Then compare the number of stones:

1. If there are more stones than the opponent, you win;
2. If the number of stones is less than that of your opponent, you can reverse the order in which you take the stones and the order in which your opponent takes the stones (**Because it is an even-numbered pile of stones, you can all reverse them**), and you will still win.

So the code is as follows:

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        return true;
    }
}
```

Let me introduce to you a simple strategy as a reference. Using this strategy can ensure that the Pleasant Goat who takes the stone first will definitely win.

First, calculate the total number of stones in the odd-numbered and even-numbered stone piles respectively, and then compare them. If the total number of stones in the odd-numbered piles is more, Pleasant Goat will always guarantee that it will choose the odd-numbered stone pile, otherwise it will choose the even number.

For example, assuming that the pile of stones is [5, 10000, 2, 3], then the total number of odd-numbered piles is 7 (numbered starting from 1), and the total number of even-numbered piles is 1003, then Pleasant Goat must ensure that it always chooses the even-numbered piles, that is, the fourth and second piles, to win.

However, the **result obtained by this selection method may not be the optimal solution**. For example, the pile of stones is [2, 1, 3, 5]. When using dynamic programming to ensure that both Pleasant Goat and Big Big Wolf choose the optimal solution, Pleasant Goat will take away two piles of chess pieces [2, 5], while Big Gray Wolf will take away two piles [1, 3]. However, using this strategy can still guarantee the victory of Pleasant Goat even if it is not the optimal solution, so as the first player, Pleasant Goat must have a way to win the game.

How did you feel after reading it?

There was a lot of complaints in the comment area of ​​LeetCode about this question: **What kind of stupid question is this! **

Maybe people who have participated in competitions such as ACM will smile slightly: How can you say that you are an acmer if you don’t know tens of thousands of routines? The questions that ordinary people like us are surprised by are completely broken by them, with all kinds of weird and instant solutions.







![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/lnwx8.png)
