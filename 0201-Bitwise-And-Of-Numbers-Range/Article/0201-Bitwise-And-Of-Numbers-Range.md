# LeetCode Issue No. 201: Bitwise AND of Numeric Ranges

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 201 on LeetCode: Bitwise AND of Number Ranges. The difficulty level of the questions is Medium, and the current passing rate is 39.1%.

### Title description

Given a range [m, n] where 0 <= m <= n <= 2147483647, returns the bitwise AND of all numbers in the range, inclusive (m, n).

**Example 1:**

```
Input: [5,7]
Output: 4
```

**Example 2:**

```
Input: [0,1]
Output: 0
```

### Question analysis

Take [26, 30] as an example.

First, represent the range of numbers [26, 30] in binary:

**11**010　　**11**011　　**11**100　　**11**101　　**11**110

And the output of 24 is 11000 in binary.

It can be found that just find the binary **common part on the left**.

Therefore, you can first create a mask with 32 bits all being 1, and then shift one bit to the left each time, compare m and n to see if they are the same, if they are different, continue to shift one bit to the left until they are the same, and then sum m and mask to get the final result.

### Animation description

None yet

### Code implementation

```c++
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        unsigned int d = INT_MAX;
        while ((m & d) != (n & d)) {
            d <<= 1;
        }
        return m & d;
    }
};
```

![](../../Pictures/qrcode.jpg)
