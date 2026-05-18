# LeetCode Question No. 107: Level Traversal of Binary Tree II

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 107 on LeetCode: Level Traversal of Binary Trees II. The difficulty of the questions is Easy, and the current passing rate is 55.8%.

### Title description

Given a binary tree, return a bottom-up hierarchical traversal of its node values. (That is, traverse from left to right layer by layer from the layer where the leaf node is to the layer where the root node is)

For example:
Given a binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

Return its bottom-up hierarchical traversal as:

```
[
  [15,7],
  [9,20],
  [3]
]
```

### Question analysis

This problem requires the use of **queue**. The solution is similar to the previous article [One calculation per day: Binary Tree Level Order Traversal] (https://xiaozhuanlan.com/topic/8579460312). The difference lies in the final storage method.

- Create a queue
- Put the root node in first, then find the left and right child nodes of the root node
- Remove the root node. At this time, the elements in the queue are all the nodes in the next layer.
- Use a for loop to traverse and store the results in a one-dimensional vector
- After traversing, insert the one-dimensional vector into the two-dimensional vector
- By analogy, layer-order traversal can be completed



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/varp8.gif)



### Code implementation

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/9iccc.png)





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/tdqxb.png)