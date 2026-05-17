# LeetCode Problem No. 9: Palindromes

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from LeetCode Problem No. 9: Palindrome Numbers. The difficulty level of the questions is Easy, and the current passing rate is 56.0%.

## Title description

Determine whether an integer is a palindrome. A palindrome number is an integer that reads the same in forward order (from left to right) and reverse order (from right to left).

**Example 1:**

```
Input: 121
Output: true
```

**Example 2:**

```
Input: -121
Output: false
Explanation: Reading from left to right, it is -121. Reading from right to left, it is 121- . Therefore it is not a palindrome.
```

**Example 3:**

```
Input: 10
Output: false
Explanation: Reading from right to left, it is 01. Therefore it is not a palindrome.
```

**Advanced:**

Can you solve this problem without converting the integer to a string?



## Question analysis

### Solution 1: Ordinary solution

One of the best-understood solutions is to first convert the **integer to a string**, and then split the string into an array. You only need to loop through half the length of the array to determine whether the corresponding elements are equal.

#### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/ods8b.gif)

#### Code implementation

```java
///Simple and crude, just take a look
class Solution {
    public boolean isPalindrome(int x) {
        String reversedStr = (new StringBuilder(x + "")).reverse().toString();
        return (x + "").equals(reversedStr);
    }
}
```



### Solution 2: Advanced solution---mathematical solution

Obtain the corresponding number in the integer for comparison through rounding and remainder operations.

For example: the number 1221.

- By calculating 1221 / 1000, we get the first place 1
- By calculating 1221 % 10, we get the last 1
- make comparisons
- Take out 22 and continue the comparison.

#### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/v3tkl.gif)

#### Code implementation

```java
class Solution {
    public boolean isPalindrome(int x) {
        //Boundary judgment
        if (x < 0) return false;
        int div = 1;
        //
        while (x / div >= 10) div *= 10;
        while (x > 0) {
            int left = x / div;
            int right = x % 10;
            if (left != right) return false;
            x = (x % div) / 10;
            div /= 100;
        }
        return true;
    }
}
```



### Solution Three: Advanced Solution---Smart Solution

When looking at palindromes intuitively, it feels like folding the numbers in half to see if they correspond one to one.

So the operation of this solution is to **take out the second half of the number and flip it**.

One point to note here is that since the number of digits in a palindrome can be odd or even, when its length is an even number, the folded half should be equal; when its length is an odd number, then after folded, one of the lengths needs to be reduced by one digit (divided by 10 and rounded).

The specific steps are as follows:

- Each time the remainder operation (%10) is performed, the lowest number is taken out: `y = x % 10`
- Add the lowest number to the end of the taken number: `revertNum = revertNum * 10 + y`
- For each lowest digit, x must be divided by 10
- Determine whether `x` is less than `revertNum`. When it is less than `revertNum`, it means that the number has been half or more than half.
- Finally, determine the odd and even numbers: if it is an even number, revertNum is equal to x; if it is an odd number, the middle number is in the lowest bit of revertNum, and it should be equal to x after dividing it by 10.

#### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/0siv7.png)

#### Code implementation

```java
class Solution {
    public boolean isPalindrome(int x) {
        //Thinking: Here you can think about why if the end is 0, you can directly return false.
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        return x == revertedNumber || x == revertedNumber / 10;
    }
}
```

![](../../Pictures/qrcode.jpg)