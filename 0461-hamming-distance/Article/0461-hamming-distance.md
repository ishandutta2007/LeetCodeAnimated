### Title description

The [Hamming distance](https://baike.baidu.com/item/Hamming distance) between two integers refers to the number of different binary positions corresponding to the two numbers.

Given two integers `x` and `y`, calculate the Hamming distance between them.

Example:

```
Input: x = 1, y = 4

Output: 2

explain:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
```

### Question analysis

First, use the XOR operation to find the positions where the corresponding bits of the two numbers are different, and then count the number of these positions.

The statistical solution method is explained by referring to the source code of the Integer.bitCount() method in Java. The number of 1's after XOR is obtained through a fixed number of steps.

Step 1: Add the odd digits and the even digits to get the number of 1's in each two digits, and record the number in these two digits.

> i = i - (( i >>> 1 ) & 0x55555555 )
>
> ```
> 0x55555555 => 01 01 01 01 ... 01 01
> i & 0x55555555 takes out the 1 in the odd digit
> (i >>> 1) & 0x55555555 Take out the 1 in the even number digit
> For example, in the case of two digits, there are four situations in total: 00 11 01 10
> Assume i = 00 11 01 10
> i          & 0x55555555 = 00 11 01 10 
>                           01 01 01 01
>                           -----------
>                           00 01 01 00
> (i >>> 1)  & 0x55555555 = 00 01 10 11 
> 													01 01 01 01
> 													-----------
> 													00 01 00 01
>Sum the number of 1's in odd digits and the 1's in even digits:
> 00 01 01 00
> 00 01 00 01
> -----------
> 00 10 01 01
> Combining the original numbers, it can be seen that 00 (00: no 1) 11 (10: two 1s) 01 (01: 1 1) 10 (01: 1 1)
> 
> When each two digits are counted by addition, there are a total of four situations [i & 01 + (i>>>1) & 01]:
> 11: 01 + 01 = 10 = 2, 10: 00 + 01 = 01 = 1, 01: 01 + 00 = 01 = 1, 00: 00 + 00 = 00 = 0 
> When each two digits are counted by subtraction, there are a total of four situations [i - (i>>>1) & 01]:
> 11: 11 - 01 = 10 = 2, 10: 10 - 01 = 01 = 1, 01: 01 - 00 = 01 = 1, 00: 00 + 00 = 00 = 0
> It can be found that the result is the same, but one bit operation is missing!
> 
> After counting the number of 1's in every two digits, you can start adding two two digits, four four digits... to find the total number of 1's
> ```

Step 2: Find the number of 1's in every four digits by adding the number of 1's in two adjacent digits, and store the result in the four digits.

> i = ( i & 0x33333333 ) + (( i >>> 2 ) & 0x33333333 )
>
> ```
> 0x55555555 => 0011 0011 0011 ... 0011 0011
> Continue the result of the previous step downward: 00 10 01 01
> i          & 0x33333333 = 0010 0101
> 													0011 0011
> 													---------
> 													0010 0001
> (i >>> 2)  & 0x33333333 = 0000 1001
> 													0011 0011
> 													---------
> 													0000 0001
> 												
> Use the sum to find the number of 1's contained in every four digits
> 0010 0001
> 0000 0001
> ---------
> 0010 0010
> Combining the original numbers, we can see that 0011 (0010: there are two 1s) 0110 (0010: there are two 1s)
> ```

Step 3: Find the number of 1's in every eight bits by adding the number of 1's in adjacent four bits, and store the result in the eight bits.

>i = ( i + ( i >>> 4 )) & 0x0f0f0f0f;
>
>```
>0x0f0f0f0f => 00001111 ... 00001111‬
>Continue the result of the previous step downward: 0010 0010
>i          & 0x0f0f0f0f = 00100010
>													00001111
>													--------
>													00000010
>(i >>> 4)  & 0x0f0f0f0f = 00000010
>													00001111
>													--------
>													00000010
>Use the sum to find the number of 1’s contained in every eight bits
>00000010
>00000010
>--------
>00000100
>Combined with the original numbers, we can see that 00110110 (00000100: there are four 1s)
>
>In the source code, four adjacent bits are added directly, and then the useless bits are cleared.
>```

Step 4: Find the number of 1's in every sixteen bits by adding the number of 1's in adjacent eight bits, and store the result in the sixteen bits.

> i = i + ( i  >>>  8 );
>
> ```
> Can be understood as ( i & 0x0f0f0f0f ) + (( i >>> 8 ) & 0x0f0f0f0f );
> 
> 0x0f0f0f0f => 00000000111111110000000011111111
> ```

Step 5: Find the number of all 1's in the int by adding the number of 1's in the first 16 digits and the number of 1's in the last 16 digits of the int type.

> i = i + ( i >>> 16 );
>
> ```
> Can be understood as (i & 0x0000ffff) + (( i >>> 8) & 0x0000ffff);
> 
> 0x0000ffff => 00000000000000001111111111111111‬
> ```

Step 6: Remove useless bits

> return i & 0x3f;
>
> ```
> The int type is 32 bits, that is, up to 0x100000 1s. In addition, the left bits are useless.
> 0x3f => 00111111‬
> ```

### Animation understanding

![](../Animation/Animation.mp4)


‎⁨

### Reference code

```java
class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y); 
    }
}
```

bitCount source code:

```java
public static int bitCount(int i) {
    i = i - ((i >>> 1) & 0x55555555);
    i = (i & 0x33333333) + ((i >>> 2) & 0x33333333);
    i = (i + (i >>> 4)) & 0x0f0f0f0f;
    i = i + (i >>> 8);
    i = i + (i >>> 16);
    return i & 0x3f;
}
```

### Complexity analysis

Time complexity: O(1)

Space complexity: O(1)