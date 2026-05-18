# LeetCode Problem No. 350: Intersection of Two Arrays II

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from Question No. 350 on LeetCode: Intersection of Two Arrays II. The difficulty of the questions is Easy, and the current passing rate is 41.8%.

### Title description

Given two arrays, write a function to calculate their intersection.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

**illustrate:**

- The number of occurrences of each element in the output result should be consistent with the number of occurrences of the element in the two arrays.
- We can ignore the order of output results.

**Advanced:**

- What if the given array is already sorted? How would you optimize your algorithm?
- If the size of *nums1* is much smaller than *nums2*, which approach is better?
- If the elements of *nums2* are stored on disk, disk memory is limited, and you cannot load all elements into memory at once, what should you do?

### Question analysis

Use of container class [map](https://zh.cppreference.com/w/cpp/container/map).

- Traverse num1 and store the elements and frequencies of num1 through the map container record
- Traverse num2 and find if there is the same element in record (the storage frequency of this element is greater than 0). If so, use the map container resultVector to store it, and at the same time reduce the frequency of the element by one.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/3kc4w.gif)

### Code implementation

```
// 350. Intersection of Two Arrays II
// https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
// Time complexity: O(nlogn)
// Space complexity: O(n)
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {

        map<int, int> record;
        for(int i = 0 ; i < nums1.size() ; i ++){
             record[nums1[i]] += 1;
        }
        
        vector<int> resultVector;
        for(int i = 0 ; i < nums2.size() ; i ++){
            if(record[nums2[i]] > 0){
                resultVector.push_back(nums2[i]);
                record[nums2[i]] --;
            }
        }
        
        return resultVector;
    }
};
```

#### Execution results

![img](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/xdsii.png)



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/3zqhi.png)