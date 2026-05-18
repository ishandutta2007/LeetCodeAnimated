# LeetCode Problem No. 1: Sum of Two Numbers

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)
>
> Video explanation: [[Follow programmer Xiao Wu’s illustration of LeetCode] LeetCode Question No. 1: The sum of two numbers](<https://www.bilibili.com/video/av51296602>)

The question comes from question No. 1 on LeetCode: The sum of two numbers. The difficulty of the questions is Easy, and the current passing rate is 45.8%.

### Title description

Given an integer array `nums` and a target value `target`, please find the **two** integers in the array whose sum is the target value, and return their array subscripts.

You can assume that each input will correspond to only one answer. However, you cannot reuse the same elements in this array.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9

Because nums[0] + nums[1] = 2 + 7 = 9
So it returns [0, 1]
```

### Question analysis

Use a lookup table to solve this problem.

Set up a map container record to record the value and index of the element, and then traverse the array nums.

* Use the temporary variable complement each time it traverses to save the difference between the target value and the current value
* Search record in this traversal to see if there is a value consistent with complement. If the search is successful, return the index value of the search value and the value of the current variable i
* If not found, save the element and index value i in record

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/mol6g.gif)

### Code implementation

```
// 1. Two Sum
// https://leetcode.com/problems/two-sum/description/
// Time complexity: O(n)
// Space complexity: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> record;
        for(int i = 0 ; i < nums.size() ; i ++){
       
            int complement = target - nums[i];
            if(record.find(complement) != record.end()){
                int res[] = {i, record[complement]};
                return vector<int>(res, res + 2);
            }

            record[nums[i]] = i;
        }

        return {};
    }
};

```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/wavdg.png)