# LeetCode Issue No. 75: Color Classification

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from Question No. 75 on LeetCode: Color Classification. The difficulty level of the questions is Medium, and the current passing rate is 51.8%.

### Title description

Given an array containing *n* elements in red, white and blue, sort them **in place** so that elements of the same color are adjacent and arranged in the order of red, white and blue.

In this question, we use the integers 0, 1, and 2 to represent red, white, and blue respectively.

**Notice:**
This problem cannot be solved using the sorting functions in the code base.

**Example:**

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Advanced:**

- An intuitive solution is to use a counting sorted two-pass scan algorithm.
  First, iteratively calculate the number of elements 0, 1, and 2, and then rewrite the current array in order of 0, 1, and 2.
- Can you come up with a one-pass scan algorithm using only constant space?

### Question analysis

Combined with the application of three-way quick partition partition idea.

Set two indexes, one for sliding `zero` from left to right, and one for sliding `two` from right to left.

* Traverse `nums`, when the value of `nums[i]` is 1, `i++`;
* When the value of `nums[i]` is 2, the value of `two` is first decremented by 1, and then exchanges `nums[i]` and `nums[two]`. At this time, the value of `nums[i]` is observed;
* When the value of `nums[i]` is 0, `zero++`, then exchange `nums[i]` and `nums[zero]`, `i++`; when `i = two`, end the loop.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/6g5tm.gif)

### Code implementation

```
//The idea of ​​three-way quick sorting
// The entire array is traversed only once
// Time complexity: O(n)
// Space complexity: O(1)
class Solution {
public:
    void sortColors(vector<int> &nums) {

        int zero = -1;          // [0...zero] == 0
        int two = nums.size();  // [two...n-1] == 2
        for(int i = 0 ; i < two ; ){
            if(nums[i] == 1){
                 i ++;
            }else if (nums[i] == 2){
                 two--;
                 swap( nums[i] , nums[two]);
            }else{ // nums[i] == 0
                 zero++;
                 swap(nums[zero] , nums[i]);
                 i++;
            }
        }
    }
};

```

![](../../Pictures/qrcode.jpg)