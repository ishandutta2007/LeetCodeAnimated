# LeetCode Issue No. 20: Valid Parentheses

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 20 on LeetCode: Valid Parentheses. The difficulty of the questions is Easy, and the current passing rate is 37.8%.

### Title description

Given a string that only includes `'('', `')'`, `'{'`, `'}'`, `'['`, `']'`, determine whether the string is valid.

A valid string must satisfy:

1. The left bracket must be closed by a right bracket of the same type.
2. The left bracket must be closed in the correct order.

Note that the empty string is considered a valid string.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

### Question analysis

This question asks us to verify whether the input string is a bracket string, including braces, square brackets and parentheses.

Here we use **stack**.

- Iterate over the input string
- If the current character is a left half bracket, push it onto the stack
- If you encounter a right half bracket, **Classification discussion:**
- 1) If the stack is not empty and is the corresponding left half bracket, remove the top element of the stack and continue the loop
- 2) If the stack is empty at this time, return false directly.
- 3) If it is not the corresponding left half bracket, otherwise it returns false

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/xu55u.gif)

### Code implementation

```
class Solution {
public:
    bool isValid(string s) {

        stack<char> stack;
        for( int i = 0 ; i < s.size() ; i ++ )
            if( s[i] == '(' || s[i] == '{' || s[i] == '[')
                stack.push(s[i]);
            else{

                if( stack.size() == 0 )
                    return false;

                char c = stack.top();
                stack.pop();

                char match;
                if( s[i] == ')' ){
                    match = '(';
                }
                else if( s[i] == ']' ){
                    match = '[';
                }
                else{
                    match = '{';
                }

                if(c != match)  return false;
            }

        if( stack.size() != 0 )
            return false;

        return true;
    }
};
```

![](../../Pictures/qrcode.jpg)