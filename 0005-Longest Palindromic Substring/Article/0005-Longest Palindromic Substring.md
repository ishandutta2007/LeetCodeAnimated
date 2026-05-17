# LeetCode Problem No. 5: Longest Palindrome

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com
>

The title comes from question No. 5 on LeetCode: The longest palindrome string. The difficulty level of the questions is Medium, and the current pass rate is 29%.

## Title description

Given a string, find the longest palindrome string in this string.

## Example

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

```
Input: "cbbd"
Output: "bb"
```

## Question analysis

This question is a typical question that looks simple, but is actually not simple.

Let's start with a simple algorithm. The simplest method is of course brute force. Since we need to find the longest palindrome string, one way is to find all the substrings of the s string, and then compare them one by one to see if they form a palindrome. This is of course feasible, but if we briefly analyze the complexity, we will find that this is not acceptable. For a string of length n, we can find a substring of it by randomly selecting two positions. Then the number of two positions we choose is $C_n^2 = \frac{n(n-1)}{2}$. For each substring, we need to traverse it once to determine whether it is a palindrome, so the overall complexity is $O(n^3)$.

But if you are very familiar with palindrome strings, you will find that this can actually be optimized. Because what we require is the longest palindrome string, if we determine the position of the symmetry center, the longest palindrome string it can form is determined. So we only need to traverse all palindrome string centers and find the longest palindrome string found in each center. In this way, our complexity is reduced by one dimension and becomes $O(n^2)$.

There are two forms of palindrome strings. One is an odd palindrome, that is, the center of the palindrome is a character, such as aba. There is also an even palindrome, where the center of the palindrome is between two characters, such as abba. We need to discuss these two situations separately.

We write the code:

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        ret = ''
        for i in range(n):
            # Odd palindromes
            l, r = i, i
            while s[l] == s[r]:
                l -= 1
                r += 1
                if l < 0 or r >= n:
                    break
            if r - l - 1 > len(ret):
                ret = s[l+1: r]
            
            # Even palindrome situation
            l, r = i-1, i
            while l >= 0 and s[l] == s[r]:
                l -= 1
                r += 1
                if l < 0 or r >= n:
                    break
            if r - l - 1 > len(ret):
                ret = s[l+1: r]
                
        return ret
```

It’s not over yet. Next, we introduce a classic palindrome string solving algorithm-Manacher, also called the horse-drawn cart algorithm.

First, we need to unify the two situations of odd palindrome and even palindrome. This is also very convenient. We process the original string and insert a separator character # between two adjacent characters. For example, abcd is converted into #a#b#c#d#. Generally, we will also add characters at the beginning and end to prevent out-of-bounds, such as $&, etc. After that we maintain two values, namely id and mr. mr represents the farthest position to the right of the currently constructed palindrome string, and id represents the symmetry center corresponding to this position. Based on this position id and mr, we can quickly find the length of the legal palindrome string that can be formed by the current position i.

We assume that the radius of the legal palindrome string formed by each position is p[i], then for the position i, we can get p[i] >= min(mr - i, p[id * 2 - i]). Among them, id * 2 - i is the symmetric position of the i position with respect to the id, and the part of the palindrome string that is symmetrical about i and is smaller than the mr position is also symmetrical with respect to the id. So if p[id * 2 - i] < mr - i, it means that the symmetric position of i with respect to id cannot break through the limit of id symmetry. Since the symmetry point of i cannot break through the limit, then i obviously cannot break through the limit. In the same way, if p[id * 2 - i] > mr - i, it means that the symmetric position of i is not restricted by id, but this just means that i is restricted. Because if i can also break through the limit of mr, it means that the symmetry range of id can be expanded, which is contrary to our premise assumption. So only when p[id * 2 - i] == mr - i, i can continue to extend.

If you can understand the above relationship, the entire algorithm is already very clear. If you don't understand, it doesn't matter. You can look at the animation below, which will show it more clearly.

After understanding the above algorithm process, the remaining work is simple. We only need to maintain id and mr while solving p[i].

Finally, let's look at the complexity of the algorithm. Why is this an O(n) algorithm? The reason is very simple, we only need to pay attention to the variable mr. The variable mr is incrementing, and the size of each increment of mr is actually the length of p[i] - (mr - i). So although it seems that we have used two loops, since mr can only be incremented at most n times, it is still an O(n) algorithm.

#### Animation description

![](../Animation/LeetCode5.gif)

#### Code implementation

```python
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        # Insert # between all characters
        def transform(s):
            return '$#' + '#'.join(list(s)) + '#&'
        
        if s == '':
            return s
        # initialization
        s = transform(s)
        p = [0 for _ in range(len(s)+1)]
        mr, id_ = 0, 0
        # The first and last characters are special characters, so the subscripts range from 1 to len(s)-2
        for i in range(1, len(s)-1):
            # Calculate p[i]
            p[i] = 1 if mr <= i else min(p[2*id_-i], mr - i)

            # Only when the current i has got rid of the ID restriction, or is the third situation, can it be continued to extend.
            # This is just an optimization, it can still run without this judgment.
            if mr <= i or p[2*id_-i] == mr - i:
                while s[i - p[i]] == s[i + p[i]]:
                    p[i] += 1

                if i + p[i] > mr:
                    mr, id_ = i + p[i], i
        # Find the longest subscript
        id_ = p.index(max(p))
        # Get the entire palindrome string
        palindromic = s[id_ - p[id_]+1: id_ + p[id_]]
        # Filter out # and restore to original characters
        return ''.join(filter(lambda x: x != '#', list(palindromic)))
        
```

![](../../Pictures/qrcode.jpg)