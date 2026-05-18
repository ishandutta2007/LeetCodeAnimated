

# yanghui triangle

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/yf0dp.png)

> This article was first published on the public account "Learn Algorithm in Five Minutes" and is one of the series of articles [Illustrated LeetCode](https://github.com/MisterBooo/LeetCodeAnimation).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)
>


Yang Hui's triangle should be a mathematical knowledge that everyone has been exposed to very early. It has many interesting properties:

- Each number is equal to the sum of the left and right numbers in the previous row, that is, *C(n+1,i) = C(n,i) + C(n,i-1)*
- Each row of numbers is symmetrical, starting from 1 and gradually getting larger
- The number in row n has n items
- The m-th number in the n-th row is equal to the n-m + 1 number, which is one of the properties of [combination number](https://baike.baidu.com/item/%E7%BB%84%E5%90%88%E6%95%B0)
- Each term [coefficient] in the expansion of ( a + b ) <sup>n</sup> (https://baike.baidu.com/item/%E7%B3%BB%E6%95%B0) corresponds to each term in the ( n + 1 )th row of Yang Hui's triangle.
- 。。。



## Yang Hui Triangle

The title comes from question No. 118 on LeetCode: Yang Hui Triangle. The difficulty of the questions is Easy, and the current passing rate is 61.8%.

### Title description

Given a non-negative integer *numRows, *generate the first *numRows* rows of Yang Hui's triangle.

![img](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/ehk16.gif)

In Yang Hui's triangle, each number is the sum of the numbers to its upper left and upper right.

**Example:**

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

### Question analysis

> This question often appears in exercises in major universities.

For this question, use property 1: the first and last numbers in each line are both 1. Starting from the third line, each number in the middle is the sum of the left and right numbers in the previous line.

### Code implementation

```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        
     List<List<Integer>> result = new ArrayList<>();
     if (numRows < 1) return result;

    for (int i = 0; i < numRows; ++i) {
      //Expansion
      List<Integer> list = Arrays.asList(new Integer[i+1]);
      list.set(0, 1); list.set(i, 1);
      for (int j = 1; j < i; ++j) {
        //Equal to the sum of the left and right numbers in the previous row
        list.set(j, result.get(i-1).get(j-1) + result.get(i-1).get(j));
      }
      result.add(list);
     }
    return result;   
        
    }
}

```



## Yang Hui Triangle II

The question comes from question No. 119 on LeetCode: Yang Hui Triangle II. The difficulty of the questions is Easy, and the current passing rate is 55.5%.

### Title description

Given a non-negative index *k* where *k* ≤ 33, return the *k*th row of Yang Hui's triangle.

![img](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/ehk16.gif)

In Yang Hui's triangle, each number is the sum of the numbers to its upper left and upper right.

**Example:**

```
Input: 3
Output: [1,3,3,1]
```

**Advanced:**

Can you optimize your algorithm to *O*(*k*) space complexity?

### Question analysis

The difficulty and thinking point of this question is that the question has additional restrictions. The program can only use O(k) extra space, so it cannot print each line through accumulation.

The law of Yang Hui's triangle is still used here, a very hidden law: for the same row of Yang Hui's triangle, the (i + 1)-th item is `(k-i)/(i + 1)` times of the i-th item.

for example:

- Item 0 of k-th index row: 1
- Item 1 of k-th index row: 1 * k
- Item 2 of the k-th index row: 1 * k * ( k - 1) / 2
- Item 3 of the k-th index row: [1 * k * ( k - 1) / 2 ] * ( k - 2 ) / 3



### Code implementation

```java
class Solution {
  public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>(rowIndex + 1);
        long index = 1;
        for (int i = 0; i <= rowIndex; i++) {
            res.add((int) index);
            index = index * ( rowIndex - i ) / ( i + 1 );
        }
        return res; 
  }
}
```



## An interesting conclusion

Interested friends can search for Li Yongle's video about lottery probability, which mentions many magical characteristics of Yang Hui's triangle.
![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/ggto5.gif)


![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/bhn6z.png)