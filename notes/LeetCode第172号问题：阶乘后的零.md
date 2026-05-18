# LeetCode Question No. 172: Zero after factorial

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 172 on LeetCode: Zero after factorial. The difficulty of the questions is Easy, and the current passing rate is 38.0%.

### Title description

Given an integer *n*, return *n*! The number of zeros in the result's mantissa.

**Example 1:**

```
Input: 3
Output: 0
Explanation: 3! = 6, there is no zero in the mantissa.
```

**Example 2:**

```
Input: 5
Output: 1
Explanation: 5! = 120, there is 1 zero in the mantissa.
```

**Note:** The time complexity of your algorithm should be *O*(log *n*).

### Question analysis

The question is easy to understand, count how many zeros there are at the end of the number after factorial.

The simplest and crudest way is to multiply them first and then count them one by one.

In fact, you can find the pattern in the process of using the brute force method: **Among these 9 numbers, only 0 appears when 2 (its multiple) is multiplied by 5 (its multiple)**.

So, now the question becomes how many pairs of 2 and 5 can be matched in this factorial number.

To give a more complicated example:

 ` 10！ = 【 2 *（ 2 * 2 ）* 5 *（ 2 * 3 ）*（ 2 * 2 * 2 ）*（ 2 * 5）】`

At 10! Two pairs of 2 * 5 can be matched in this factorial number, so 10! There are 2 zeros at the end.

It can be found that the number of 2's after a number is split is definitely greater than the number of 5's, so how many pairs can be matched depends on the number of 5's. (For example, the ratio of men to women is very different now. The maximum number of opposite-sex couples there can be depends on the number of girls).

Then the question becomes **how many factors of 5 are there in the statistical factorial number**.

Note that numbers like 25 and 125 that contain more than just a 5 need to be taken into account.

For example `n = 15`. Then there are `3` `5` in `15!` (from `5`, `10`, `15`), so calculating `n/5` can be done.

But for example `n=25`, still calculating `n/5`, you can get `5` `5`, respectively from `5, 10, 15, 20, 25`, but `25` actually contains `2 `5`, this needs to be noted.

So in addition to calculating `n/5`, we also need to calculate `n/5/5, n/5/5/5, n/5/5/5/5, ..., n/5/5/5,,,/5` until the quotient is 0, and then sum it up.

### Code implementation

```java
public class Solution {
    public int trailingZeroes(int n) {
        return n == 0 ? 0 : n / 5 + trailingZeroes(n / 5);
    }
}
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/tvt94.png)







