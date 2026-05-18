# LeetCode Problem No. 15: Sum of Three Numbers

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 15 on LeetCode: The sum of three numbers.

### Title description

Given an array `nums` containing *n* integers, determine whether there are three elements *a, b, c in `nums` such that *a + b + c =* 0? Find all triplets that satisfy the condition and are not repeated.

### Question analysis

The question requires us to find three numbers and the sum is 0. Then, except for the case where the three numbers are all 0, there will definitely be negative numbers and positive numbers, so you can choose a number at the beginning, and then find the other two numbers. In this way, you only need to find two numbers and the sum is the opposite number of the first selected number. That is to say, you need to enumerate a and b and store c in the map.

It should be noted that there cannot be duplicate results among the returned results. The time complexity of such code is O(n^2). Here you can sort the original array first, and then traverse the sorted array. In this way, you can use double pointers to traverse all two array combinations that meet the meaning of the question with linear time complexity.

### Animation description

To be added

### Code implementation

### 

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        if (nums.empty() || nums.back() < 0 || nums.front() > 0) return {};
        for (int k = 0; k < nums.size(); ++k) {
            if (nums[k] > 0) break;
            if (k > 0 && nums[k] == nums[k - 1]) continue;
            int target = 0 - nums[k];
            int i = k + 1, j = nums.size() - 1;
            while (i < j) {
                if (nums[i] + nums[j] == target) {
                    res.push_back({nums[k], nums[i], nums[j]});
                    while (i < j && nums[i] == nums[i + 1]) ++i;
                    while (i < j && nums[j] == nums[j - 1]) --j;
                    ++i; --j;
                } else if (nums[i] + nums[j] < target) ++i;
                else --j;
            }
        }
        return res;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/m1phx.gif)