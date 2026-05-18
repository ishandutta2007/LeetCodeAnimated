# LeetCode Problem No. 191: Number of bits 1

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 191 on LeetCode: Number of bits 1. The difficulty of the questions is Easy, and the current passing rate is 52.3%.

### Title description

Write a function that takes an unsigned integer as input and returns the number of digits with '1' in its binary expression (also known as [Hamming weight](https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F)).

 

**Example 1:**

```
Enter: 00000000000000000000000000001011
Output: 3
Explanation: In the input binary string 00000000000000000000000000001011, a total of three bits are '1'.
```

**Example 2:**

```
Enter: 00000000000000000000000010000000
Output: 1
Explanation: In the input binary string 00000000000000000000000010000000, a total of one bit is '1'.
```

**Example 3:**

```
Enter: 11111111111111111111111111111101
Output: 31
Explanation: In the input binary string 11111111111111111111111111111101, a total of 31 bits are '1'.
```

 

**hint:**

- Note that in some languages ​​(such as Java) there is no unsigned integer type. In this case, both the input and output will be specified as signed integer types, and this should not affect your implementation since the internal binary representation of the integer is the same regardless of whether it is signed or unsigned.
- In Java, the compiler uses two's complement notation to represent signed integers. So, in **Example 3** above, the input represents the signed integer `-3`.

 

**Advanced**:
How would you optimize your algorithm if this function is called multiple times?

### Question analysis

This question is relatively simple, and there are many solutions, including displacement method, bit operation method, table lookup method, secondary table lookup method, etc.

Observe the binary representation of the two numbers n and n-1: For the binary representation of the number n-1, compared to the binary representation of n, the 1 in the last digit will become 0, and the 0s after the 1 in the last digit will all become 1, and the other bits will remain the same.

For example, n = 8888, its binary value is **10001010111000**

Then n - 1 = 8887, its binary value is **10001010110111**

After bitwise AND operation: n & (n-1) = **10001010110000**

In other words: through the operation **n&(n-1)**, it can eliminate the last 1**.

So you can eliminate the 1 at the end of n by performing the n&(n-1) operation. The number of times it is eliminated indicates how many 1 there are.



### Animation description

None~

### Code implementation

```c++
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while(n > 0){
            cnt++;
            n = n & (n - 1);
        }
        return cnt;
    }
};
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/se6v6.png)