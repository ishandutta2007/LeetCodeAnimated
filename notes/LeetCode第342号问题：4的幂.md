# LeetCode Problem No. 342: Powers of 4

The question comes from question No. 342 on LeetCode: Powers of 4. The difficulty of the questions is Easy, and the current passing rate is 45.3%.

### Title description

Given an integer (32-bit signed integer), write a function to determine whether it is a power of 4.

**Example 1:**

```
Input: 16
Output: true
```

**Example 2:**

```
Input: 5
Output: false
```

**Advanced:**
Can you solve this problem without using loops or recursion?

### Question analysis

The most direct way to solve this problem is to keep dividing by 4 to see if the final result is 1. See the code below:

```java
class Solution {
    public boolean isPowerOfFour(int num) {
         while ( (num != 0)  && (num % 4 == 0)) {
            num /= 4;
        }
        return num == 1;
    }
}
```

However, this code uses **loop**, which is not high enough.

For an integer, if the number is a power of 4, it must also be a power of 2.

Let's first list the powers of 2 to find out which numbers are powers of 4.

| Decimal | Binary |
| ------ | ------------------------------- |
| 2      | 10                              |
| 4 | **100** (1 in position 3) |
| 8      | 1000                            |
| 16 | **10000** (1 in position 5) |
| 32     | 100000                          |
| 64 | **1000000** (1 in position 7) |
| 128    | 10000000                        |
| 256 | **100000000** (1 in position 9) |
| 512    | 1000000000                      |
| 1024 | **10000000000** (1 at position 11) |

Find the rules: The binary representation of numbers that are powers of 4 always places 1 in the **odd digits**.

Previously, in Xiao Wu's article, the bit operation `n & (n - 1)` was used to determine whether a number is a power of 2. Similarly, bit operations can still be used here: perform bit operations on this number and a special number.

This special number has the following characteristics:

* Large enough, but no more than 32 bits, that is, the maximum is 1111111111111111111111111111111 (31 ones)

* Its binary representation has odd bits as 1 and even bits as 0

  A binary number that meets these two conditions is:

```java
1010101010101010101010101010101
```

**If you do an AND operation with a number that is a power of 4, you will still get a number that is a power of 4**.

Convert this binary number to hexadecimal representation: 0x55555555. Do you feel that your level is higher? . .

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/c0s9n.png)



### Image description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/ux5pa.jpg)



### Code implementation

```java
class Solution {
    public boolean isPowerOfFour(int num) {
        if (num <= 0)
			return false;
        //First determine whether it is a power of 2
		if ((num & num - 1) != 0)
			return false;
        //If the AND operation is followed by itself, it is a power of 4
		if ((num & 0x55555555) == num)
			return true;
		return false;
    }
}
```



