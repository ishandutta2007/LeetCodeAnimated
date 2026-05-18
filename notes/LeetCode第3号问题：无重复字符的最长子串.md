# LeetCode Problem No. 3: Longest substring without repeating characters

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 3 on LeetCode: The longest substring without repeated characters. The difficulty level of the questions is Medium, and the current passing rate is 29.0%.

### Title description

Given a string, please find the length of the longest substring that does not contain repeated characters.

**Example 1:**

```java
Input: "abcabcbb"
Output: 3
Explanation: Because the longest substring without repeated characters is "abc", its length is 3.
```

### Question analysis

Create a 256-bit integer array freg to establish a mapping between characters and their occurrence positions.

Maintain a sliding window. There are no repeated characters in the window. To expand the size of the window as much as possible, the window keeps sliding to the right.

- (1) If the currently traversed character has never appeared, then directly expand the right boundary;
- (2) If the currently traversed character has appeared before, reduce the window (the left index moves to the right), and then continue to observe the currently traversed character;
- (3) Repeat (1) (2) until the left index can no longer move;
- (4) Maintain a result res, update the result res with the window size that has appeared each time, and finally return res to obtain the result.

### Animation description

![Animation description](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/20ahe.gif)

### Code implementation

```c++
// sliding window
// Time complexity: O(len(s))
// Space complexity: O(len(charset))
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int freq[256] = {0};
        int l = 0, r = -1; //The sliding window is s[l...r]
        int res = 0;
        //The entire loop starts from the empty window l == 0; r == -1
        //The empty window ends when l == s.size(); r == s.size()-1
        // Gradually change the window in each loop, maintain freq, and record whether a new optimal value is found in the current window
        while(l < s.size()){
            if(r + 1 < s.size() && freq[s[r+1]] == 0){
                r++;
                freq[s[r]]++;
            }else { //r has ended || freq[s[r+1]] == 1
                freq[s[l]]--;
                l++;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
};
```

