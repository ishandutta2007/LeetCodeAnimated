

# A brief discussion of what dynamic programming is and related "stock" algorithm questions

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

## Dynamic programming

### 1 Concept

  The **Dynamic Programming** algorithm splits the problem and defines the relationship between the problem state and the state, so that the problem can be solved in a recursive (or divide and conquer) manner. There are several important concepts that need to be clearly understood before learning dynamic programming.

  **Phase**: For a complete problem process, it is appropriately divided into several interconnected sub-problems. Each time a sub-problem is solved, it corresponds to a stage, and the solution of the entire problem is transformed into a solution in accordance with the order of the stages.

  **State**: The state represents the objective conditions at the beginning of each stage, that is, the known conditions when solving the sub-problem. Status describes the situation in the process of researching the problem.

  **Decision**: Decision-making means that when the solution process is in a certain state at a certain stage, different choices can be made based on the current conditions to determine the state of the next stage. This choice is called decision-making.

  **Strategy**: The decision sequence consisting of decisions at all stages is called the full-process strategy, or strategy for short.

  **Optimal strategy**: Among all strategies, find the strategy with the smallest cost and the best performance. This strategy is called the optimal strategy.

  **State transition equation**: The state transition equation is the evolution process of determining the state of two adjacent stages, describing how the states evolve.

### 2 Usage scenarios

Problems that can be solved by dynamic programming generally have three properties:

  (1) **Optimization**: If the solution to the sub-problem contained in the optimal solution of the problem is also optimal, the problem is said to have the optimal substructure, that is, it satisfies the optimization principle. The local optimum of a subproblem will lead to the global optimum of the entire problem. In other words, an optimal solution to the problem must contain an optimal solution to the sub-problem.

  (2) **No aftereffects**: That is, once the state of a certain stage is determined, it will not be affected by subsequent decisions in this state. That is to say, the process after a certain state will not affect the previous state, but is only related to the current state and has nothing to do with the state of other stages, especially the state of the stage that has not yet occurred.

   (3) **Overlapping sub-problems**: That is, the sub-problems are not independent, and a sub-problem may be used multiple times in the next stage of decision-making. (This property is not a necessary condition for the application of dynamic programming, but without this property, the dynamic programming algorithm will not have advantages compared with other algorithms)

### 3 Algorithm process

  (1) Divide into stages: Divide the problem into several stages according to the time or space characteristics of the problem.
  (2) Determine the state and state variables: describe the different states of the problem at different stages.
  (3) Determine the decision and write the state transition equation: Determine the decision based on the relationship between the states of the two adjacent stages.
  (4) Find boundary conditions: Generally speaking, the state transition equation is a recursive formula and must have a recursive boundary condition.
  (5) Design programs and solve problems

## Practical exercises

The following three algorithm questions are all derived from issues related to stock trading on LeetCode. We deal with this type of problems according to the algorithm flow of **dynamic programming**.

**Stock buying and selling** This type of question is given an input array, each element in it represents the daily stock price, and you can only hold one stock (that is, you must sell the previous stock before buying again). Generally speaking, there are the following questions:

- Can only be bought and sold once
- Can be bought and sold numerous times
- Can be bought and sold k times

You need to design an algorithm to maximize profits.

## Best time to buy and sell stocks

The question comes from question No. 121 on LeetCode: The best time to buy and sell stocks. The difficulty of the questions is Easy, and the current passing rate is 49.4%.

### Title description

Given an array whose *i*th element is the price of a given stock on day *i*.

If you are only allowed to complete one transaction at most (i.e. buying and selling a stock), design an algorithm to calculate the maximum profit you can make.

Note that you cannot sell a stock before buying it.

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (stock price = 1), sell on day 5 (stock price = 6), maximum profit = 6-1 = 5.
     Note that the profit cannot be 7-1 = 6, because the selling price needs to be greater than the buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no trade is completed, so the maximum profit is 0.
```

### Question analysis

We think about this problem according to the idea of ​​dynamic programming.

#### state

There are two states: **buy** and **sell**.

#### Transfer equation

For buying, you can sell after buying (enter the selling state), or you can no longer conduct stock transactions (remain in the buying state).

For selling, stock trading is no longer carried out after selling the stock (it is still in the selling state).

Only the money in hand counts as money, and the money in hand is equivalent to a loss after buying the stock of the day. In other words, buying on the same day means losing `-prices[i]`, selling on the same day means increasing `prices[i]`, and the total profit of selling on the same day is `buy+prices[i]`.

So we only need to consider which one is more profitable if we buy on the same day or if we buy before, and which one is more profitable if we sell on the same day or if we sell before.

- buy = max(buy, -price[i]) (Note: buy is negative by definition)
- sell = max(sell,  prices[i] + buy)

#### Boundary

On the first day, `buy = -prices[0]`, `sell = 0`, and finally return to sell.

### Code implementation

```java
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length <= 1)
            return 0;
        int buy = -prices[0], sell = 0;
        for(int i = 1; i < prices.length; i++) {
            buy = Math.max(buy, -prices[i]);
            sell = Math.max(sell, prices[i] + buy);
        
        }
        return sell;
    }
}
```



## The best time to buy and sell stocks II

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

#### state

There are two states: **buy** and **sell**.

#### Transfer equation

Comparing to the previous question, there can be unlimited buying and selling here, which means that the **buy** state can have the **sell** state before it, so the transfer equation for buying needs to change.

- buy = max(buy, sell - price[i])
- sell = max(sell,   buy + prices[i] )

#### Boundary

On the first day, `buy = -prices[0]`, `sell = 0`, and finally return to sell.

### Code implementation

```java
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length <= 1)
            return 0;
        int buy = -prices[0], sell = 0;
        for(int i = 1; i < prices.length; i++) {
            sell = Math.max(sell, prices[i] + buy);
            buy = Math.max( buy,sell - prices[i]);
        }
        return sell;
    }
}
```



## The best time to buy and sell stocks III

The question comes from question No. 123 on LeetCode: The best time to buy and sell stocks III. The difficulty of the questions is Hard, and the current passing rate is 36.1%.

### Title description

Given an array, the *i*th element is the price of a given stock on the *i*th day.

Design an algorithm to calculate the maximum profit you can make. You can complete up to *two* transactions.

**Note:** You cannot participate in multiple trades at the same time (you must sell your previous shares before buying again).

**Example 1:**

```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on the 4th day (stock price = 0) and sell on the 6th day (stock price = 3). The profit from this transaction = 3-0 = 3.
     Subsequently, if you buy on the 7th day (stock price = 1) and sell on the 8th day (stock price = 4), you can earn a profit = 4-1 = 3 from this transaction.
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

There is a limit of two transactions at most.

#### state

There are four states: **First Buy (fstBuy)**, **First Sell (fstSell)**, **Second Buy (secBuy)** and **Second Sell (secSell)**.

#### Transfer equation

There are at most two buys and two sells, which means that the **buy** state can have the **sell** state before it, and the **sell** state can have the **buy** state before it, so the transfer equations for both buying and selling need to change.

- fstBuy = max(fstBuy ，  -price[i]) 
- fstSell = max(fstSell，fstBuy + prices[i] )
- secBuy = max(secBuy, fstSell -price[i]) (affected by the first sell status)
- secSell = max(secSell ，secBuy + prices[i] )

#### Boundary

- Initially `fstBuy = -prices[0]`
- Sell directly after buying, `fstSell = 0`
- Buy and then sell and then buy again, `secBuy - prices[0]`
- Buy and sell again, buy and sell again, `secSell = 0`

Finally returns secSell.

### Code implementation

```java
class Solution {
    public int maxProfit(int[] prices) {
        int fstBuy = Integer.MIN_VALUE, fstSell = 0;
        int secBuy = Integer.MIN_VALUE, secSell = 0;
        for(int i = 0; i < prices.length; i++) {
            fstBuy = Math.max(fstBuy, -prices[i]);
            fstSell = Math.max(fstSell, fstBuy + prices[i]);
            secBuy = Math.max(secBuy, fstSell -  prices[i]);
            secSell = Math.max(secSell, secBuy +  prices[i]); 
        }
        return secSell;
        
    }
}
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/pr1o6.png)



