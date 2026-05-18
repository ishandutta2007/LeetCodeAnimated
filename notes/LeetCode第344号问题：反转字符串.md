# LeetCode Issue No. 344: Reverse a string

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from LeetCode question No. 344: Reverse a string. The interviewer’s favorite algorithm question is to ask you to write it by hand!

### Title description

Write a function that reverses the input string. The input string is given as a character array `char[]`.

Instead of allocating extra space to another array, you must modify the input array in place, using O(1) extra space to solve the problem.

You can assume that all characters in the array are printable characters in the [ASCII](https://baike.baidu.com/item/ASCII) code table.

**Example 1:**

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

### 

### Question analysis

This question is not difficult. Just go from the two ends to the middle and swap the characters on both sides. Note that you only need to write it in whiteboard programming, and be careful not to use advanced functions such as reverse() to solve the problem. . .

### Animation description

![](<https://bucket-1257126549.cos.ap-guangzhou.myqcloud.com/blog/ariy2.gif>)

### Code implementation

```
class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j){
            swap(s[i],s[j]);
            i++;
            j--;
        }
        return s;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/bksj7.png)