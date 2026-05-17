# LeetCode Issue No. 139: Word Splitting

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 139 on LeetCode: Word Splitting.

### Title description

Given a **non-empty** string *s* and a dictionary *wordDict* containing a **non-empty** word list, determine whether *s* can be split by spaces into one or more words that appear in the dictionary.

**illustrate:**

- Words from the dictionary can be reused when splitting.
- You can assume that there are no duplicate words in the dictionary.



### Question analysis

It is somewhat similar to **Split Palindrome String**, both are splitting, but if this question is solved using the depth-first search method, the answer is timeout. Students who don't believe it can try it~

Why does it time out?

Because using depth-first search will repeatedly calculate the splittable situation of some bits, the optimization of this situation definitely requires dynamic programming to handle.

If you don’t know about dynamic programming, you can read Xiao Wu’s previous 10,000-word article, which introduces the concept of dynamic programming in more detail.

Here, you only need to define an array boolean[] memo, where the i-th bit memo[i] represents whether the string to be split can be successfully split from bit 0 to bit i-1.

Then calculate each bit individually whether it can be split successfully.



### Animation description

None~

### Code implementation



```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        int max_length=0;
        for(String temp:wordDict){
            max_length = temp.length() > max_length ? temp.length() : max_length;
        }
        // memo[i] indicates whether the string ending with i - 1 in s can be split by wordDict
        boolean[] memo = new boolean[n + 1];
        memo[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = i-1; j >= 0 && max_length >= i - j; j--) {
                if (memo[j] && wordDict.contains(s.substring(j, i))) {
                    memo[i] = true;
                    break;
                }
            }
        }
        return memo[n];
    }
}
```

![](../../Pictures/qrcode.jpg)
