# LeetCode Problem No. 6: Snake Matrix

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com
>

The question comes from question No. 6 on LeetCode: Snake Matrix. The difficulty level of the questions is Medium, and the current passing rate is 35.1%.


## Title description

Given a string, and an integer n, arrange it into a snake shape of n lines and return it.

## Example

```
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

Given a string and the number of lines occupied by the serpentine arrangement, it is required to return the rearranged string

## Question analysis

This question is a simulation question. The requirement of the question is the answer. We only need to understand the meaning of the question and it can be easily realized.

What we ultimately want to output is the result of strings arranged in a snake shape and then concatenated in rows. That is to say, the column in which each letter is placed is not important, what is important is the row number in which it is placed. We can easily think of maintaining the letters placed in each row through an array, and finally concatenating the results of each row. So the only question remains, how do we know which row each letter should be placed on?

In fact, this is also regular. By observing the examples, we can find that the line number where each letter is placed first increases from 0 to n-1, and then decreases from n-1 to 0. We will simulate this process and place it character by character.

For example, the string is "PAYPALISHIRING", rowNum=4. We can create four empty strings:

“”
“”
“”
“”

Then we put them into these empty strings letter by letter according to the snake shape:

When the first letter p is placed, it becomes:

“p”
“”
“”
“”

Then put the second one:

“p”
“a”
“”
“”

Then the third one:

“p”
“a”
“y”
“”

After we have placed all the letters, we can get four strings like this:

“PIN”
“ALSIG”
“YAHR”
“PI”

Then just splice these four strings together.


#### Animation description

![](../Animation/LeetCode6.gif)

#### Code implementation

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Record the letters placed in each line
        rows = ['' for _ in range(numRows)]
        # Record the current line number
        cur_row = 0
        #Record whether the current placement order is from top to bottom, False means from bottom to top
        forward = True
        # numRows = 1 returns directly
        if numRows == 1:
            return s
        
        for i, c in enumerate(s):
            rows[cur_row] += c
            # Change line numbers according to order
            if forward:
                cur_row += 1
            else:
                cur_row -= 1
            # Determine whether to redirect based on the line number and current sequence
            if cur_row == numRows - 1 and forward:
                forward = False
            
            if cur_row == 0 and not forward:
                forward = True
            
        ret = ''
        for sc in rows:
            ret += sc
        return ret
```

![](../../Pictures/qrcode.jpg)