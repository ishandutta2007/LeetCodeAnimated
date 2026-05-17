# LeetCode Issue No. 66: Plus One

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The topic shared today comes from question No. 66 on LeetCode: Add one. The difficulty of the questions is Easy, and the current passing rate is 39.0%.

### Title description

Given a non-negative integer represented by a **non-empty** array of **integers**, add one to the number.

The highest digit is stored at the beginning of the array, and each element in the array stores only one number.

You can assume that other than the integer 0, this integer will not start with zero.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The input array represents the number 123.
```

**Example 2:**

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The input array represents the number 4321.
```

**Example 3:**

```
//In order to better understand the meaning of the question, add an example based on the comments in the LeetCode comment area.
Input: [9,9]
Output: [1, 0, 0]
Explanation: The input array represents the number 100.
```

### Question analysis

This question is very simple, and the meaning of the question is easy to understand. The important point to pay attention to is the **carry problem**.

* If the last digit (ones digit) of the array is less than 9, just add 1 to the ones digit and return

* If the last digit of the array (ones digit) is equal to 9, set the bit (ones digit) to 0, and a carry occurs, and then observe the previous digit (tens)

* * If the previous digit (tens digit) is less than 9, just add 1 to the tens digit and return
  * If the previous bit (tens place) is equal to 9, set the bit (tens place) to 0 and a carry occurs, then observe the previous bit (hundreds place)

* By analogy, finally observe whether the first bit after the operation is 0. If it is 0, add 1 to the front (**Example 3**)

  

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/iejo0.gif)

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/15na7.gif)



### Code implementation

```java
public class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        //Traverse forward from the end of the array
        for (int i = digits.length - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                //No carry, return directly
                return digits;
            }
            //To generate a carry, this bit needs to be assigned a value of 0
            digits[i] = 0;
        }
        //A carry is generated overall, and the array length needs to be changed by adding 1
        int[] res = new int[n + 1];
        res[0] = 1;
        return res;
    }
}
```

![](../../Pictures/qrcode.jpg)

