## LeetCode Problem No. 1137: Nth Tabonacci Number

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal blog: www.zhangxiaoshuai.fun

**This question is selected from question 1137 in leetcode, easy level, current pass rate is 52.4%**

### Title description:

```txt
The Tabonacci sequence Tn is defined as follows:
T0 = ​​0, T1 = 1, T2 = 1, and under the condition that n >= 0, Tn+3 = Tn + Tn+1 + Tn+2
Given an integer n, please return the value of the nth Tabonacci number Tn.

Example 1:
Input: n = 4
Output: 4
explain:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

hint:
    0 <= n <= 37
    The answer is guaranteed to be a 32-bit integer, i.e. answer <= 2^31 - 1.
```

### Question analysis:
If you have been exposed to the Fibonacci sequence before, it is very easy to have a solution to this problem. We have the following three methods (two serious methods, hahaha) to solve this problem:

```
1. Recursion (but AC cannot be used in leetcode, and the time limit is exceeded, but the code will still be displayed)
2. Dynamic programming (this kind of problem is all about finding the unknown by knowing the previous ones, so it is best to use dp)
3. Violence (show your wits, just watch it for fun)
```

### GIF animation demonstration:

![](../Animation/1137-Tribonacci.gif)

## Code:

### Recursive version:

```java
public int tribonacci(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    }
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n -3);
}
```

### Dynamic programming

```java
int[] dp = new int[38];
public int tribonacci(int n) {
    if (dp[n] != 0) {
        return dp[n];
    }
    if (n == 0) {
        return 0;
    } else if (n == 1 || n == 2) {
        return 1;
    } else {
        int res = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);
        dp[n] = res;
        return res;
    }
}
```

### Violent law (very violent, hahahaha...)

```java
public int tribonacci(int n) {
    int[] Ts = {0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 				10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 					2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 						181997601, 334745777, 615693474, 1132436852, 2082876103};
    return Ts[n];
}
```

