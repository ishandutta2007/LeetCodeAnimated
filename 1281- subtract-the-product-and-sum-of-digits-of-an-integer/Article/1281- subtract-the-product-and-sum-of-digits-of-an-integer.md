### Title description

Given an integer `n`, please help calculate and return the difference between the "product of the digits" and the "sum of the digits" of the integer.

Example 1:

```
Input: n = 234
Output: 15
explain:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
```

Example 2:

```
Input: n = 4421
Output: 21
explain:
The product of each digit = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
```

**hint:**

```
1 <= n <= 10^5
```

### Question analysis

1. Traverse each digit of the number through modulo operation

2. Use two variables to record the sum and product respectively during the traversal process.

### Animation understanding

![](../Animation/Animation.mp4)

‎⁨

### Reference code

```java
class Solution {
    public int subtractProductAndSum(int n) {
        int addResult = 0, mulResult = 1;
        while (n > 0) {
            int num = n % 10;
            n /= 10;
            addResult += num;
            mulResult *= num;
        }
        return mulResult - addResult;
    }
}
```



### Complexity analysis

Time complexity: O(logN)

Space complexity: O(1)