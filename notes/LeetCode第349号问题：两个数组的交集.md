# LeetCode Problem No. 349: Intersection of Two Arrays

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 349 on LeetCode: Intersection of two arrays. The difficulty of the questions is Easy, and the current passing rate is 62.3%.

### Title description

Given two arrays, write a function to calculate their intersection.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

**illustrate:**

- Each element in the output result must be unique.
- We can ignore the order of output results.

### Question analysis

Use of container class [set](https://zh.cppreference.com/w/cpp/container/set).

- Traverse num1 and store the elements of num1 through the set container record
- Traverse num2 and find whether there are the same elements in record. If so, use the set container resultSet to store them.
- Convert resultSet to vector type

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/xfx1k.gif)

### Code implementation

```
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> record;
        for(int i = 0; i < nums1.size(); i ++){
            record.insert(nums1[i]);
        }
        
        set<int> resultSet;
        for(int i = 0; i < nums2.size();i++){
            if(record.find(nums2[i]) != record.end()){
                resultSet.insert(nums2[i]);
            }
        }
        
        vector<int> resultVector;
        for(set<int>::iterator iter=resultSet.begin(); iter != resultSet.end();iter++){
            resultVector.push_back(*iter);
        }
        return resultVector;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/y7jcl.png)