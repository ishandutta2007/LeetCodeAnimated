# LeetCode Issue No. 26: Remove Duplicates in Sorted Array

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 26 on LeetCode: Remove duplicates in a sorted array. The difficulty of the questions is Easy, and the current passing rate is 48.8%.

### Title description

Given a sorted array, you need to remove duplicate elements in place so that each element appears only once, and return the new length of the array after removal.

Instead of using extra array space, you must modify the input array in-place and do it using O(1) extra space.

**Example 1:**

```
Given array nums = [1,1,2],

The function should return a new length of 2, and the first two elements of the original array nums are modified to 1, 2.

You don't need to consider elements in the array beyond the new length.
```

**Example 2:**

```
Given nums = [0,0,1,1,1,2,2,3,3,4],

The function should return a new length of 5, and the first five elements of the original array nums are modified to 0, 1, 2, 3, 4.

You don't need to consider elements in the array beyond the new length.
```

**illustrate:**

Why is the returned value an integer but the output answer is an array?

Please note that the input array is passed by "reference", which means that modifications to the input array in the function are visible to the caller.

You can imagine the internal operation as follows:

```
// nums is passed by "reference". In other words, no copies of actual parameters are made
int len = removeDuplicates(nums);

// Modifying the input array in the function is visible to the caller.
// Based on the length returned by your function, it will print out all elements in the array within that length range.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

### Question analysis

Use fast and slow pointers to record traversed coordinates.

- Initially both pointers point to the first number
- If both pointers point to the same number, the fast pointer moves forward one step
- If different, both pointers move forward one step
- When the fast pointer completes the entire array, the current coordinates of the slow pointer plus 1 is the number of different numbers in the array.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/4y1ec.gif)



### Code implementation

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int pre = 0, cur = 0, n = nums.size();
        while (cur < n) {
            if (nums[pre] == nums[cur]){
              cur++;  
            } else{
                ++pre;
                nums[pre] = nums[cur];
                cur++;
            } 
        }
        return pre + 1;
    }
};
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/j3v4r.png)