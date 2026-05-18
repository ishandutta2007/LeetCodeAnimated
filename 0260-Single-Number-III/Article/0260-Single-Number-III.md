# LeetCode Issue No. 260: Number III that appears only once

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 260 on LeetCode: The number III that only appears once. The difficulty level of the questions is Medium, and the current pass rate is 72.1%.

## Title description

You are given an integer array `nums` in which exactly two elements appear exactly once and all remaining elements appear twice. Find those two elements that appear only once.

**Example:**

```
Input: [1,2,1,3,2,5]
Output: [3,5]
```

**Notice:**

1. The order of the result output is not important. For the above example, [5, 3] is also the correct answer.
2. Your algorithm should have linear time complexity. Can you do it using only constant space complexity?

<br>

## Question analysis

The third question only changes one thing from the first question, that is, except for **two** elements in the input array, which appear once, the rest appear twice. We can still think about this question from the solution of the first question. If we still follow the approach of the first question, the final answer we will get will be the result of `ele1 ^ ele2`. We need to think about how to get `ele1` and `ele2` from this result. First think about a question: what is the result of `ele1 ^ ele2`, or what kind of information is there? The XOR operation is to set the same bit position to 0 and the different bit position to 1. That is to say, the bit bit that is 1 in the XOR result of `ele1` and `ele2` is the bit bit of the two elements. Furthermore, we can use this bit bit to distinguish the two elements**. So based on the first question, a bit bit is used as a judgment condition to determine the XOR of the currently traversed element and that value, because at this time we require two values.

From the above questions, you can see the power of bit operations. The time complexity of the three series of questions is `O(n)`, but bit operations are lower-level operations, and the actual time consumption will be faster than normal operations. When understanding bit operations, **try to think about bit as the smallest unit, you may have different discoveries**.

<br>

### Code implementation

```java
public int[] singleNumber(int[] nums) {
    if (nums == null || nums.length == 0) {
        return new int[2];
    }
    
    int different = 0;
    for (int i : nums) {
        different ^= i;
    }

    // This operation is to take the last bit of different from left to right which is 1
    different &= -different;
    int[] ans = {0, 0};
    for (int i : nums) {
        if ((different & i) == 0) {
            ans[0] ^= i;
        } else {
            ans[1] ^= i;
        }
    }
    
    return ans;
}
```

<br>

### Animation demonstration
![](../Animation/260.gif)




![](../../Pictures/qrcode.jpg)