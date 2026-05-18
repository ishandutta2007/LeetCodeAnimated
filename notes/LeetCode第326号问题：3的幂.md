# LeetCode Question No. 326: Powers of 3

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 326 on LeetCode: Powers of 3. The difficulty of the questions is Easy, and the current passing rate is 43.5%.

### Title description

Given an integer, write a function to determine whether it is a power of 3.

**Example 1:**

```
Input: 27
Output: true
```

**Example 2:**

```
Input: 0
Output: false
```

**Advanced:**
Can you solve this problem without using loops or recursion?

### Question analysis

The normal idea is to keep dividing by 3 to see if the final iteration quotient is 1. The code of this kind of thinking uses loops, which is not high enough.

The trick here is to use the knowledge of number theory: the prime factor of a power of 3 is only 3**.

The question requires input of int type. The range of positive numbers is 0 - 2<sup>31</sup>. The maximum power of 3 allowed in this range is 3<sup>19 </sup>= 1162261467. Then just check whether this number is divisible by n.

### Animation description

To be added

### Code implementation



```java
class Solution {
    public boolean isPowerOfThree(int n) {
         return n > 0 && 1162261467 % n == 0;
    }
}
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/fzqbe.png)