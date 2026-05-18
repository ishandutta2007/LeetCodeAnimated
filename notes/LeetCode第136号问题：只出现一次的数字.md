# LeetCode Issue No. 136: Numbers that appear only once

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 136 on LeetCode: Numbers that only appear once. The difficulty of the questions is Easy, and the current passing rate is 66.8%.

### Title description

Given a **non-empty** array of integers, each element appears twice except for one element which appears only once. Find the element that appears only once.

**illustrate:**

Your algorithm should have linear time complexity. Can you do it without using extra space?

**Example 1:**

```
Input: [2,2,1]
Output: 1
```

**Example 2:**

```
Input: [4,1,2,1,2]
Output: 4
```

### Question analysis

According to the title description, due to the conditions that the time complexity must be O(n) and the space complexity be O(1), the sorting method cannot be used, and the map data structure cannot be used.

Programmer Xiao Wu thought about it all afternoon but didn't come up with it. The answer is to use **Bit Operation** to solve this problem.

Execute XOR operation on all elements, that is, a[1] ⊕ a[2] ⊕ a[3] ⊕...⊕ a[n]. The result is the number that only appears once, and the time complexity is O(n).

### XOR

The truth table of the XOR operation A ⊕ B is as follows:

| A    |  B   |    ⊕ |
| :--- | :--: | ---: |
| F    |  F   |    F |
| F    |  T   |    T |
| T    |  F   |    T |
| T    |  T   |    F |

### Animation demonstration

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/8720h.gif)



### Advanced version

There is an array of n elements. Except for two numbers that only appear once, the rest of the elements appear twice. Let you find out the numbers of these two numbers that only appear once. The time complexity is required to be O(n) and the memory space to be opened is fixed (irrespective of n).

#### Example:

Input: [1,2,2,1,3,4]
Output: [3,4]

### Re-analysis of the question

According to the previous algorithm of finding a different number, all elements are XORed here, and the result obtained is the XOR result of the two elements that only appear once.

Then, because these two elements that only appear once must be different, the binary forms of these two elements must have at least one bit that is different, that is, one is 0 and the other is 1. Now we need to find this bit.

According to the property of XOR, `the XOR of any number is equal to 0`, any bit that is 1 in the binary form of this number is the bit we are looking for.

Then, based on whether this bit is 1 or 0, the n elements of the array are divided into two parts.

- Exclusive-OR all the elements whose bit is 0, and the resulting number is one of the numbers that only appears once
- Exclusive-OR all the elements whose bit is 1, and the resulting number is another number that appears only once.

This solves the problem. Ignoring the process of finding different bits, the array is traversed twice, and the time complexity is O(n).

### Animation demonstration again

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/5uz1n.gif)





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/2hfta.png)