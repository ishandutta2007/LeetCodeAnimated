# LeetCode Problem No. 295: Median of Data Streams

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 295 on LeetCode: Median of Data Stream. The difficulty level is Hard and the current pass rate is 33.5%.

### Title description

The median is the number in the middle of an ordered list. If the list length is an even number, the median is the average of the two middle numbers.

For example,

The median of [2,3,4] is 3

The median of [2,3] is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

- void addNum(int num) - Adds an integer from the data stream to the data structure.
- double findMedian() - Returns the median of all elements so far.

**Example:**

```java
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```



### Question analysis

This question gives us a data stream and asks us to find the median. For dynamic (flowing) data such as data flow, if array storage is used, it will be very inefficient if it is sorted every time a new piece of data comes in.

The commonly used data structures for processing dynamic data are stacks, queues, binary trees, and heaps.

In this question, we use the **heap** data structure.

First, the data is divided into two parts. The data located in the **maximum heap** above is smaller than the data in the **minimum heap** below.

In order to ensure that data is evenly distributed into the two heaps, the difference in the number of data in the two heaps cannot exceed 1 during dynamic operations.

In order to ensure that **all data in the max heap is smaller than the data in the min heap**, during the operation, the newly added data needs to be compared with the maximum value of the max heap or the minimum value of the min heap.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/slcao.gif)

### Code implementation



```java
class MedianFinder {
    public PriorityQueue<Integer> minheap, maxheap;
    public MedianFinder() {
        //Maintain a minimum heap of larger elements
        maxheap = new PriorityQueue<Integer>(Collections.reverseOrder());
        //Maintain a maximum heap of smaller elements
        minheap = new PriorityQueue<Integer>();
    }
    
    // Adds a number into the data structure.
    public void addNum(int num) {
        maxheap.add(num);
        minheap.add(maxheap.poll());
        if (maxheap.size() < minheap.size()) {
            maxheap.add(minheap.poll());
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (maxheap.size() == minheap.size()) {
            return (maxheap.peek() + minheap.peek()) * 0.5;
        } else {
            return maxheap.peek();
        }
    }
};
```







![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/k2ihh.gif)