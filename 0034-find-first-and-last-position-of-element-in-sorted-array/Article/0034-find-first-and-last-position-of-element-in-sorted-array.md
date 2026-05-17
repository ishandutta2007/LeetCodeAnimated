# LeetCode Problem No. 34: Find the first and last position of an element in a sorted array


The question comes from question No. 34 on LeetCode: find-first-and-last-position-of-element-in-sorted-array. The difficulty of the questions is medium.

### Title description

Given an array of integers **nums** sorted in ascending order, and a target value **target**. Find the start and end position of the given target value in the array.

The time complexity of your algorithm must be of the **O(log n)** level.

If the target value does not exist in the array, [-1, -1] is returned.


**Example:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
### Question analysis

The question requires that the time complexity is O(log n), so it is clear that the binary search method must be used.

First define two pointer variables to store the indexes of the left and right positions respectively. First, find the leftmost index of the target value. In order to prevent element loss through looping, the rightmost element is retained each time, and the pointer on the left is +1 when it moves. At the end of the loop, determine whether the target value is included in the array. If not, exit directly.
The one on the right is the same as the one on the left, just opposite.



### Animation description

![](..\Animation\Find the first and last position of an element in a sorted array.gif)

### Code implementation

```java
// 34. Next arrangement
// https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Time complexity: O(n)
// Space complexity: O(1)
class Solution {
    public int[] searchRange(int[] nums, int target) {
		int[] res = new int[] { -1, -1 };
		int left = 0;
		int right = nums.length - 1;
		int l = left;
		int r = right;
		while (left < right) {
			int mid = (left + right) / 2;
			if (nums[mid] < target) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		if (left>right||nums[left]!=target) {
			return new int[]{-1,-1};
		}
		while (l < r) {
			int mid = (l + r) / 2 + 1;
			if (nums[mid] > target) {
				r = mid - 1;
			} else {
				l = mid;
			}
		}
		if (left > right || left > r) {
			return new int[] { -1, -1 };
		} else {
			return new int[] { left, r };
		}
	}
}

```

 ![](../../Pictures/qrcode.jpg)
