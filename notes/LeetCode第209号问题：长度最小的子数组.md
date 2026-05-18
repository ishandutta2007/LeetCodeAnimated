# LeetCode Problem No. 209: Minimum length subarray

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 209 on LeetCode: Minimum length subarray. The difficulty level of the questions is Medium, and the current pass rate is 25.8%.

### Title description

Given an array containing **n** positive integers and a positive integer **s, find the smallest contiguous subarray in the array whose sum **≥ s**. **If there is no contiguous subarray that meets the condition, return 0.

**Example:**

```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: Subarray [4,3] is the continuous subarray with the smallest length under this condition.
```

**Advanced:**

If you have completed the solution with *O*(*n*) time complexity, please try the solution with *O*(*n* log *n*) time complexity.

### Question analysis

Define two pointers left and right to record the left and right boundary positions of the subarray respectively.


* (1) Let right move right until the sum of the subarrays is greater than or equal to the given value or right reaches the end of the array;

* (2) Update the shortest distance, move the left image to the right by one position, and subtract the moved value from sum;

* (3) Repeat steps (1) (2) until right reaches the end and left reaches the critical position



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/0ga4f.gif)

Set the length of the sliding window to 0, located at the leftmost end of the number axis.

##### 1. The right end R of the sliding window starts to move until the interval meets the given conditions, that is, the sum is greater than 7. At this time, it stops at the third element 2, and the current optimal length is 4

![Figure 1](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/lo41y.jpg)



##### 2. The left end L of the sliding window starts to move, reduces the size of the sliding window, and stops at the first element 3. At this time, the sum of the intervals is 6, so that the sum of the intervals does not meet the given conditions (it is not greater than 7 at this time)

![Picture 2](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/j7qnc.jpg)



#### 3. The right end of the sliding window R continues to move and stops at the fourth element 4. At this time, the sum is 10, but the optimal length is still 4

![Picture 3](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/q8dxy.jpg)



### Code implementation

```
//The idea of ​​sliding window
// Time complexity: O(n)
// Space complexity: O(1)
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int l= 0,r = -1; // nums[l...r] is our sliding window
        int sum = 0;
        int result = nums.length + 1;
        while (l < nums.length){ // The left boundary of the window is within the range of the array, then the loop continues

            if( r+1 <nums.length && sum < s){
                r++;
                sum += nums[r];
            }else { // r has reached the end or sum >= s
                sum -= nums[l];
                l++;
            }

            if(sum >= s){
                result = (r-l+1) < result ? (r-l+1) : result ;
            }
        }
        if(result==nums.length+1){
            return 0;
        }
        return result;
    }
}

```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/0fotr.png)