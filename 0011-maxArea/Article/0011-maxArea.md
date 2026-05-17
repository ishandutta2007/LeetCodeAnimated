## LeetCode Question No. 11: The container with the most water

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronize personal blog: www.zhangxiaoshuai.fun

**This question is selected from Question 11 of leetcode, medium level, current pass rate: 61.3%**

**Title description:**

```txt
Give you n non-negative integers a1, a2,...,an, each number represents a point (i, ai) in the coordinates. Draw n vertical lines within the coordinates,
The two endpoints of the vertical line i are (i,ai) and (i,0). Find the two lines such that the container they form with the x-axis can hold the most water.
Note: You cannot tilt the container and the value of n is at least 2.
Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

We should all have heard of the **Barrel Principle**. How much water can be filled in a wooden barrel depends on the shortest board; and this question can also correspond to the problem of filling water in a wooden barrel.
 It is easy to get---->**The capacity of the container to hold water = the shortest of the two vertical lines * the distance between the two lines **
 The current situation is that there are many lines that allow you to calculate the most water that can be filled between two. In fact, the brute force method can solve this problem, but its time complexity has also reached **O(n^2)**

OK, let’s try to use **brute force** to solve the problem first:

### 1. Violent law

Go directly to the code:

```java
public int maxArea(int[] height) {
    int res = 0;
    for(int i = 0;i < height.length;i++){
      for(int j = i+1;j < height.length;j++){
        int temp = Math.min(height[i],height[j]) * (j-i);
        res = Math.max(res,temp);
      }
    }
    return res;
}
```

The brute force method can pass the test, but you can see that the program execution time is not ideal.

```
Execution time: 440 ms, beats 17.44% of users among all Java submissions
Memory consumption: 39.9 MB, beats 37.86% of users among all Java submissions
```

### 2.Double pointer

Idea: Use two pointers (**resource** and **last**) to point to the first element and the last element of the array respectively. Then we calculate the capacity of water that can be accommodated between these two "lines" and update the maximum capacity (the initial value is 0); then we need to move the pointer pointing to the smaller element value one step forward, and then repeat the above steps until the **resource = last** loop ends.

**GIF animation demo:**

![](../Animation/maxArea.gif)

**Let’s take a look at the code:**

```java
public int maxArea(int[] height) {
    int resource = 0;
    int last = height.length - 1;
    int res = 0;
    while (resource < last) {
        if (height[resource] >= height[last]) {
            res = Math.max(res, (last - resource) * height[last]);
            last--;
        } else {
            res = Math.max(res, (last - resource) * height[resource]);
            resource++;
        }
    }
    return res;
}
```

**It can be clearly seen that although the memory consumption of the two is similar, the speed of double pointers is many times higher than the speed of brute force solution. **

Time complexity: **O(n)** Space complexity: **O(1)**

```
Execution time: 3 ms, beats 92.69% of all Java submissions
Memory consumption: 40.3 MB, beats 7.86% of users among all Java submissions
```

[Video demonstration](../Animation/maxArea.mp4)