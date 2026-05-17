# LeetCode Issue No. 137: Numbers that appear only once II

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 137 on LeetCode: Number II that only appears once. The difficulty level of the questions is Medium, and the current pass rate is 66.7%.

### Title description

Given a non-empty array of integers, each element appears three times except for one element that appears only once. Find the element that appears only once.

illustrate:

Your algorithm should have linear time complexity. Can you do it without using extra space?

**Example 1:**

```
Input: [2,2,3,2]
Output: 3
```

**Example 2:**

```
Input: [0,1,0,1,0,1,99]
Output: 99
```

### Question analysis

Compared with [Single Number](https://leetcode.com/problems/single-number/), the conditions for inputting the array have changed. Except for one element in the array, it only appears once, and the other elements appear **three** times. The final question still asks you to find this element that only appears once. This question may seem impossible from the perspective of bit operations at first, but if you think from the perspective of sets, you may be able to think of a solution. If we traverse the elements in the array, during the traversal process, we will find that there are only three situations for each element, appearing once, twice, and three times**. Because what we are looking for is the element that appears once, and in the end, except for the element we are looking for, all other elements will appear three times, so we need to find a way to exclude elements that appear three times. At the beginning, you can think that we use two sets, set 1 is used to store elements that appear once, and set 2 is used to store elements that appear twice, so we can find the following logical correspondence:

```
If the traversed element is not in set 1 or set 2: The element appears for the first time and is added to set 1
If the traversed element is in set 1 but not in set 2: The element appears for the second time, and is removed from set 1 and added to set 2.
If the traversed element is not in set 1 but in set 2: The element appears for the third time and is removed from set 2
```

The above logical correspondence should be easy for you to understand, but what I want to say is that this can be done through bit operations. We don't need a real set, we just need to replace the set with an integer. How to explain it? Suppose we use the integer `ones` to represent set 1 and the integer `twos` to represent set 2. The values ​​of these two integers are initialized to 0. `ones ^ ele[i]` means adding element `ele[i]` to set 1. If the next element `ele[i + 1]` comes and `ele[i] != ele[i + 1]`, then `ones ^ ele[i] ^ ele[i + 1]` will definitely produce a non-zero value. As for what this value is, you don’t need to care. But if `ele[i] == ele[i + 1]`, then the result of `ones ^ ele[i] ^ ele[i + 1]` will definitely be 0. By now, you should know that through the XOR operation, we can already do it, add the elements that appear once to set 1, and remove the elements that appear twice from set 1. But this is not enough, because the element may appear three times. If it is just the above XOR expression, the element that appears for the third time will still be added to set 1. We also need to ensure that the element is not in set 2. `(ones ^ ele[i]) & (~twos)` can guarantee this. The same is true for set 2, `(twos ^ ele[i]) & (~ones)` guarantees that elements that do not exist in set 1 and do not exist in set 2 are added to set 2. If we update set 1 first, and then update set 2, we can achieve the logical correspondence we mentioned before. Having said that, if you still don't understand, then you can try to think of an element as a combination of bits with a value of 1. For example, the binary number of 12 is `0001 0100`. If 12 appears three times, then the third and fifth bits from the right to the left appear three times. The same is true when we put this conclusion in an array. For those bits that appear an integer multiple of 3, we need to eliminate them and find those bits that appear `3 * n + 1` times. Combining them together is the element we are looking for. The above bit operation does this. Rather than putting the elements into the set, we can also say **Put all the bits with a value of 1 of the element into the set**, which will be better understood.

<br>

### Animation demonstration

![](../Animation/137.gif)

### Code implementation
#### C++
```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int one=0, two=0;
        for(int n:nums)
        {
            one = (one ^ n) & (~two);
            two = (two ^ n) & (~one);
        }
        return one;
    }
};
```
#### Java
```java
class Solution {
    public int singleNumber(int[] nums) {
        int one=0, two=0;
        for(int n:nums)
        {
            one = (one ^ n) & (~two);
            two = (two ^ n) & (~one);
        }
        return one;
    }
}
```
#### Python
```python
class Solution(object):
    def singleNumber(self, nums):
        one = two = 0
        for n in nums:
            one = (one ^ n) & (~two)
            two = (two ^ n) & (~one)
        return one
```

![](../../Pictures/qrcode.jpg)
