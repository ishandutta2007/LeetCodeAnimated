

#LeetCode Question No. 122: Best time to buy and sell stocks II

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

In the previous article [**Dynamic Programming and Stock Issues**](https://github.com/MisterBooo/LeetCodeAnimation/tree/master/notes/LeetCode Question No. 122: The Best Time to Buy and Sell Stocks II.md), Xiao Wu used the idea of ​​​​dynamic programming to analyze and write routine codes, but there are still some friends who don’t understand it very well. Today, I will come up with a new question to analyze it from another angle, hoping to help everyone understand it easier.

### Title description

The question comes from Question No. 122 on LeetCode: The Best Time to Buy and Sell Stocks II. The difficulty of the questions is Easy, and the current passing rate is 53.0%.

### Title description

Given an array whose *i*th element is the price of a given stock on day *i*.

Design an algorithm to calculate the maximum profit you can make. You can complete as many trades as possible (buy and sell a stock multiple times).

**Note**: You cannot participate in multiple trades at the same time (you must sell your previous shares before buying again).

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (stock price = 1) and sell on day 3 (stock price = 5). The profit from this transaction = 5-1 = 4.
     Subsequently, if you buy on the 4th day (stock price = 3) and sell on the 5th day (stock price = 6), the profit from this transaction = 6-3 = 3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (stock price = 1) and sell on day 5 (stock price = 5). The profit from this transaction = 5-1 = 4.
     Note that you cannot buy stocks back-to-back on Days 1 and 2 and then sell them later.
     Because you are participating in multiple trades at the same time, you must sell your previous shares before buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no trade is completed, so the maximum profit is 0.
```

### Question analysis

Let's think about it from a practical scenario. Suppose you are in the stock market. What is the ideal operation if you want to get the maximum profit?

Of course **buy low and sell high**!

Take a simple array as an example [100, 1, 20, 81]. If you scan it with the naked eye, if you buy it on the second day and sell it on the fourth day, you will get the highest profit (81 - 1) = 80.

So why can we know to sell on the fourth day but not on the third day?

In fact, please note that the question does not limit the number of transactions. You can sell it on the third day. However, if you find that it has risen on the fourth day, you can buy it back on the third day.

That is ` (81 - 1) = [( 20 - 1 ) + ( 81 - 20 )]`.

In other words, the four actions of buying on the second day, selling on the third day, buying on the third day, and selling on the fourth day are consistent with the results of buying on the second day and selling on the fourth day.

**So as long as today’s price is higher than yesterday, sell**! (You can buy it again anyway)

To sum up, observe from the next day. If the current price (today) is higher than the previous price (yesterday), add the difference to the profit (because we can buy yesterday and sell today. If the price is higher tomorrow, we can also buy today and sell tomorrow). By analogy, the maximum profit can be found after traversing the entire array.

### Image description

![The best time to buy and sell stocks II](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/nkvdj.png)

### Code implementation

```java
//Programmer Xiao Wu
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 1 ; i < prices.length; i++){
            if (prices[i] > prices[i-1]){
                 profit  = profit + prices[i] - prices[i - 1];
             }
        }
        return profit;
            
    }
}
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/4s1oh.png)



