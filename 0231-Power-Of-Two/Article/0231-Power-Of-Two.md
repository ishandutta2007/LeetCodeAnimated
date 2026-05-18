# LeetCode Problem No. 231: Powers of 2

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 231 on LeetCode: Powers of 2. The difficulty of the questions is Easy, and the current passing rate is 45.6%.

### Title description

Given an integer, write a function to determine whether it is a power of 2.

**Example 1:**

```
Input: 1
Output: true
Explanation: 2^0 = 1
```

**Example 2:**

```
Input: 16
Output: true
Explanation: 2^4 = 16
```

**Example 3:**

```
Input: 218
Output: false
```

### Question analysis

First, let’s analyze the binary writing of 2 to the power of 2:

![Form](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/3wdpd.jpg)

If you look closely, you can see that every power of 2 has only one 1, and the rest are all 0. According to this feature, you only need to determine whether the lowest bit is 1 each time, then shift to the right, and finally count the number of 1's to determine whether it is a power of 2.

The code is very simple:

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        int cnt = 0;
        while (n > 0) {
            cnt += (n & 1);
            n >>= 1;
        }
        return cnt == 1;
    } 
};
```

There is also an ingenious solution to this problem. Observe the above table again. If a number is a power of 2, then its binary number must have the highest bit as 1 and the rest as 0. If we subtract 1 at this time, the highest bit will drop by one, and the remaining 0 bits will now become 1. Then we add the two numbers and we will get 0.

For example, the third power of 2 is 8, and the binary digit is 1000, then `8 - 1 = 7`, where the binary digit of 7 is 0111.

### Image description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/1w9lq.jpg)

### Code implementation

Taking advantage of this property, it can be done with just one line of code.

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return (n > 0) && (!(n & (n - 1)));
    } 
};
```

![](../../Pictures/qrcode.jpg)
