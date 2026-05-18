# LeetCode Issue No. 125: Validating Palindrome Strings

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from LeetCode Question No. 125: Verifying Palindrome Strings. This question is an algorithm question that **junior programmers** often encounter during interviews, and the interviewer likes the interviewer's handwriting!



### Title description

Given a string, verify whether it is a palindrome, considering only alphanumeric characters and ignoring the case of letters.

**Note:** In this question, we define the empty string as a valid palindrome string.

**Example 1:**

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**

```
Input: "race a car"
Output: false
```

### Question analysis

First understand a concept: the so-called palindrome is a string that has the same forward and reverse readings.

Let's first assume that we want to verify whether the word `level` is a palindrome string. Through the concept of positive and negative, it is easy to think of using double pointers to traverse the entire string from the beginning and end of the character. If they are the same, continue to search forward. If they are different, false will be returned directly.

The difference here from separately verifying whether a word is a palindrome string is that spaces and non-alphanumeric characters are added, but the actual method is the same:

First, create two pointers, left and right, and let them traverse the entire string starting from the beginning and end of the character respectively.

If you encounter a non-alphanumeric character, skip it and continue searching until you find the next alphanumeric character or end the traversal. If you encounter an uppercase letter, convert it to lowercase.

When both the left and right pointers find letters and numbers, and comparison can be made, compare the two characters. If they are equal, the two pointers move in their forward direction, and then continue to compare the two letters and numbers found respectively. If they are not equal, return false directly.

### Animation description

![](<https://bucket-1257126549.cos.ap-guangzhou.myqcloud.com/blog/pvbiv.gif>)

### Code implementation

Note: The `isLetterOrDigit` method determines whether the specified character is a letter or number.

```java
class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 0)
             return true;
        int l = 0, r = s.length() - 1;
        while(l < r){
            //Determine whether the specified character is a letter or number
            if(!Character.isLetterOrDigit(s.charAt(l))){
                l++;
            }else if(!Character.isLetterOrDigit(s.charAt(r))){
                r--;
            }else{
                if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r)))
                    return false;
                l++;
                r--;
            } 
        }
        return true;
    }
}

```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/k5tcp.png)