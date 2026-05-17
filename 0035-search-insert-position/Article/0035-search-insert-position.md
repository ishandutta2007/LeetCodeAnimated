# LeetCode Issue No. 35: Search for insertion position

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from LeetCode Question No. 35: Search for insertion position.

## Title

Given a sorted array and a target value, find the target value in the array and return its index. If the target value does not exist in the array, returns the position at which it will be inserted sequentially.
You can assume that there are no duplicate elements in the array.


Example 1:

```
Input: [1,3,5,6], 5
Output: 2
```

Example 2:


```
Input: [1,3,5,6], 2
Output: 1
```

Example 3:


```
Input: [1,3,5,6], 7
Output: 4
```


Example 4:


```
Input: [1,3,5,6], 0
Output: 0
```



## Idea analysis

### Violent cycle method

This question seems to be very simple, it is a question that tests the search algorithm. The simplest is brute force search.

#### Ideas

Traverse this array, and then if the current value is consistent with the target value target or less than the target value target, then return the current subscript. The time complexity of this solution is O(N)

### Animation understanding

![](../Animation/violent search.gif)

#### Code implementation


```java
//Time complexity: O(n)
//Space complexity: O(1)
class Solution {
    public int searchInsert(int[] nums, int target) {
        int i=0;
        for(;i<nums.length;i++){
            if (nums[i]>=target){
                break;
            }
        }
        return i;
    }
}
```

### Dichotomy

#### Ideas

In addition to the brute force method, another method we can use to find values ​​in a sorted array is the dichotomy method. The idea is still the same as the improved brute force loop method. First find the left and right boundaries, and then calculate, which can save half the time each time. The time complexity is O(logn)

#### Code implementation

```java
//Time complexity: O(lon(n))
//Space complexity: O(1)
class Solution {
    public int searchInsert(int[] nums, int target) {
        if (target>nums[nums.length-1]) {
            return nums.length;
        }
        int left=0;
        int right=nums.length-1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;

    }
}
```
 ![](../../Pictures/qrcode.jpg)